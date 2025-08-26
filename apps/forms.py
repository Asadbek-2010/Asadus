from django.forms.models import ModelForm

from apps.models import Register


class RegisterModelForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'