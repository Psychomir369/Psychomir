# وارد کردن توابع مورد نیاز برای تعریف مسیرها و ویوها
from django.urls import path
from . import views

# لیست مسیرهای اپلیکیشن فروشگاه که به توابع موجود در views متصل می‌شوند
urlpatterns = [
    path('', views.home, name="home"),  # صفحه اصلی فروشگاه

    path('about/', views.about, name="about"),  # صفحه درباره ما

    path('product/<int:pk>', views.product, name="product"),  # نمایش جزئیات یک محصول خاص با شناسه عددی

    path('category/<str:cat>', views.category, name="category"),  # نمایش محصولات مربوط به یک دسته خاص

    path('category/', views.category_summary, name="category_summary"),  # نمایش خلاصه‌ای از تمام دسته‌بندی‌ها

    path('search/', views.search, name="search"),  # جستجو در محصولات فروشگاه

    path('orders/', views.user_orders, name="orders"),  # نمایش لیست سفارش‌های کاربر لاگین کرده

    path('order_details/<int:pk>', views.order_details, name="order_details"),  # نمایش جزئیات یک سفارش خاص با شناسه
]
