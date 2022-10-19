from django.shortcuts import render

def chatbox(request):
    return render(request, "chatbox/chatbox.html")
