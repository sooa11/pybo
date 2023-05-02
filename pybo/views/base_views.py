from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.db.models import Q, Count

def index(request):
    # -create_date로 해야 먼저작성한 글이 밀려 내려가게됨
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어 3-14 추가
    so = request.GET.get('so', 'recent') # 정렬기준
    question_list = Question.objects.order_by('-create_date')
    if kw: # 3-14 추가
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(answer__content__icontains=kw) | # 답변 내용 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()

    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # question_list는 페이징 객체(page_obj), # 3-14 검색추가
    # context = {'question_list': question_list} # 위에 context 사용으로 전에 써둔거 off
    return render(request, 'pybo/question_list.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # pk = primary key 에 해당하는 값
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)