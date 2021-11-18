from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import User
from django.contrib import auth
from space.models import Booking


"""
login
"""
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # 해당 계정 정보가 있는지 확인
        user = authenticate(username = username, password = password)
        
        if user is not None:    # 로그인 성공
            login(request, user)
            return redirect('main')
        else:
            # 로그인 실패
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')


"""
signup
"""
def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                # Django 기본 User 필드
                username = request.POST["username"],
                password = request.POST["password"],

                # 확장 User 필드
                nickname = request.POST["nickname"],
                phone = request.POST["phone"]
            )
            user.save()
            
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


"""
logout
"""
def user_logout(request):
    logout(request)
    return redirect('main')


"""
mypage
"""
def mypage(request):
    book = Booking.objects.all()
    return render(request, 'mypage.html', {'book':book})