import django.forms as forms
from forums.models import ForumsRazdel, ForumsTema, ForumsComment, ComplaintGCF


class ForumsRazdelForm(forms.ModelForm):
    class Meta:
        model = ForumsRazdel
        fields = ('name_game',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ForumsTemaForm(forms.ModelForm):
    class Meta:
        model = ForumsTema
        fields = ('razdel', 'name', 'author', 'text', 'photo')

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


class ComplaintTemaForm(forms.ModelForm):
    class Meta:
        model = ForumsTema
        fields = ('tema_complaint_quantity',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintCommentForm(forms.ModelForm):
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
