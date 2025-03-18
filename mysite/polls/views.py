from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from polls.models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # return HttpResponse()(f'You are looking at question: {question_id}')
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {
    #         'question': question
    #     }
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist!')

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    return HttpResponse(f'You are looking at results of: {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting at question: {question_id}')
