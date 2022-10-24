from django.shortcuts import render
from . import models
from . import forms


user_messages = []
bot_messages = []

def chatbox(request):
    form = forms.InputForm(request.POST or None)
    
    new_msg = None
    
    if request.method == "POST" :
        if form.is_valid() :
            new_msg = form.cleaned_data['text_msg']
            user_messages.append(new_msg)
            print(user_messages)
            form.save()
            form = forms.InputForm()
            return render(request, "chatbox/chatbox.html", {'form': form, 'user_messages': user_messages})
        else:
            return render(request, "chatbox/chatbox.html", {'form': form})
    else:
        return render(request, "chatbox/chatbox.html", {'form': form})