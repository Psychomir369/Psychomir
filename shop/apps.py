# ایمپورت کلاس پایه برای پیکربندی اپلیکیشن
from django.apps import AppConfig

# تعریف کلاس پیکربندی اپلیکیشن فروشگاه
class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # نوع پیش‌فرض فیلد کلید اصلی برای مدل‌ها
    name = 'shop'  # نام اپلیکیشن که با پوشه اپلیکیشن باید هم‌خوان باشد
