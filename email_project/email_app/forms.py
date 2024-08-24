from django import forms
from .models import Product, Color

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'colors': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the checkbox labels to include color circles
        for color in self.fields['colors'].queryset:
            self.fields['colors'].widget.choices.queryset = Color.objects.all()
            self.fields['colors'].widget.choices = [
                (color.id, mark_safe(f'<span style="background-color: {color.hex_code}; border-radius: 50%; width: 12px; height: 12px; display: inline-block; margin-right: 5px;"></span>{color.name}'))
                for color in self.fields['colors'].queryset
            ]
