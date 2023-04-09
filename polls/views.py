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

def vote(request):
    # Get all categories
    categories = Category.objects.all()

    # Check if the user has submitted a vote
    if request.method == 'POST':
        # Get the selected nominees for each category
        selected_nominees = {}
        for category in categories:
            nominee_id = request.POST.get(str(category.id))
            if nominee_id:
                selected_nominees[category.id] = nominee_id

        # Create a vote for each selected nominee
        for category_id, nominee_id in selected_nominees.items():
            nominee = get_object_or_404(Nominee, id=nominee_id)
            vote = Vote(user=request.user, nominee=nominee)
            vote.save()

        # Redirect back to index
        return redirect('polls:success')

    # Render the vote template with all categories and their nominees
    context = {'categories': categories}
    return render(request, 'vote.html', context)


def vote_success(request):
    return render(request, 'vote_success.html')

def waiting_view(request):
    return render(request, 'waiting.html')