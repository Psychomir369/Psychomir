# استفاده شده است URL برای مدیریت مسیرهای django.urls از 
# ما نیز برای تعریف عملکردهای مربوط به هر مسیر ایمپورت شده است views فایل 
from django.urls import path
from . import views

# را مشخص می‌کند (cart) این بخش تمامی URL‌ های مرتبط با سبد خرید (urlpatterns) تعریف لیستی از مسیرها 
urlpatterns = [
    # مسیر اصلی: صفحه خلاصه سبد خرید
    path('', views.cart_summary, name="cart_summary"),
    
    # مسیر اضافه کردن آیتم به سبد خرید
    path('add/', views.cart_add, name="cart_add"),
    
    # مسیر به‌روزرسانی آیتم‌های سبد خرید
    path('update/', views.cart_update, name="cart_update"),
    
    # مسیر حذف آیتم از سبد خرید
    path('delete/', views.cart_delete, name="cart_delete"),
]
