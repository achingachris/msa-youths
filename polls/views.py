from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice, Category, Nominee, Vote
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# list all categories and nominees
def index(request):
    categories = Category.objects.all()
    nominees = Nominee.objects.all()
    context = {'categories': categories, 'nominees': nominees}
    return render(request, 'index.html', context)

@login_required
def vote(request):
    if request.method == 'POST':
        user = request.user
        nominee_id = request.POST.get('nominee')
        nominee = Nominee.objects.get(pk=nominee_id)
        timestamp = timezone.now()
        try:
            vote = Vote.objects.get(user=user, nominee__category=nominee.category)
            vote.nominee = nominee
            vote.timestamp = timestamp
            vote.save()
        except ObjectDoesNotExist:
            vote = Vote(user=user, nominee=nominee, timestamp=timestamp)
            vote.save()
        return redirect('vote_success')
    else:
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'vote.html', context)

# def nominees(request, category_id):
#     category = Category.objects.get(pk=category_id)
#     nominees = Nominee.objects.filter(category=category)
#     context = {'category': category, 'nominees': nominees}
#     return render(request, 'nominees.html', context)

def vote_success(request):
    return render(request, 'vote_success.html')



























def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

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