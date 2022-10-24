from django.shortcuts import render
from . import models
from . import forms
import os
import openai
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = SECRET_KEY

user_messages = []
bot_messages = []

messages = {}


def chatbox(request):
    form = forms.InputForm(request.POST or None)
    
    new_msg = None
    
    if request.method == "POST" :
        if form.is_valid() :
            new_msg = form.cleaned_data['text_msg']
            user_messages.append(new_msg)
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: {user_messages[len(user_messages) - 1]}\nAI: ",
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )
            bot_messages.append(response['choices'][0]['text'])
            messages[new_msg] = response['choices'][0]['text']
            form.save()
            form = forms.InputForm()
            return render(request, "chatbox/chatbox.html", {'form': form, 'user_messages': user_messages, 'bot_messages': bot_messages, 'messages':messages})
        
        else:
            return render(request, "chatbox/chatbox.html", {'form': form})
        
    else:
        return render(request, "chatbox/chatbox.html", {'form': form})