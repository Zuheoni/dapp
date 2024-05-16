from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import ResponseForm
from ..models import Question, Response


@login_required(login_url='common:login')
def response_create (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user # author 필드
            response.create_date = timezone.now()
            response.question = question
            response.save()
            return redirect('{}#response_{}'.format(
                resolve_url('dapp:detail', question_id=question.id), response.id))

    else:
        form = ResponseForm()

    context = {'question': question, 'form': form}
    return render(request, 'dapp/question_detail.html', context)

@login_required(login_url='common:login')
def response_modify(request, response_id):
    """ dapp 답변 수정 """
    response = get_object_or_404(Response, pk=response_id)
    if request.user != response.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('dapp:detail', question_id=response.question.id)

    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=response)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.modify_date = timezone.now()
            response.save()
            return redirect('{}#response_{}'.format(
                resolve_url('dapp:detail', question_id=response.question.id), response.id))

    else:
        form = ResponseForm(instance=response)

    context = {'response': response, 'form': form}
    return render(request, 'dapp/response_form.html', context)

@login_required(login_url='common:login')
def response_delete(request, response_id):
    """ dapp 답변 삭제 """
    response = get_object_or_404(Response, pk=response_id)
    if request.user != response.author:
        messages.error(request, '삭제권한이 없습니다')

    else:
        response.delete()

    return redirect('dapp:detail', question_id=response.question.id)