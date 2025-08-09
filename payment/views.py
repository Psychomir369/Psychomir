# ایمپورت ماژول‌ها و مدل‌ها و فرم‌های موردنیاز برای مدیریت سفارش و تسویه‌حساب
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress, Order, OrderItem
from django.contrib import messages
from shop.models import Product, Profile
from django.contrib.auth.models import User

# نمایش صفحه موفقیت‌آمیز بودن پرداخت
def payment_success(request):
    return render(request, 'payment/payment_success.html', {})

# نمایش صفحه تسویه‌حساب و فرم آدرس ارسال با توجه به وضعیت ورود کاربر
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()

    # اگر کاربر لاگین کرده، فرم با اطلاعات آدرس قبلی پر می‌شود
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    else:
        # اگر کاربر مهمان باشد، فرم آدرس خالی نمایش داده می‌شود
        shipping_form = ShippingForm(request.POST or None)

    # همراه با اطلاعات سبد خرید و فرم ارسال checkout رندر قالب
    return render(request, 'payment/checkout.html', {
        'cart_products': cart_products,
        'quantities': quantities,
        'total': total,
        'shipping_form': shipping_form
    })

# ذخیره‌سازی موقت اطلاعات سفارش کاربر در نشست و نمایش صفحه تأیید سفارش
def confirm_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()

        # ذخیره اطلاعات فرم ارسال در نشست برای استفاده در مرحله بعد
        user_shipping = request.POST
        request.session['user_shipping'] = user_shipping

        # نمایش صفحه تأیید سفارش با جزئیات سبد خرید و آدرس
        return render(request, 'payment/confirm_order.html', {
            'cart_products': cart_products,
            'quantities': quantities,
            'total': total,
            'shipping_info': user_shipping
        })
    else:
        # view هدایت به صفحه اصلی در صورت دسترسی نامعتبر به این
        messages.success(request, 'دسترسی به این صفحه امکان‌پذیر نمی‌باشد.')
        return redirect("home")

# پردازش نهایی سفارش و ذخیره آن در دیتابیس (برای کاربران عضو و مهمان)
def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()

        # بازیابی اطلاعات آدرس از نشست
        user_shipping = request.session.get('user_shipping')
        full_name = user_shipping['shipping_full_name']
        email = user_shipping['shipping_email']
        full_address = f"{user_shipping["shipping_address"]}\n{user_shipping["shipping_city"]}\n{user_shipping["shipping_state"]}\n{user_shipping["shipping_zipcode"]}"

        # اگر کاربر لاگین کرده، سفارش به نام او ثبت می‌شود
        if request.user.is_authenticated:
            user = request.user
            new_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=full_address,
                mount_paid=total
            )
            new_order.save()

            odr = get_object_or_404(Order, id=new_order.pk)

            # ذخیره هر محصول سبد خرید به عنوان یک آیتم سفارش
            for product in cart_products:
                prod = get_object_or_404(Product, id=product.id)
                price = product.sale_price if product.is_sale else product.price

                for k, v in quantities.items():
                    if int(k) == product.id:
                        new_item = OrderItem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantity=v,
                            user=user
                        )
                        new_item.save()

            # پاک‌سازی نشست کاربر از اطلاعات موقتی و سبد قدیمی
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]
            Profile.objects.filter(user__id=request.user.id).update(old_cart="")

            messages.success(request, 'سفارش شما ثبت شد!')
            return redirect("home")
        else:
            # ثبت سفارش برای کاربران مهمان بدون حساب کاربری
            new_order = Order(
                full_name=full_name,
                email=email,
                shipping_address=full_address,
                mount_paid=total
            )
            new_order.save()

            odr = get_object_or_404(Order, id=new_order.pk)

            for product in cart_products:
                prod = get_object_or_404(Product, id=product.id)
                price = product.sale_price if product.is_sale else product.price

                for k, v in quantities.items():
                    if int(k) == product.id:
                        new_item = OrderItem(
                            order=odr,
                            product=prod,
                            price=price,
                            quantity=v
                        )
                        new_item.save()

            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]

            messages.success(request, 'سفارش شما ثبت شد!')
            return redirect("home")

    else:
        messages.success(request, 'دسترسی به این صفحه امکان‌پذیر نمی‌باشد.')
        return redirect("home")
