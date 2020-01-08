from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from musicapp.authentication.forms import LoginForm

from django.contrib.auth import get_user_model
User = get_user_model()

from musicapp.authentication.forms import SignupForm
from musicapp.jamusers.models import CustomUser
from django.views.generic.edit import FormView


def login_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class SignUpView(FormView):
    template_name = 'generic_form.html'
    form_class = SignupForm

    def get_context_data(self):
        context = super(SignUpView, self).get_context_data()
        context['title']='signup'
        return context

    def form_valid(self,form):
        data = form.cleaned_data
        user = User.objects.create_user(
            username=data['email'],
            password=data['password']
        )
        login(self.request, user)
        CustomUser.objects.create(
            email=data['username'],
            user=user
        )

        return HttpResponseRedirect(reverse('homepage'))