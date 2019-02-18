from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
            # 위에가 전부 실행이 된다면 blog로 가라.
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else :
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else :
        return render(request, 'login.html')

def logout(request):
    if auth.authenticate:
        auth.logout(request)
        # logout이라는 함수를 이용하여 현재 로그인된 유저를 로그아웃시킨다.
        return redirect('home')
    else : 
        return render(request, 'login.html') 
    # 위에가 아니라면 login화면으로 간다.