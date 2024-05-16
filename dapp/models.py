from django.contrib.auth.models import User
from django.db import models

# Create your models here.
## 신고/질문 게시
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question') # 글쓴이 (author) 필드, FK:유저
    subject = models.CharField(max_length=200) # 제목
    content = models.TextField() # 내용
    create_date = models.DateTimeField() # 신고 날짜
    modify_date = models.DateTimeField(null=True, blank=True) # 수정 일시; 값이 비워져 있어도 가능함
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천 기능 추가

    ## 속성값 표시:
    def __str__(self):
        return self.subject

## 신고에 대한 답변/대응
class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_response')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_response')

'''
## Comment 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, null=True, blank=True, on_delete=models.CASCADE)
    '''