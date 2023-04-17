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

# @login_required
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
@login_required
def nominee_vote(request, category_id):
    category = get_object_or_404(NominationCategory, pk=category_id)
    
    last_vote_time = request.session.get('last_vote_time')
    if last_vote_time:
        last_vote_time = datetime.strptime(last_vote_time, '%Y-%m-%dT%H:%M:%S.%f')
        time_since_last_vote = datetime.now() - last_vote_time
        if time_since_last_vote < timedelta(hours=1):
            return redirect('polls:vote_limit')  # Redirect to the vote_limit view

# @login_required
# def nominee_vote(request, category_id):
#     category = get_object_or_404(NominationCategory, pk=category_id)
#     try:
#         selected_nominee = category.nominee_set.get(pk=request.POST["nominee"])
#     except (KeyError, Nominee.DoesNotExist):
#         # Redisplay the nomination category detail form.
#         messages.error(request, "You didn't select a nominee.")
#         # return HttpResponseRedirect(reverse("polls:nomination_category_detail", args=(category.id,)))
#         return redirect('polls:thank_you_forvoting')
#     else:
#         # Increment the votes for the selected nominee and save the changes.
#         # You'll need to add a "votes" field to the Nominee model before using this line.
#         selected_nominee.votes += 1
#         selected_nominee.save()

#         # Redirect to the results page for this category.
#         # You'll need to create a "nomination_category_results" view and corresponding URL pattern.
#         # return HttpResponseRedirect(reverse("polls:nomination_category_results", args=(category.id,)))
#         return redirect('polls:thank_you_forvoting')

# @login_required
# def nominee_vote(request, category_id):
#     category = get_object_or_404(NominationCategory, pk=category_id)
    
#     # Check if the user has voted within the last hour
#     last_vote_time = request.session.get('last_vote_time')
#     if last_vote_time:
#         last_vote_time = datetime.strptime(last_vote_time, '%Y-%m-%dT%H:%M:%S.%f')
#         time_since_last_vote = datetime.now() - last_vote_time
#         if time_since_last_vote < timedelta(hours=1):
#             messages.error(request, "You can only vote once per hour.")
#             return redirect('polls:thank_you_forvoting')

#     try:
#         selected_nominee = category.nominee_set.get(pk=request.POST["nominee"])
#     except (KeyError, Nominee.DoesNotExist):
#         messages.error(request, "You didn't select a nominee.")
#         return redirect('polls:thank_you_forvoting')
#     else:
#         selected_nominee.votes += 1
#         selected_nominee.save()

#         # Update the session with the new vote timestamp
#         request.session['last_vote_time'] = datetime.now().isoformat()

#         return redirect('polls:thank_you_forvoting')

@login_required
def nominee_vote(request, category_id):
    category = get_object_or_404(NominationCategory, pk=category_id)
    
    # Check if the user has voted within the last hour
    last_vote_time = request.session.get('last_vote_time')
    if last_vote_time:
        last_vote_time = datetime.strptime(last_vote_time, '%Y-%m-%dT%H:%M:%S.%f')
        time_since_last_vote = datetime.now() - last_vote_time
        if time_since_last_vote < timedelta(hours=1):
            return redirect('polls:vote_limit')  # Redirect to the vote_limit view

    try:
        selected_nominee = category.nominee_set.get(pk=request.POST["nominee"])
    except (KeyError, Nominee.DoesNotExist):
        messages.error(request, "You didn't select a nominee.")
        return redirect('polls:thank_you_forvoting')
    else:
        selected_nominee.votes += 1
        selected_nominee.save()

        # Update the session with the new vote timestamp
        request.session['last_vote_time'] = datetime.now().isoformat()

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
