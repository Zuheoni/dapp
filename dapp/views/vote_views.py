from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from ..models import Question, Response


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    dapp 질문 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')

    else:
        question.voter.add(request.user)

    return redirect('dapp:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_response(request, response_id):
    """
    dapp 답글 추천 등록
    """
    response = get_object_or_404(Response, pk=response_id)
    if request.user == response.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')

    else:
        response.voter.add(request.user)

    return redirect('dapp:detail', question_id=response.question.id)


