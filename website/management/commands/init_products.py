from django.core.management.base import BaseCommand
from website.models import Product, ProductCategory

class Command(BaseCommand):
    help = 'Initialize product categories and sample products'

    def handle(self, *args, **options):
        # Clear old data
        self.stdout.write('Clearing old product data...')
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        # Create Categories
        self.stdout.write('Creating categories...')
        c1 = ProductCategory.objects.create(name='紧固件/螺丝', order=1)
        c2 = ProductCategory.objects.create(name='螺母系列', order=2)
        c3 = ProductCategory.objects.create(name='垫圈/垫片', order=3)
        c4 = ProductCategory.objects.create(name='定制非标件', order=4)

        # Creates Sample Products
        products_data = [
            ('高强度六角螺栓', c1),
            ('不锈钢自攻螺丝', c1),
            ('内六角螺钉', c1),
            ('防松螺母 M10', c2),
            ('法兰螺母', c2),
            ('蝶形螺母', c2),
            ('平垫圈', c3),
            ('弹簧垫圈', c3),
            ('波形垫圈', c3),
            ('特制加长螺栓', c4),
            ('异形螺母', c4),
            ('精密定位销', c4),
        ]

        self.stdout.write('Creating products...')
        for name, category in products_data:
            Product.objects.create(name=name, category=category, is_active=True)

        self.stdout.write(self.style.SUCCESS('Successfully initialized products!'))
        self.stdout.write(f'Categories: {ProductCategory.objects.count()}')
        self.stdout.write(f'Products: {Product.objects.count()}')
