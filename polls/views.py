from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.http import Http404
from .models import Question, Choice 


# Create your views here.
def index(request):
    # 예1번 - 단순 텍스트 ------------
    # return HttpResponse("Hello, world. You're at the polls index.")
    # 예2번 - ORM 결과를 가져와서 화면에 ','로 붙여 보여준다. ------------
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # 예3번 - 템플릿을 적용한다. ------------
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    # 예4번은 3번 방식의 개선(간편) 버전
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 예 1
    # return HttpResponse("You're looking at question %s." % question_id)
    # 예 2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})번
    # 예 3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)