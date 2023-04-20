from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            row_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=row_password) # 사용자 인증 담당
            login(request, user)    # 로그인 담당
            return redirect("index")
    else:   # GET 요청일 때
        form = UserForm()
    return render(request, "common/signup.html", {"form": form})