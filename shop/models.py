# ایمپورت‌های مورد نیاز برای تعریف مدل‌ها و اعتبارسنجی داده‌ها
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

# مدل دسته‌بندی برای گروه‌بندی محصولات فروشگاه
class Category(models.Model):
    name = models.CharField(max_length=20)  # نام دسته‌بندی (مثلاً: موبایل، پوشاک و ...)

    def __str__(self):
        return self.name

# مدل پروفایل برای افزودن اطلاعات تکمیلی به کاربر (آدرس، شماره تلفن و ...)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User ارتباط یک‌به‌یک با مدل
    date_modified = models.DateTimeField(User, auto_now=True)  # زمان آخرین تغییر اطلاعات پروفایل
    phone = models.CharField(max_length=20, blank=True)  # شماره تلفن کاربر
    address = models.CharField(max_length=250, blank=True)  # آدرس کامل کاربر
    city = models.CharField(max_length=25, blank=True)  # شهر محل سکونت
    state = models.CharField(max_length=25, blank=True)  # استان یا ایالت
    zipcode = models.CharField(max_length=25, blank=True)  # کد پستی
    country = models.CharField(max_length=25, default='IRAN')  # کشور (پیش‌فرض ایران)
    old_cart = models.CharField(max_length=200, blank=True, null=True)  # ذخیره اطلاعات سبد خرید قبلی (اختیاری)

    def __str__(self):
        return self.user.username

# سیگنال برای ایجاد خودکار پروفایل بعد از ساختن یک کاربر جدید
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# User اتصال سیگنال به مدل
post_save.connect(create_profile, sender=User)

# مدل محصول برای تعریف مشخصات هر کالای موجود در فروشگاه
class Product(models.Model):
    name = models.CharField(max_length=40)  # نام محصول
    description = models.CharField(max_length=500, default='', blank=True, null=True)  # توضیحات محصول
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)  # قیمت محصول
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # دسته‌بندی مربوطه
    picture = models.ImageField(upload_to='upload/product/')  # تصویر محصول
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  # تعداد ستاره‌ها (امتیاز از 0 تا 5)
    is_sale = models.BooleanField(default=False)  # آیا محصول در حراج قرار دارد؟
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)  # قیمت حراجی (در صورت فعال بودن)

    def __str__(self):
        return self.name

# مدل سفارش برای ثبت خریدهای کاربران
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # محصول خریداری‌شده
    quantity = models.IntegerField(default=1)  # تعداد سفارش‌شده
    address = models.CharField(max_length=400, default='', blank=True)  # آدرس تحویل سفارش
    phone = models.CharField(max_length=20, blank=True)  # شماره تماس
    date = models.DateTimeField(default=timezone.now)  # تاریخ سفارش
    status = models.BooleanField(default=False)  # وضعیت سفارش (تحویل شده یا نه)

    def __str__(self):
        return self.product.name
