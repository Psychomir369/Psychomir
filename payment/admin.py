# ایمپورت‌های لازم برای ثبت مدل‌ها در پنل ادمین
from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

# در پنل مدیریت برای دسترسی از طریق رابط ادمین OrderItem و ShippingAddress ثبت مدل‌های
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)

# تعریف کلاس درون‌خطی برای نمایش آیتم‌های هر سفارش در داخل صفحه مدیریت سفارش
class OrderItemInLine(admin.TabularInline):
    model = OrderItem     # استفاده از مدل آیتم سفارش
    extra = 0             # عدم نمایش فیلد اضافی خالی در فرم

# به صورت سفارشی با تنظیمات مدیریتی خاص Order ثبت مدل
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered', 'last_update']  # فیلدهایی که فقط قابل مشاهده‌اند و قابل ویرایش نیستند
    inlines = [OrderItemInLine]  # نمایش لیست آیتم‌های مرتبط با هر سفارش در همان صفحه
