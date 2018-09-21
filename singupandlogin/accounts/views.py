from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import SignUpForm

# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Data {}".format(form.cleaned_data()))
        if form.is_valid():

            form.save()

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form':form})


















