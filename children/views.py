import django
from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.

@login_required(login_url='/auth/login')
def Index(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print("success")
            login(request, user)
            return redirect('index_view')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})