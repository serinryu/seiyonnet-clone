from django.shortcuts import render, redirect
from django.contrib import auth #데이터베이스에 이미 있는지 확인하는 authenticate()메소드 사용가능
from django.contrib.auth.models import User

def login(request):
	#POST 요청이 들어오면 로그인 처리
	if request.method == 'POST':
		userid = request.POST['username']
		pwd = request.POST['password']
		user = auth.authenticate(request, username=userid, password=pwd) 
		if user is not None:
			auth.login(request, user) #로그인
			return redirect('home')
		else:
			return render(request, 'login.html')

	#GET 요청이 들어오면 login.html 띄워주기
	else:
		return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
            email=request.POST['email'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')