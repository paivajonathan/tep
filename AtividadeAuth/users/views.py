from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        filtered_users_by_username = get_user_model().objects.filter(username=username)

        if filtered_users_by_username.exists():
            return render(request, "register.html", {"error": "Usuário já existe."})
        
        get_user_model().objects.create_user(username=username, email=email, password=password)

        return render(request, "login.html")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return render(request, "home.html")
        
        return render(request, "login.html", {"error": "Usuário ou senha incorreto(s)."})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
