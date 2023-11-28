import os
import django
from django.utils import timezone
from django.core.management.base import BaseCommand

from web.models import Mobile, MobileImage

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mobillo.settings")

django.setup()

def create_mobile_with_images():
    for i in range(10):
        mobile = Mobile.objects.create(
            name=f"Mobile {i+1}",
            slug=f"mobile-{i+1}",
            description=f"This is the description for Mobile {i+1}",
            price=1000.00 + (i * 100),
            main_image=f"res/image/products/mobile_{i+1}.jpg"  # Adjust image paths as needed
        )

        # Create images for each mobile
        for j in range(3):  # Create 3 images for each mobile
            MobileImage.objects.create(
                product=mobile,
                image=f"res/image/products/mobile_{i+1}_image_{j+1}.jpg",  # Adjust image paths
                date_created=timezone.now()
            )

if __name__ == "__main__":
    create_mobile_with_images()


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        create_mobile_with_images()
        self.stdout.write("10 rows inserted successfully.")


