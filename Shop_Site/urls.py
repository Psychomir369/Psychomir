# ایمپورت ماژول‌های مورد نیاز برای تعریف مسیرها و تنظیمات رسانه‌ای
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.conf import settings

# تعریف مسیرهای اصلی پروژه که به اپلیکیشن‌های مختلف متصل می‌شوند
urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پنل مدیریت جنگو
    path('', include('shop.urls')),  # مسیر پیش‌فرض به اپلیکیشن فروشگاه متصل می‌شود
    path('cart/', include('cart.urls')),  # مسیر سبد خرید
    path('payment/', include('payment.urls')),  # مسیر پرداخت
    path('account/', include('account.urls')),  # مسیر مربوط به حساب کاربری
]

# در حالت توسعه (DEBUG=True)، مسیرهای مربوط به فایل‌های رسانه‌ای مانند عکس‌ها و فایل‌های آپلود شده فعال می‌شوند
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
