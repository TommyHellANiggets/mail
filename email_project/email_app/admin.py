from django import forms
from django.contrib import admin
from .models import Product, Color, Size, ProductImage
from django.utils.safestring import mark_safe


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 8  # Количество дополнительных форм для изображений
    max_num = 8  # Максимальное количество изображений
    fields = ['image', 'preview']

    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;"/>') if obj.image else ""

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Настройка чекбоксов для цветов и размеров
        self.fields['colors'].queryset = Color.objects.all()
        self.fields['colors'].widget = forms.CheckboxSelectMultiple()
        self.fields['colors'].widget.choices = [
            (color.id, mark_safe(
                f'<span style="background-color: {color.name}; '
                f'border-radius: 50%; width: 12px; height: 12px; '
                f'display: inline-block; margin-right: 5px;"></span>{color.get_name_display()}'
            ))
            for color in self.fields['colors'].queryset
        ]

        self.fields['sizes'].queryset = Size.objects.all()
        self.fields['sizes'].widget = forms.CheckboxSelectMultiple()
        self.fields['sizes'].widget.choices = [
            (size.id, mark_safe(f'{size.get_name_display()}'))
            for size in self.fields['sizes'].queryset
        ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 8  # Количество дополнительных форм для изображений
    max_num = 8  # Максимальное количество изображений
    fields = ['image', 'preview']

    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;"/>') if obj.image else ""

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductImageInline]

    list_display = ['name', 'category', 'wildberries_link', 'ozon_link']
    search_fields = ['name', 'category']

    fieldsets = (
        (None, {
            'fields': ('name', 'category')
        }),
        ('Details', {
            'fields': ('colors', 'sizes', 'characteristics', 'care_instructions', 'wildberries_link', 'ozon_link'),
        }),
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
