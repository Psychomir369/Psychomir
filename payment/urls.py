# ایمپورت‌های مورد نیاز برای تعریف مسیرها
from django.urls import path
from . import views

# تعریف مسیرهای مربوط به پرداخت و تسویه‌حساب
urlpatterns = [
    # مسیر برای نمایش موفقیت‌آمیز بودن پرداخت
    path('payment_success/', views.payment_success, name="payment_success"),

    # مسیر برای نمایش فرم تسویه‌حساب
    path('checkout/', views.checkout, name="checkout"),

    # مسیر برای تأیید نهایی سفارش (قبل از پرداخت)
    path('confirm_order/', views.confirm_order, name="confirm_order"),

    # مسیر برای پردازش نهایی سفارش و ثبت آن در سیستم
    path('process_order/', views.process_order, name="process_order"),
]
