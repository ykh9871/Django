from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    # 'pybo/question_list.html' -> 'pvbo/경로에 해당하는 디렉토리 생성이 필요
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question =get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # save()랑 동일한 기능
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now()) # 
    return redirect('pybo:detail', question_id=question.id)