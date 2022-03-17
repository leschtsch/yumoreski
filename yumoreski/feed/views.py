from django.shortcuts import render, redirect
from .models import Jokes
from .forms import JokesForm


# Create your views here.
def feed(request):
    jokes = Jokes.objects.order_by('?')[:15]
    return render(request, 'feed/feed.html', {'jokes': jokes})


def add(request):
    if not request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = JokesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {
        "form": JokesForm
    }
    return render(request, 'feed/add.html', context)
