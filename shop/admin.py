# ایمپورت‌های لازم برای ثبت مدل‌ها در ادمین پنل و مدیریت کاربران
from django.contrib import admin
from . import models
from django.contrib.auth.models import User

# ثبت مدل‌های اصلی (دسته‌بندی، محصول، سفارش، پروفایل) در ادمین پنل
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Profile)

# در صفحه کاربر Profile برای نمایش و ویرایش مدل Inline تعریف یک کلاس
class ProfileInLine(admin.StackedInline):
    model = models.Profile  # مدل مرتبط
    can_delete = False  # جلوگیری از حذف پروفایل از همین‌جا (اختیاری)

# تعریف یک کلاس سفارشی برای نمایش کاربران همراه با پروفایلشان
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']  # فیلدهایی که نمایش داده می‌شوند
    inlines = [ProfileInLine]  # افزودن پروفایل به صورت درون‌خطی

# جایگزینی مدل پیش‌فرض کاربر با نسخه سفارشی‌شده
admin.site.unregister(User)  # User حذف ثبت اولیه مدل
admin.site.register(User, UserAdmin)  # ثبت نسخه سفارشی‌شده
