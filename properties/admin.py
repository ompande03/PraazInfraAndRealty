
from django.contrib import admin
from django.utils.html import format_html
from .models import Property, PropertyImage, PropertyEnquiry


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 10
    fields = ('image', 'caption')
    verbose_name = "Additional Property Image"
    verbose_name_plural = "Property Image Gallery"


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'location',
        'price',
        'availability',
        'is_published',
        'is_featured',
        'created_at',
    )

    search_fields = ('title', 'location', 'description')

    list_filter = (
        'category',
        'availability',
        'is_published',
        'is_featured',
    )

    list_editable = ('is_published', 'is_featured')

    readonly_fields = (
        'created_at',
        'updated_at',
        'image_preview',
    )

    inlines = [PropertyImageInline]

    fieldsets = (
        ('Property Information', {
            'fields': (
                'title',
                'category',
                'location',
                'description',
            )
        }),

        ('Pricing and Details', {
            'fields': (
                'price',
                'area_sqft',
                'bedrooms',
                'bathrooms',
            )
        }),

        ('Cover Image', {
            'fields': (
                'cover_image',
                'image_preview',
            )
        }),

        ('Publishing Settings', {
            'fields': (
                'availability',
                'is_featured',
                'is_published',
            )
        }),

        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    @admin.display(description='Cover Image Preview')
    def image_preview(self, obj):
        if obj and obj.cover_image:
            return format_html(
                '<img src="{}" width="180" style="border-radius:10px;" />',
                obj.cover_image.url
            )
        return "No cover image uploaded"

@admin.register(PropertyEnquiry)
class PropertyEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'service',
        'preferred_location',
        'created_at',
        'is_contacted',
    )

    list_filter = ('service', 'is_contacted', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'preferred_location')
    readonly_fields = ('created_at',)
    list_editable = ('is_contacted',)
    ordering = ('-created_at',)


admin.site.site_header = "PRAAZ INFRA AND REALTY"
admin.site.site_title = "Praaz Admin"
admin.site.index_title = "Property Management Dashboard"


