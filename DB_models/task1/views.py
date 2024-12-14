from django.shortcuts import render
from .models import Buyer, Game


# Create your views here.


def platform(request):
    return render(request, 'platform.html')


def games(request):
    title = 'Игры'
    games = [game for game in Game.objects.all()]

    context = {
        'title': title, 'games': games}
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {'title': title, 'text': text}
    return render(request, 'cart.html', context)


def sign_up_by_html(request):
    usernames = [buyer.name for buyer in Buyer.objects.all()]
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get('age')

        if password == repeat_password and username not in usernames:
            Buyer.objects.create(name=username, balance=100, age=age)
            welcome = f'Приветствуем, {username}!'
            info['welkom'] = welcome


        elif password != repeat_password:
            error_password = "Пароли не совпадают"
            info['error_password'] = error_password
            if username in usernames:
                error_username = "Пользователь уже существует"
                info['error_username'] = error_username

        elif username in usernames:
            error_username = "Пользователь уже существует"
            info['error_username'] = error_username

    return render(request, 'registration_page.html', info)
