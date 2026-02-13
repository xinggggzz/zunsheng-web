from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import (
    HeroSlide, CompanyInfo, News, NewsCategory, Product,
    ProductCategory, Certificate, CustomerMessage,
    TechnicalEquipment, CompanyEnvironment
)


def index(request):
    """首页"""
    slides = HeroSlide.objects.filter(is_active=True)
    company = CompanyInfo.objects.first()
    news_list = News.objects.filter(is_active=True)[:3]
    products = Product.objects.filter(is_active=True)[:6]
    context = {
        'hero_slides': slides,
        'company': company,
        'news_list': news_list,
        'products': products,
    }
    return render(request, 'website/index.html', context)


def about(request):
    """关于遵盛 - 公司简介"""
    company = CompanyInfo.objects.first()
    certificates = Certificate.objects.all()
    context = {
        'company': company,
        'certificates': certificates,
        'slogan_cn': company.about_slogan_cn if company and company.about_slogan_cn else "造一流汽配产品，铸遵盛顶级品牌",
        'slogan_en': company.about_slogan_en if company and company.about_slogan_en else "MAKE FIRST-CLASS AUTO PARTS, CAST ZUNSHENG TOP BRAND",
    }
    return render(request, 'website/about.html', context)


def technical_equipment(request):
    """技术设备"""
    company = CompanyInfo.objects.first()
    equipment = TechnicalEquipment.objects.all()
    context = {
        'company': company,
        'equipment': equipment,
        'slogan_cn': company.about_slogan_cn if company and company.about_slogan_cn else "先进设备保障卓越品质",
        'slogan_en': company.about_slogan_en if company and company.about_slogan_en else "ADVANCED EQUIPMENT ENSURES EXCELLENT QUALITY",
    }
    return render(request, 'website/equipment.html', context)


def company_environment(request):
    """公司环境"""
    company = CompanyInfo.objects.first()
    environment = CompanyEnvironment.objects.all()
    context = {
        'company': company,
        'environment': environment,
        'slogan_cn': company.about_slogan_cn if company and company.about_slogan_cn else "优美环境凝聚团队力量",
        'slogan_en': company.about_slogan_en if company and company.about_slogan_en else "BEAUTIFUL ENVIRONMENT COHESIVE TEAM STRENGTH",
    }
    return render(request, 'website/environment.html', context)


def service_philosophy(request):
    """服务理念"""
    company = CompanyInfo.objects.first()
    context = {
        'company': company,
        'slogan_cn': company.service_slogan_cn if company and company.service_slogan_cn else "你的需求，我们的追求，遵盛汽配",
        'slogan_en': company.service_slogan_en if company and company.service_slogan_en else "YOUR NEEDS, OUR PURSUIT, ZUNSHENG AUTO PARTS",
    }
    return render(request, 'website/service_philosophy.html', context)


def news_list(request):
    """新闻列表"""
    category_id = request.GET.get('category')
    keyword = request.GET.get('keyword')
    
    news_qs = News.objects.filter(is_active=True)
    
    if category_id:
        news_qs = news_qs.filter(category_id=category_id)
    if keyword:
        from django.db.models import Q
        news_qs = news_qs.filter(
            Q(title__icontains=keyword) | 
            Q(summary__icontains=keyword) | 
            Q(content__icontains=keyword)
        )
        
    paginator = Paginator(news_qs, 10) # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = NewsCategory.objects.all()
    company = CompanyInfo.objects.first()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': int(category_id) if category_id else None,
        'company': company,
        'slogan_cn': company.news_slogan_cn if company and company.news_slogan_cn else "互补、团结和谐并为负有共同责任",
        'slogan_en': company.news_slogan_en if company and company.news_slogan_en else "TO COMPLEMENT EACH OTHER, UNITY AND HARMONY AND BEAR THE COMMON RESPONSIBILITY",
    }
    return render(request, 'website/news_list.html', context)


def news_detail(request, pk):
    """新闻详情"""
    news = get_object_or_404(News, pk=pk, is_active=True)
    # Get previous and next news
    try:
        prev_news = News.objects.filter(is_active=True, created_at__lt=news.created_at).order_by('-created_at').first()
    except News.DoesNotExist:
        prev_news = None
        
    try:
        next_news = News.objects.filter(is_active=True, created_at__gt=news.created_at).order_by('created_at').first()
    except News.DoesNotExist:
        next_news = None
        
    context = {
        'news': news,
        'prev_news': prev_news,
        'next_news': next_news,
    }
    return render(request, 'website/news_detail.html', context)


def product_list(request):
    """产品列表"""
    category_id = request.GET.get('category')
    
    product_qs = Product.objects.filter(is_active=True)
    keyword = request.GET.get('keyword')
    
    if category_id:
        product_qs = product_qs.filter(category_id=category_id)
    if keyword:
        from django.db.models import Q
        product_qs = product_qs.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword)
        )
        
    paginator = Paginator(product_qs, 12) # 12 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = ProductCategory.objects.all()
    company = CompanyInfo.objects.first()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': int(category_id) if category_id else None,
        'company': company,
        'slogan_cn': company.product_slogan_cn if company and company.product_slogan_cn else "注重产品质量，降低生产成本",
        'slogan_en': company.product_slogan_en if company and company.product_slogan_en else "FOCUS ON PRODUCT QUALITY AND REDUCE PRODUCTION COSTS",
    }
    return render(request, 'website/product_list.html', context)


