import django.forms as forms
from news.models import New, NewComment, ComplaintGC


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = NewComment
        fields = ('avatar', 'text', 'author', 'new_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = NewComment
        fields = ('complaint_quantity',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintGCForm(forms.ModelForm):
    class Meta:
        model = ComplaintGC
        fields = ('user_complaint', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'