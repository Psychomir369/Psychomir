# کتابخانه‌های مورد نیاز برای کار با مسیر فایل‌ها
from pathlib import Path
import os
import dj_database_url

# تعیین مسیر پایه پروژه برای استفاده در مسیرهای دیگر
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید امنیتی برای رمزگذاری (در محیط تولید باید مخفی نگه داشته شود)
SECRET_KEY = 'django-insecure-2!sbs)uvf4ag3feegm6-gwofgkxhxi)oe*=#^f6uej37byk1l*'

# (باشد False فعال یا غیرفعال کردن حالت اشکال‌زدایی (در محیط تولید باید
DEBUG = True

# لیست دامنه‌هایی که اجازه دسترسی به پروژه را دارند
ALLOWED_HOSTS = ['https://psychomir.onrender.com']

# لیست اپلیکیشن‌های فعال در پروژه
INSTALLED_APPS = [
    'django.contrib.admin',  # پنل مدیریت
    'django.contrib.auth',  # مدیریت کاربران و احراز هویت
    'django.contrib.contenttypes',  # مدیریت نوع محتوای مدل‌ها
    'django.contrib.sessions',  # مدیریت سشن‌ها برای کاربران
    'django.contrib.messages',  # نمایش پیام‌های سیستمی
    'django.contrib.staticfiles',  # مدیریت فایل‌های استاتیک (CSS, JS و ...)
    'django.contrib.humanize',  # قالب‌بندی داده‌ها مانند اعداد خواناتر
    'shop',      # اپلیکیشن فروشگاه
    'cart',      # اپلیکیشن سبد خرید
    'payment',   # اپلیکیشن پرداخت
    'account',   # اپلیکیشن حساب کاربری
]

# لیست میان‌افزارهایی که در چرخه پردازش درخواست‌ها نقش دارند
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # امنیت پایه
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # فعال‌سازی سشن‌ها
    'django.middleware.common.CommonMiddleware',  # پردازش عمومی درخواست‌ها
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF جلوگیری از حملات
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # مدیریت لاگین و دسترسی‌ها
    'django.contrib.messages.middleware.MessageMiddleware',  # مدیریت پیام‌های موقت
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # جلوگیری از حملات کلیک‌جکینگ
]

# ماژولی که URLهای اصلی پروژه را نگه می‌دارد
ROOT_URLCONF = 'Shop_Site.urls'

# تنظیمات مربوط به قالب‌ها (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # استفاده از موتور قالب پیش‌فرض جنگو
        'DIRS': [],  # اگر مسیر خاصی برای قالب‌ها دارید، اینجا تعریف می‌شود
        'APP_DIRS': True,  # فعال‌سازی استفاده از قالب‌های موجود در هر اپلیکیشن
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # اطلاعات اشکال‌زدایی در قالب‌ها
                'django.template.context_processors.request',  # در قالب request دسترسی به
                'django.contrib.auth.context_processors.auth',  # وضعیت احراز هویت کاربر
                'django.contrib.messages.context_processors.messages',  # پیام‌های سیستمی
                'cart.context_processors.cart',  # اضافه کردن اطلاعات سبد خرید به قالب‌ها
            ],
        },
    },
]

# برای اجرا روی سرور WSGI مسیر فایل
WSGI_APPLICATION = 'Shop_Site.wsgi.application'

'''
# برای توسعه اولیه (SQLite تنظیمات پایگاه داده (پیش‌فرض
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}

# قوانین اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # شباهت با اطلاعات کاربر
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # حداقل طول رمز عبور
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # جلوگیری از رمزهای رایج
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # جلوگیری از رمزهای کاملاً عددی
    },
]

# تنظیمات زبان و منطقه زمانی
LANGUAGE_CODE = 'en-us'  # زبان پیش‌فرض انگلیسی
TIME_ZONE = 'Asia/Tehran'  # منطقه زمانی ایران
USE_I18N = True  # فعال‌سازی ترجمه بین‌المللی
USE_TZ = True  # استفاده از زمان محلی

# و رسانه‌ای (مثل تصاویر آپلودی) (CSS, JS تنظیم مسیرهای فایل‌های استاتیک (مثل
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # مسیر تجمیع فایل‌های استاتیک برای دیپلوی

STATICFILES_DIRS = [BASE_DIR / 'static']  # مسیر پوشه استاتیک در توسعه
STATICFILES_URLS = ['static/']

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # مسیر ذخیره فایل‌های آپلود شده توسط کاربران

if not DEBUG:

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# تعیین نوع فیلد پیش‌فرض برای کلید اصلی مدل‌ها
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
