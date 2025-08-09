# برای ساخت فرم سفارشی آدرس ارسال ShippingAddress ایمپورت کلاس فرم‌ها و مدل
from django import forms
from .models import ShippingAddress

# تعریف فرم مدل‌محور برای دریافت اطلاعات آدرس ارسال از کاربر
class ShippingForm(forms.ModelForm):
    # تعریف فیلد نام و نام خانوادگی با ظاهر سفارشی و اجباری
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}),
        required=True,
    )
    # دلخواه CSS و کلاس placeholder تعریف فیلد ایمیل با
    shipping_email = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}), 
        required=True,  
    )
    # تعریف فیلد شماره تماس با استایل‌دهی و الزامی بودن
    shipping_phone = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),  
        required=True,  
    )
    # تعریف فیلد آدرس با قابلیت پر شدن توسط کاربر
    shipping_address = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس'}),  
        required=True,  
    )
    # تعریف فیلد شهر برای مشخص‌کردن مقصد ارسال
    shipping_city = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),  
        required=True, 
    )
    # فیلد اختیاری برای منطقه یا استان
    shipping_state = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'}), 
        required=False, 
    )
    # فیلد کد پستی با استایل‌دهی سفارشی
    shipping_zipcode = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}), 
        required=True, 
    )

    # و مشخص کردن فیلدهای قابل استفاده ShippingAddress تنظیمات فرم برای اتصال به مدل
    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name', 'shipping_email', 'shipping_phone',
            'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_address',
        ]
        exclude = ['user',]  # فیلد کاربر از فرم حذف شده و در پس‌زمینه مدیریت می‌شود

