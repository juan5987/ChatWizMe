from django.shortcuts import render
from . import forms
import os
from datetime import datetime
import openai
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = SECRET_KEY

user_messages = []
bot_messages = []

messages = {}
correction = []

def chatbox(request):
    form = forms.InputForm(request.POST or None)
    
    user_msg = None
    
    if request.method == "POST" :
        if form.is_valid() :
            user_msg = form.cleaned_data['text_msg']
            user_messages.append(user_msg)
            form.save()
            form = forms.InputForm()
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"Correct this to standard English:{user_msg}",
                temperature=0,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                )
            normalized_user_message = user_msg.replace(" ", "").lower()
            normalized_bot_message = response['choices'][0]['text'].replace(" ", "").replace(",", "").lower()[2:]
            
            # final_bot_message = "Your sentence is incorrect. It should be as follow:" + "\n\n" + response['choices'][0]['text'] + "\n\n" + "\n\n" "Try to write it again to improve your skill."
            
            message1 = "Your sentence is incorrect. It should be as follow:"
            message2 = response['choices'][0]['text']
            message3 = "Try to write it again to improve your skill."
            
            if normalized_user_message == normalized_bot_message:
                
                response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=f"You: {user_msg}\nFriend:",
                    temperature=0.5,
                    max_tokens=600,
                    top_p=1.0,
                    frequency_penalty=0.5,
                    presence_penalty=0.0,
                    stop=["You:"]
                    )
                final_bot_message = response['choices'][0]['text']
                bot_messages.append(final_bot_message)
                time = datetime.today().strftime('%H:%M')
                messages[user_messages[len(user_messages) - 1]] = bot_messages[len(bot_messages) - 1]
                return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})
                
            else:
                correction = [message1, message2, message3]
                time = datetime.today().strftime('%H:%M')         
                messages[user_messages[len(user_messages) - 1]] = ""
                return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time, 'correction' : correction})
        
        else:
            return render(request, "chatbox/chatbox.html", {'form': form})
        
    else:
        return render(request, "chatbox/chatbox.html", {'form': form})
