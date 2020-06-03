import django.forms as forms
from forums.models import ForumsRazdel, ForumsTema, ForumsComment, ComplaintGCF


class ForumsTema(forms.ModelForm):
    class Meta:
        model = ForumsRazdel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ForumsCommentForm(forms.ModelForm):
    class Meta:
        model = ForumsComment
        fields = ('avatar', 'text', 'author', 'forums')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = ForumsComment
        fields = ('com_complaint_quantity',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintGCForm(forms.ModelForm):
    class Meta:
        model = ComplaintGCF
        fields = ('user_complaint', 'tema',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'