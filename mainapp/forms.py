import django.forms as forms
from mainapp.models import Game, GameComment, ComplaintGCG


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class GameCommentForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ('avatar', 'text', 'author', 'game_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ('complaint_quantity',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ComplaintGCForm(forms.ModelForm):
    class Meta:
        model = ComplaintGCG
        fields = ('user_complaint', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'