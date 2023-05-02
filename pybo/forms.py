from django import forms
from pybo.models import Question, Answer, Comment # 강사님 .models 책 = pybo.models

class QuestionForm(forms.ModelForm): #ModelForm에서 M 대문자 나만 씀
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question on 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        ## {{ form.as_p }} 사용으로 필요없어짐
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # ## 위젯 속성을 지정하면 sub, cont 입력 필드에 form-control 과 같은 부트스트랩 클래스를 추가할 수 있다.
        # 질문 등록페이지 빈칸 크기가 변경되었음
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }