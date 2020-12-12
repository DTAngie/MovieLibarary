from django.forms import ModelForm
from .models import Award

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = ['year', 'name', 'category']