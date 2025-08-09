# مربوط به عملیات‌های مربوط به کاربران URL تعریف مسیرهای
# این قسمت شامل مسیرهایی برای ورود، خروج، ثبت‌نام، ورود با شماره تلفن، تأیید کد، و به‌روزرسانی اطلاعات کاربران است

from django.urls import path
from . import views

urlpatterns = [
    # مسیر ورود کاربران به سیستم
    path('login/', views.login_user, name="login"),

    # مسیر خروج کاربران از سیستم
    path('logout/', views.logout_user, name="logout"),

    # مسیر ثبت‌نام کاربران جدید
    path('login/signup/', views.signup_user, name="signup"),

    # مسیر ورود کاربران با استفاده از شماره تلفن
    path('login/login_phone/', views.login_phone_user, name='login_phone'),

    # مسیر برای تأیید کد ارسال‌شده به کاربر (مانند کد احراز هویت)
    path('verify_code/', views.verify_code, name='verify_code'),

    # مسیر به‌روزرسانی اطلاعات اصلی کاربر (مانند نام، ایمیل و ...)
    path('update_user/', views.update_user, name="update_user"),

    # مسیر به‌روزرسانی اطلاعات اضافی کاربر (مانند آدرس، شماره تلفن و ...)
    path('update_info/', views.update_info, name="update_info"),

    # مسیر برای ارسال فرم‌های به‌روزرسانی اطلاعات
    path('update_send/', views.update_send, name="update_send"),

    # مسیر به‌روزرسانی رمز عبور کاربران
    path('update_password/', views.update_password, name="update_password"),
]
