from django.shortcuts import render
from .models import UserName

def index(request):
    text_hello = ""
    err = ""

    if request.method == 'POST':
        user_name = request.POST.get('name')
        
        if user_name == "":
            err = "Ошибка пустое имя!"
        else:
            n = UserName(name=user_name)
            n.save()
            text_hello = "Привет, " + user_name + "!"

    return render(request, 'salamchik/index.html', {'text_hello': text_hello, 'err': err})