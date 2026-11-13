from django.db import models


class Property(models.Model):

    CATEGORY_CHOICES = [
        ('rent', 'Rent'),
        ('sale', 'Sale'),
        ('commercial', 'Commercial'),
        ('plot', 'Plots / Land'),
        ('interior', 'Interior Design'),
    ]

    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ]

    # Property information
    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    location = models.CharField(max_length=250)

    description = models.TextField()

    # Price and area
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    area_sqft = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    bedrooms = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    bathrooms = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    # Property photograph
    cover_image = models.ImageField(
        upload_to='properties/',
        null=True,
        blank=True
    )

    # Availability and publishing
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='available'
    )

    is_featured = models.BooleanField(default=False)

    is_published = models.BooleanField(default=False)

    # Automatic timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title

class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='properties/gallery/'
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['uploaded_at']

    def __str__(self):
        return f"Image for {self.property.title}"