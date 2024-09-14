from django import forms

from mainapp.models import EmailPost


class EmailPostForm(forms.ModelForm):

    class Meta:
        model = EmailPost
        fields = '__all__'

    def clean_email(self):
        clean_data = self.cleaned_data['email']
        if '@mail.ru' not in clean_data:
            raise forms.ValidationError('Не отечественная почта')
        return clean_data
