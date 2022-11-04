from django.shortcuts import render
from . import forms
import os
from datetime import datetime
import openai
from dotenv import load_dotenv
from .utils import call_api

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = SECRET_KEY

# on initialise nos variables
messages = []
user_prompt = ""

def chatbox(request):
    form = forms.InputForm(request.POST or None)
    user_msg = None     
    logged_in_user = request.user
    
    if form.is_valid() : # si l'utilisateur a envoyé un message
        user_msg = form.cleaned_data['text_msg'] # on récupère sa saisie
        messages.append({user_msg : ""}) # on ajoute le message de l'user dans la liste messages
        time = datetime.today().strftime('%H:%M')
        
        response = call_api(user_msg) # on appelle la fonction qui appelle l'API
        
        # on normalise les messages de l'utilisateur et de l'IA
        normalized_user_message = user_msg.replace(" ", "").replace(",", "").replace(".", "").lower()
        normalized_bot_message = response.replace(" ", "").replace(",", "").replace(".", "").lower()[2:]
        form = forms.InputForm() # on vide le formulaire
        
        if normalized_user_message == normalized_bot_message: # si les messages sont identiques donc pas de fautede l'user
            global user_prompt
            # on ajoute a user_prompt l'historique de la conversation et le nouveau message de l'utilisateur
            user_prompt += f"You: {user_msg}\nFriend:"
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=user_prompt,
                temperature=0.5,
                max_tokens=600,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["You:"]
                )
            messages.append({'': response['choices'][0]['text']}) # on ajoute la reponse du BOT à la variable messages
            user_prompt += response['choices'][0]['text'] # on ajoute la réponse du BOT dans l'historique pour la prochaine requete a l'API
            return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})

        else: # si il y a une faute de grammaire
            messages.append({"" : "Your sentence is incorrect. It should be as follow:"})
            messages.append({"" : response}) # réponse du BOT
            messages.append({"" : "Try to write it again to improve your skill."})
            return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'time': time})

    else:
        if str(logged_in_user) != "AnonymousUser": # si l'utilisateur est connecté.
            messages.clear()
            messages.append({"": f"Hello {logged_in_user}, nice to see you."})
        else:
            messages.clear()
        return render(request, "chatbox/chatbox.html", {'form': form, 'messages':messages, 'user_name': logged_in_user})

