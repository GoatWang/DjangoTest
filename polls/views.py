from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404


# Create your views here


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([str(q) for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {'latest_question_list':latest_question_list}

    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    question = get_object_or_404(Question, pk=question_id)
    
    # return HttpResponse("You are looking at question{}".format(question_id))
    return render(request, "polls/detail.html", {'question':question})

def results(request, question_id):
    return HttpResponse("You looking at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You are voting on question {}".format(question_id))





