from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def base_template(request):
    return render(request, 'base_template.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profile(request):
    return render(request, "registration/profile.html", {})

def memory(request):
    return render(request, "memory.html", {})

def snake(request):
    return render(request, "snake.html", {})

def paint(request):
    return render(request, "paint.html", {})

