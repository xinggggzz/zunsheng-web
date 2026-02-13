from django.contrib import admin
from .models import (
    HeroSlide, CompanyInfo, NewsCategory, News,
    ProductCategory, Product, Certificate, CustomerMessage,
    TechnicalEquipment, CompanyEnvironment
)

admin.site.site_header = "遵盛汽车零部件后台管理系统"
admin.site.site_title = "遵盛汽配管理后台"
admin.site.index_title = "欢迎使用遵盛汽车零部件官方网站管理系统"


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'short_name', 'slogan', 'description', 'image')
        }),
        ('关于页面配置', {
            'fields': ('about_banner', 'about_slogan_cn', 'about_slogan_en'),
            'description': '在此上传关于页面的Banner图和修改标语文字'
        }),
        ('新闻页面配置', {
            'fields': ('news_banner', 'news_slogan_cn', 'news_slogan_en'),
            'description': '在此上传新闻页面的Banner图和修改标语文字'
        }),
        ('产品页面配置', {
            'fields': ('product_banner', 'product_slogan_cn', 'product_slogan_en'),
            'description': '在此上传产品页面的Banner图和修改标语文字'
        }),
        ('服务页面配置', {
            'fields': ('service_banner', 'service_slogan_cn', 'service_slogan_en'),
            'description': '在此上传客户服务页面的Banner图和修改标语文字'
        }),
        ('联系页面配置', {
            'fields': ('contact_banner', 'contact_slogan_cn', 'contact_slogan_en'),
            'description': '在此上传联系我们页面的Banner图和修改标语文字'
        }),
        ('联系方式', {
            'fields': ('phone', 'email', 'address', 'postcode', 'pdf_catalog', 'wechat_qr')
        }),
    )

    def has_add_permission(self, request):
        # 如果已经有数据了，就不允许再添加
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'is_active']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'summary']
    list_editable = ['is_active']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order', 'is_active', 'image_tag']
    list_filter = ['is_active', 'category']
    search_fields = ['name']
    list_editable = ['order', 'is_active']
    
    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)
        return "-"
    image_tag.short_description = '预览'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(TechnicalEquipment)
class TechnicalEquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(CompanyEnvironment)
class CompanyEnvironmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'company', 'created_at', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'phone', 'company', 'message', 'created_at']
