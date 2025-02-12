from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login') # 로그아웃 상태라면 자동으로 로그인 화면으로 이동
def question_create(request):
    ''' 질문 등록 '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 실제 객체를 받기 위한 임시 저장 선언
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('dapp:index')

    else: # method = GET 인 경우
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'dapp/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """ dapp 질문 수정 """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dapp:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now() # 수정일시 저장
            question.save()
            return redirect('dapp:detail', question_id=question.id)

    else:
        form = QuestionForm(instance=question)

    context = {'form': form}
    return render(request, 'dapp/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """ dapp 질문 삭제 """

    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('dapp:detail', question_id=question.id)

    question.delete()
    return redirect('dapp:index')