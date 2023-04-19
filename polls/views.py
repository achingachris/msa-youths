from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question, NominationCategory, Nominee
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.core.cache import cache

# API imports
from rest_framework import generics
from .serializers import NomineeSerializer, NominationCategorySerializer

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    category = NominationCategory.objects.all()
    context = {"latest_question_list": latest_question_list, "category": category}
    return render(request, "polls/index.html", context)

def viewcategories(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    category = NominationCategory.objects.all()
    context = {"latest_question_list": latest_question_list, "category": category}
    return render(request, "polls/votedetails.html", context)

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

    
def nominee_vote(request, category_id):
    category = get_object_or_404(NominationCategory, pk=category_id)
    
    last_vote_time = request.session.get('last_vote_time')
    if last_vote_time:
        last_vote_time = datetime.strptime(last_vote_time, '%Y-%m-%dT%H:%M:%S.%f')
        time_since_last_vote = datetime.now() - last_vote_time
        if time_since_last_vote < timedelta(hours=1):
            return redirect('polls:vote_limit')  # Redirect to the vote_limit view


def nominee_vote(request, category_id):
    category = get_object_or_404(NominationCategory, pk=category_id)

    try:
        selected_nominee = category.nominee_set.get(pk=request.POST["nominee"])
    except (KeyError, Nominee.DoesNotExist):
        messages.error(request, "You didn't select a nominee.")
        return redirect('polls:thank_you_forvoting')
    else:
        selected_nominee.votes += 1
        selected_nominee.save()

        return redirect('polls:thank_you_forvoting')
  
def nomination_category_results(request, category_id):
    category = get_object_or_404(NominationCategory, pk=category_id)
    nominees = category.nominee_set.all().order_by('-votes')
    return render(request, "polls/vote_results.html", {"nomination_category": category, "nominees": nominees})


def not_registered(request):
    return render(request, 'polls/not_registered.html')

def thank_you_forvoting(request):
    return render(request, 'polls/thankyou.html')

def vote_limit(request):
    last_vote_time = request.session.get('last_vote_time')
    remaining_time = None
    if last_vote_time:
        last_vote_time = datetime.strptime(last_vote_time, '%Y-%m-%dT%H:%M:%S.%f')
        next_vote_time = last_vote_time + timedelta(hours=1)
        remaining_time = (next_vote_time - datetime.now()).total_seconds()
    return render(request, 'polls/vote_limit.html', {'remaining_time': remaining_time})


# API VIEW

class NominationCategoryList(generics.ListAPIView):
    queryset = NominationCategory.objects.all()
    serializer_class = NominationCategorySerializer
    
class NomineesByCategory(generics.ListAPIView):
    serializer_class = NomineeSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Nominee.objects.filter(category__id=category_id)

class NominationCategoryDetail(generics.RetrieveAPIView):
    queryset = NominationCategory.objects.all()
    serializer_class = NominationCategorySerializer