
# Create your views here.

from django.shortcuts import redirect, render
from django.contrib import messages
from .form import UserRegisterForm

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, Your account has been created successfully, you can now log in !!'
            )
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})