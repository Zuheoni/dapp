from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question


def index(request):

    ## 입력 인자
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어(키워드)
    so = request.GET.get('so', 'recent') # 정렬 기준

    ## 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_response=Count('response')).order_by('-num_response', '-create_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date') # 작성일시의 '역순'(-)

    ## 조회
    if kw:
        question_list = question_list.filter(  # 'i'constains는 대소문자 가리지 않고 찾아준다.
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(response__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    ## 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    # render() : context에 있는 Question model 데이터 question_list를 HTML 코드로 변환 => '템플릿'
    return render(request, 'dapp/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'dapp/question_detail.html', context)