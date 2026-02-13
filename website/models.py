from django.db import models


class HeroSlide(models.Model):
    """首页轮播图"""
    title = models.CharField('标题', max_length=100, blank=True)
    title_en = models.CharField('标题(英)', max_length=100, blank=True)
    subtitle = models.CharField('副标题', max_length=200, blank=True)
    subtitle_en = models.CharField('副标题(英)', max_length=200, blank=True)
    image = models.ImageField('图片', upload_to='hero/')
    order = models.IntegerField('排序', default=0)
    is_active = models.BooleanField('是否启用', default=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图管理'
        ordering = ['order']

    def __str__(self):
        return self.title or f'轮播图 #{self.pk}'


class CompanyInfo(models.Model):
    """公司信息（单例）"""
    name = models.CharField('公司名称', max_length=100, default='遵盛汽车零部件有限公司')
    short_name = models.CharField('简称', max_length=20, default='遵盛')
    slogan = models.CharField('首页标语', max_length=200, blank=True)
    about_banner = models.ImageField('关于页面Banner', upload_to='company/', blank=True, help_text='如果不上传，将显示默认颜色背景')
    about_slogan_cn = models.CharField('关于页面标语(中)', max_length=200, default='造一流汽配产品，铸遵盛顶级品牌')
    about_slogan_en = models.CharField('关于页面标语(英)', max_length=200, default='MAKE FIRST-CLASS AUTO PARTS, CAST ZUNSHENG TOP BRAND')
    news_banner = models.ImageField('新闻页面Banner', upload_to='company/', blank=True)
    news_slogan_cn = models.CharField('新闻页面标语(中)', max_length=200, default='互补、团结和谐并为负有共同责任')
    news_slogan_en = models.CharField('新闻页面标语(英)', max_length=200, default='TO COMPLEMENT EACH OTHER, UNITY AND HARMONY AND BEAR THE COMMON RESPONSIBILITY')
    product_banner = models.ImageField('产品页面Banner', upload_to='company/', blank=True)
    product_slogan_cn = models.CharField('产品页面标语(中)', max_length=200, default='注重产品质量，降低生产成本')
    product_slogan_en = models.CharField('产品页面标语(英)', max_length=200, default='FOCUS ON PRODUCT QUALITY AND REDUCE PRODUCTION COSTS')
    service_banner = models.ImageField('服务页面Banner', upload_to='company/', blank=True)
    service_slogan_cn = models.CharField('服务页面标语(中)', max_length=200, default='你的需求，我们的追求，遵盛汽配')
    service_slogan_en = models.CharField('服务页面标语(英)', max_length=200, default='YOUR NEEDS, OUR PURSUIT, ZUNSHENG AUTO PARTS')
    contact_banner = models.ImageField('联系页面Banner', upload_to='company/', blank=True)
    contact_slogan_cn = models.CharField('联系页面标语(中)', max_length=200, default='你的关注是我的动力，遵盛竭诚为你服务')
    contact_slogan_en = models.CharField('联系页面标语(英)', max_length=200, default='YOUR ATTENTION IS OUR MOTIVATION, ZUNSHENG IS AT YOUR SERVICE')
    description = models.TextField('公司简介')
    description_en = models.TextField('公司简介(英)', blank=True)
    image = models.ImageField('公司图片', upload_to='company/', blank=True)
    phone = models.CharField('电话', max_length=30, blank=True)
    email = models.EmailField('邮箱', blank=True)
    address = models.CharField('地址', max_length=200, blank=True)
    address_en = models.CharField('地址(英)', max_length=200, blank=True)
    postcode = models.CharField('邮编', max_length=10, blank=True)
    pdf_catalog = models.FileField('电子图册(PDF)', upload_to='company/', blank=True, null=True)
    wechat_qr = models.ImageField('微信二维码', upload_to='company/', blank=True, null=True)

    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = '公司信息'

    def __str__(self):
        return self.name


class NewsCategory(models.Model):
    """新闻分类"""
    name = models.CharField('分类名称', max_length=50)
    name_en = models.CharField('分类名称(英)', max_length=50, blank=True)

    class Meta:
        verbose_name = '新闻分类'
        verbose_name_plural = '新闻分类'

    def __str__(self):
        return self.name


class News(models.Model):
    """新闻"""
    title = models.CharField('标题', max_length=200)
    title_en = models.CharField('标题(英)', max_length=200, blank=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    summary = models.CharField('摘要', max_length=300, blank=True)
    summary_en = models.CharField('摘要(英)', max_length=300, blank=True)
    content = models.TextField('内容')
    content_en = models.TextField('内容(英)', blank=True)
    cover = models.ImageField('封面图', upload_to='news/', blank=True)
    created_at = models.DateTimeField('发布时间', auto_now_add=True)
    is_active = models.BooleanField('是否发布', default=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻管理'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    """产品分类"""
    name = models.CharField('分类名称', max_length=50)
    name_en = models.CharField('分类名称(英)', max_length=50, blank=True)
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = '产品分类'
        ordering = ['order']

    def __str__(self):
        return self.name


class Product(models.Model):
    """产品"""
    name = models.CharField('产品名称/型号', max_length=100)
    name_en = models.CharField('产品名称/型号(英)', max_length=100, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    description = models.TextField('产品描述', blank=True)
    description_en = models.TextField('产品描述(英)', blank=True)
    image = models.ImageField('产品图片', upload_to='products/')
    order = models.IntegerField('排序', default=0)
    is_active = models.BooleanField('是否展示', default=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品管理'
        ordering = ['order']

    def __str__(self):
        return self.name


class Certificate(models.Model):
    """公司证书"""
    name = models.CharField('证书名称', max_length=100)
    name_en = models.CharField('证书名称(英)', max_length=100, blank=True)
    image = models.ImageField('证书图片', upload_to='certificates/')
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '证书'
        verbose_name_plural = '证书管理'
        ordering = ['order']

    def __str__(self):
        return self.name


class CustomerMessage(models.Model):
    """客户留言"""
    name = models.CharField('姓名', max_length=50)
    email = models.EmailField('邮箱', blank=True)
    phone = models.CharField('电话', max_length=30, blank=True)
    company = models.CharField('公司', max_length=100, blank=True)
    message = models.TextField('留言内容')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)
    is_read = models.BooleanField('已读', default=False)

    class Meta:
        verbose_name = '客户留言'
        verbose_name_plural = '客户留言'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%Y-%m-%d")}'


class TechnicalEquipment(models.Model):
    """技术设备"""
    name = models.CharField('设备名称', max_length=100)
    name_en = models.CharField('设备名称(英)', max_length=100, blank=True)
    image = models.ImageField('设备图片', upload_to='equipment/')
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '技术设备'
        verbose_name_plural = '技术设备管理'
        ordering = ['order']

    def __str__(self):
        return self.name


class CompanyEnvironment(models.Model):
    """公司环境"""
    name = models.CharField('环境名称', max_length=100)
    name_en = models.CharField('环境名称(英)', max_length=100, blank=True)
    image = models.ImageField('环境图片', upload_to='environment/')
    order = models.IntegerField('排序', default=0)

    class Meta:
        verbose_name = '公司环境'
        verbose_name_plural = '公司环境管理'
        ordering = ['order']

    def __str__(self):
        return self.name
