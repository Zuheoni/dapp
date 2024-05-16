from django.urls import path
from .views import base_views, question_views, response_views, vote_views

app_name = 'dapp' # NameSpace 이름 설정

urlpatterns = [
    ## base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'), # URL 별칭(alias) 이용.

    ## question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    ## response_views.py
    path('response/create/<int:question_id>/',
         response_views.response_create, name='response_create'),
    path('response/modify/<int:response_id>/',
         response_views.response_modify, name='response_modify'),
    path('response/delete/<int:response_id>/',
         response_views.response_delete, name='response_delete'),

    ## vote_views.py
    path('vote/question/<int:question_id>/',
         vote_views.vote_question, name='vote_question'),
    path('vote/response/<int:response_id>/',
         vote_views.vote_response, name='vote_response'),

]