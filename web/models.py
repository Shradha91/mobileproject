from django.db import models
from django.urls import reverse
from django.utils import timezone

class ContactMessage(models.Model):
    """
    Used for Contact Us responses
    """
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

class Mobile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()
    main_image = models.ImageField(
        upload_to="res/image/products", verbose_name="Main Image"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mobile_detail", args=[self.slug])

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "mobile"
        verbose_name_plural = "mobiles"

class MobileImage(models.Model):
    # many image for one mobile
    product = models.ForeignKey(
        Mobile, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="res/image/products")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)
        verbose_name = "mobile image"
        verbose_name_plural = "mobile images"

