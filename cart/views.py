# ایمپورت‌های مورد نیاز برای رندر صفحات، مدیریت سبد خرید و مدل‌ها
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse
from django.contrib import messages

# نمایش خلاصه سبد خرید و ارسال اطلاعات به قالب
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()
    return render(request, 'cart_summary.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total})

# JSON افزودن محصول به سبد خرید و ارسال پاسخ 
def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("به سبد خرید اضافه شد!"))
        return response

# JSON به‌روزرسانی تعداد محصول در سبد خرید و ارسال پاسخ 
def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response

# JSON حذف محصول از سبد خرید و ارسال پاسخ 
def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, ("محصول از سبد خرید حذف شد!"))
        return response
