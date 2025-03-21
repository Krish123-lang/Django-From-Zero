from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Choice, Question
from django.db.models import F
from django.views import generic
from django.utils import timezone
# Create your views here.

'''
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
    # return HttpResponse(f'You are looking at results of: {question_id}')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})
'''

# *** Generic Views ***


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # return HttpResponse(f'You are voting at question: {question_id}')

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question": question, "error_message": "You did'nt select a choice!"})

    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
