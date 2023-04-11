from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question, NominationCategory, Nominee
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    category = NominationCategory.objects.all()
    context = {"latest_question_list": latest_question_list, "category": category}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def nomination_category_detail(request, nomination_category_id):
    nomination_category = get_object_or_404(NominationCategory, pk=nomination_category_id)
    nominees = Nominee.objects.filter(category=nomination_category)
    return render(request, "polls/category_detail.html", {"nomination_category": nomination_category, "nominees": nominees})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))