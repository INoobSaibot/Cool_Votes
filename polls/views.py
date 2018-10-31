from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Choice, Question

from django.shortcuts import get_object_or_404, render

from django.http import Http404

from django.urls import reverse



def OLDindex(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index!!")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #old
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})    
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

    #old results/ action
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Rededisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didnt select a choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpRespsonseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    # old return / action
    return HttpResponse("You're voting on question %s." % question_id)