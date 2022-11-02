from django.shortcuts import render
from . import forms
import os
from datetime import datetime
import openai
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = SECRET_KEY

messages = []

def chatbox(request):
    form = forms.InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
    
    
    
    if form.is_valid() :
        user_msg = form.cleaned_data['text_msg']
        
        if user_msg == "Who is the best teacher in Simplon ?":
            messages.append({user_msg: "Who is teaching you today, Charles or Jeremy ?"})
            time = datetime.today().strftime('%H:%M')
            form = forms.InputForm()
            return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})
        elif user_msg == "Jeremy":
            messages.append({user_msg: "I think Jeremy is the best teacher"})
            time = datetime.today().strftime('%H:%M')
            form = forms.InputForm()
            return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})
        elif user_msg == "Charles":
            messages.append({user_msg: "I think Charles is the best teacher"})
            time = datetime.today().strftime('%H:%M')
            form = forms.InputForm()
            return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})
        else:
            messages.append({user_msg : ""})
            form.save()
            form = forms.InputForm()
            time = datetime.today().strftime('%H:%M')
            response = openai.Completion.create(
                    model="text-davinci-002",
                    prompt=f"Correct this to standard English:{user_msg}",
                    temperature=0,
                    max_tokens=60,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                    )
            
            normalized_user_message = user_msg.replace(" ", "").replace(",", "").replace(".", "").lower()
            normalized_bot_message = response['choices'][0]['text'].replace(" ", "").replace(",", "").replace(".", "").lower()[2:]
            print(normalized_user_message, normalized_bot_message)
            form = forms.InputForm()
            
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
                messages.append({'': response['choices'][0]['text']})
                return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})

            else:
                messages.append({"" : "Your sentence is incorrect. It should be as follow:"})
                messages.append({"" : response['choices'][0]['text']})
                messages.append({"" : "Try to write it again to improve your skill."})
                return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})

    else:
        if str(logged_in_user) != "AnonymousUser":
            messages.clear()
            messages.append({"": f"Hello {logged_in_user}, how are you doing today ?"})
        else:
            messages.clear()
        return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})

