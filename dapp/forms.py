from django import forms
from dapp.models import Question, Response

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']


        '''
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }'''
        labels = { # 한글로 표시
            'subject': '제목',
            'content': '내용',
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']
        labels = {
            'content': '답변내용',
        }