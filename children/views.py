import django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Guardians, Children
from .forms import GuardiansForm, ChildrensForm, SignUpForm

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

@login_required(login_url='/auth/login')
def guardians(request):
    guardians = Guardians.objects.all()
    form = GuardiansForm()
    if request.method == "POST":
        form = GuardiansForm(request.POST, request.FILES)
        if form.is_valid():
            guardian = form.save(commit = False)
            guardian.save_guardian()
    return render(request, 'guardians/guardians.html',
        {"guardians":guardians,"forms":form})

@login_required(login_url='/auth/login')
def children(request):
    children = Children.objects.all()
    form = ChildrensForm()
    if request.method == "POST":
        form = ChildrensForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit = False)
            child.save_child()
    return render(request, 'children/children.html',
        {"children":children,"forms":form})

@login_required(login_url='/auth/login')
def one_guardian(request, pk):
    guardian = Guardians.objects.get(id=pk)
    return render(request, 'guardians/one_guardian.html',
        {"guardian":guardian})

@login_required(login_url='/auth/login')
def one_child(request, pk):
    child = Children.objects.get(id=pk)
    return render(request, 'children/one_child.html',
        {"child":child})

@login_required(login_url='/auth/login')
def addChildren(request):
    return redirect("children")
