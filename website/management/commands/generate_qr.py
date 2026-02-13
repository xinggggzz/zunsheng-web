import os
import qrcode
from io import BytesIO
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files.base import ContentFile
from website.models import CompanyInfo

class Command(BaseCommand):
    help = 'Generate QR code for the company catalog'

    def handle(self, *args, **options):
        company = CompanyInfo.objects.first()
        if not company:
            self.stdout.write(self.style.ERROR("Error: No CompanyInfo found."))
            return

        # You would replace this with your ACTUAL public URL
        # For now, using a placeholder URL pointing to the catalog file
        catalog_url = "http://localhost:8000/media/company/catalog.pdf" # Placeholder
        
        # If company has a catalog file, we could potentially use its url if it was hosted properly
        # if company.pdf_catalog:
        #    catalog_url = company.pdf_catalog.url
        
        self.stdout.write(f"Generating QR code for: {catalog_url}")
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(catalog_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image to BytesIO
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        
        # Save to the static directory specifically
        qr_filename = "catalog_qr.png"
        static_images_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
        
        if not os.path.exists(static_images_dir):
            os.makedirs(static_images_dir)
        
        img_path = os.path.join(static_images_dir, qr_filename)
        with open(img_path, 'wb') as f:
            f.write(buffer.getvalue())
        
        self.stdout.write(self.style.SUCCESS(f"Catalog QR code generated and saved to: {img_path}"))
