# ایمپورت کتابخانه‌ها و ماژول‌های مورد نیاز برای تعریف مدل‌ها، سیگنال‌ها و تاریخ شمسی
from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
import jdatetime

# مدل مربوط به آدرس ارسال کاربر که اطلاعات لازم برای ارسال سفارش را ذخیره می‌کند
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ارتباط با کاربر
    shipping_full_name = models.CharField(max_length=250)  # نام کامل گیرنده
    shipping_email = models.CharField(max_length=300)  # ایمیل گیرنده
    shipping_phone = models.CharField(max_length=25, blank=True)  # شماره تلفن
    shipping_address = models.CharField(max_length=250, blank=True)  # آدرس دقیق
    shipping_city = models.CharField(max_length=25, blank=True)  # شهر
    shipping_state = models.CharField(max_length=25, blank=True, null=True)  # استان
    shipping_zipcode = models.CharField(max_length=25, blank=True)  # کد پستی
    shipping_country = models.CharField(max_length=25, default='IRAN')  # کشور (پیش‌فرض ایران)
    shipping_old_cart = models.CharField(max_length=200, blank=True, null=True)  # سبد خرید قبلی (در صورت نیاز)

    class Meta:
        verbose_name_plural = 'ShippingAddress'  # نام نمایشی جمع برای پنل ادمین

    def __str__(self):
        return f'Shipping Address Form {self.shipping_full_name}'  # نمایش نام گیرنده در خروجی

# سیگنال برای ایجاد خودکار رکورد آدرس ارسال پس از ساختن یک کاربر جدید
def create_shipping_user(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)  # ساخت آدرس ارسال جدید مرتبط با کاربر
        user_shipping.save()

# اتصال سیگنال به مدل User برای ایجاد آدرس پس از ساخت کاربر
post_save.connect(create_shipping_user, sender=User)


# مدل مربوط به سفارش‌ها که اطلاعات مربوط به پرداخت و وضعیت سفارش را ذخیره می‌کند
class Order(models.Model):
    STATUS_ORDER = [
        ('Pending', 'در انتظار پرداخت'),  # وضعیت اولیه سفارش
        ('Processing', 'در حال پردازش'),  # در حال آماده‌سازی
        ('Shipped', 'ارسال شده به پست'),  # ارسال شده
        ('Delivered', 'تحویل داده شده'),  # تحویل نهایی به مشتری
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ارتباط با کاربر
    full_name = models.CharField(max_length=250)  # نام کامل مشتری
    email = models.CharField(max_length=300)  # ایمیل مشتری
    shipping_address = models.TextField(max_length=150000)  # آدرس ارسال سفارش
    mount_paid = models.DecimalField(decimal_places=0, max_digits=12)  # مبلغ پرداخت‌شده
    date_ordered = jmodels.jDateTimeField(auto_now_add=True)  # تاریخ ثبت سفارش (شمسی)
    status = models.CharField(max_length=50, choices=STATUS_ORDER, default='Pending')  # وضعیت سفارش
    last_update = jmodels.jDateTimeField(auto_now=True)  # آخرین بروزرسانی (شمسی)

    def save(self, *args, **kwargs):
        # بررسی تغییر وضعیت سفارش و بروزرسانی زمان آخرین تغییر
        if self.pk:
            old_status = Order.objects.get(id=self.pk).status
            if old_status != self.status:
                self.last_update = jdatetime.datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order - {str(self.id)}'  # نمایش شناسه سفارش در خروجی

# مدل مربوط به آیتم‌های داخل هر سفارش که مشخص می‌کند چه محصولی با چه تعداد سفارش داده شده است
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)  # ارتباط با سفارش
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)  # ارتباط با محصول
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # ارتباط با کاربر (اختیاری)
    quantity = models.PositiveBigIntegerField(default=1)  # تعداد محصول در سفارش
    price = models.DecimalField(decimal_places=0, max_digits=12)  # قیمت نهایی آن آیتم

    def __str__(self):
        # نمایش شناسه آیتم سفارش به همراه نام کاربر (در صورت وجود)
        if self.user is not None:
            return f'Order Item - {str(self.id)} - for {self.user}'
        else:
            return f'Order Item - {str(self.id)}'