def product_detail(request, pk):
    """产品详情"""
    product = get_object_or_404(Product, pk=pk, is_active=True)
    categories = ProductCategory.objects.all()
    
    # 获取上一件和下一件产品
    try:
        prev_product = Product.objects.filter(is_active=True, order__lt=product.order).order_by('-order').first()
        if not prev_product:
            prev_product = Product.objects.filter(is_active=True, pk__lt=product.pk).order_by('-pk').first()
    except Product.DoesNotExist:
        prev_product = None
        
    try:
        next_product = Product.objects.filter(is_active=True, order__gt=product.order).order_by('order').first()
        if not next_product:
            next_product = Product.objects.filter(is_active=True, pk__gt=product.pk).order_by('pk').first()
    except Product.DoesNotExist:
        next_product = None

    context = {
        'product': product,
        'categories': categories,
        'prev_product': prev_product,
        'next_product': next_product,
    }
    return render(request, 'website/product_detail.html', context)


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def contact(request):
    """联系我们"""
    company = CompanyInfo.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_name = request.POST.get('company')
        content = request.POST.get('message')
        
        if name and content:
            # 1. 保存到数据库
            msg_obj = CustomerMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                company=company_name,
                message=content
            )
            
            # 2. 发送顶级视觉效果邮件通知 (Apple/Google 高级简约风格)
            try:
                subject = f'询盘通知：{name} 发送了新消息'
                recipient_list = getattr(settings, 'ADMIN_EMAILS', ['1987205417@qq.com'])
                
                # 构建 HTML 内容 (超高级扁平化设计)
                html_message = f"""
                <div style="background-color: #f0f2f5; padding: 60px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); overflow: hidden; border: 1px solid #eef0f2;">
                        <tr>
                            <td style="padding: 40px 40px 30px; text-align: left;">
                                <div style="display: inline-block; padding: 8px 16px; background: #e8f0fe; border-radius: 50px; color: #003399; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px;">
                                    NEW INQUIRY
                                </div>
                                <h1 style="color: #1d1d1f; font-size: 28px; font-weight: 700; margin: 0; line-height: 1.2;">
                                    收到来自官网的咨询
                                </h1>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 0 40px;">
                                <div style="height: 1px; background: #f2f2f2; width: 100%;"></div>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 40px;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 25px;">
                                            <p style="margin: 0 0 5px 0; font-size: 12px; color: #86868b; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;">客户基本资料</p>
                                            <p style="margin: 0; font-size: 18px; color: #1d1d1f; font-weight: 500;">{name}</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding-bottom: 25px;">
                                            <p style="margin: 0 0 5px 0; font-size: 12px; color: #86868b; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;">联系通道</p>
                                            <p style="margin: 0; font-size: 16px; color: #1d1d1f; font-weight: 400;">
                                                <span style="color: #003399; font-weight: 600;">公司:</span> {company_name if company_name else '未填写'} <br>
                                                <span style="color: #003399; font-weight: 600;">电话:</span> {phone if phone else '未留电话'} <br>
                                                <span style="color: #003399; font-weight: 600;">邮箱:</span> {email if email else '未留邮箱'}
                                            </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="background-color: #f9f9fb; border-radius: 12px; padding: 25px;">
                                            <p style="margin: 0 0 10px 0; font-size: 12px; color: #86868b; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;">具体需求描述</p>
                                            <div style="font-size: 16px; color: #333336; line-height: 1.7; font-style: italic;">
                                                “{content}”
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 0 40px 40px; text-align: center;">
                                <a href="{request.build_absolute_uri('/admin/website/customermessage/')}" style="display: inline-block; background: #003399; color: #ffffff; padding: 18px 40px; border-radius: 12px; font-weight: 600; font-size: 16px; text-decoration: none; box-shadow: 0 8px 16px rgba(0, 51, 153, 0.25);">
                                    立即处理咨询
                                </a>
                                <p style="margin: 20px 0 0 0; font-size: 13px; color: #86868b;">
                                    点击按钮直接登录遵盛管理后台
                                </p>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding: 30px 40px; background-color: #fafafa; border-top: 1px solid #f2f2f2; text-align: center;">
                                <p style="margin: 0; font-size: 12px; color: #bfbfbf; line-height: 1.5;">
                                    这是由遵盛汽车零部件官网系统自动发出的通知邮件。<br>
                                    发件账户：{settings.EMAIL_HOST_USER} &nbsp; | &nbsp; 目的账户：{', '.join(recipient_list)}
                                </p>
                            </td>
                        </tr>
                    </table>
                </div>
                """
                plain_message = strip_tags(html_message)
                
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list,
                    html_message=html_message,
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f"Failed to send email: {str(e)}")
            
            messages.success(request, '您的留言已提交，我们会尽快联系您！')
            return redirect('website:contact')
        else:
            messages.error(request, '请填写姓名和留言内容。')
            
    context = {
        'company': company,
        'slogan_cn': company.contact_slogan_cn if company and company.contact_slogan_cn else "你的关注是我的动力，遵盛竭诚为你服务",
        'slogan_en': company.contact_slogan_en if company and company.contact_slogan_en else "YOUR ATTENTION IS OUR MOTIVATION, ZUNSHENG IS AT YOUR SERVICE",
    }
    return render(request, 'website/contact.html', context)
