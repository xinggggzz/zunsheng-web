from django.core.management.base import BaseCommand
from website.models import CompanyInfo


class Command(BaseCommand):
    help = '初始化或更新公司信息'

    def handle(self, *args, **options):
        company, created = CompanyInfo.objects.get_or_create(
            id=1,
            defaults={
                'name': '遵盛汽车零部件有限公司',
                'short_name': '遵盛',
                'about_slogan_cn': '造一流汽配产品，铸遵盛顶级品牌',
                'about_slogan_en': 'MAKE FIRST-CLASS AUTO PARTS, CAST ZUNSHENG TOP BRAND',
                'description': '遵盛汽车零部件有限公司是一家专业的汽配企业。',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('成功创建公司信息'))
        else:
            # 更新现有记录，确保新字段有值
            if not company.about_slogan_cn:
                company.about_slogan_cn = '造一流汽配产品，铸遵盛顶级品牌'
            if not company.about_slogan_en:
                company.about_slogan_en = 'MAKE FIRST-CLASS AUTO PARTS, CAST ZUNSHENG TOP BRAND'
            company.save()
            self.stdout.write(self.style.SUCCESS('成功更新公司信息'))
        
        self.stdout.write(f'公司名称: {company.name}')
        self.stdout.write(f'中文标语: {company.about_slogan_cn}')
        self.stdout.write(f'英文标语: {company.about_slogan_en}')
