from django.shortcuts import render, redirect
from App.forms import CandidateForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully provided your details')
            return redirect('/')
    else:
        form = CandidateForm()
        print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'app/home.html', context)

