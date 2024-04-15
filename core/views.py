from django.shortcuts import render,redirect
from .models import *
from .forms import CommentForm
import random
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    comments = list(Comment.objects.all())  # Convert queryset to list
    random.shuffle(comments)  # Shuffle the list
    return render(request, 'index.html', {'comments': comments})
@login_required(login_url='login')
def add(request):
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST,request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.name = request.user.username
			comment.save()
			return redirect('home')
			
             
	return render(request,"add.html",{'form':form})

def register(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		repass= request.POST['repass']

		if password == repass:
			if User.objects.filter(username=username).exists():
				messages.info(request,"The username already here")
				
			elif User.objects.filter(email=email).exists():
				messages.info(request,"The email is already here")
				

			else:
				User.objects.create_user(username=username,email=email,password=password)
				return redirect('login')

		else:
			messages.info(request,"The password aren't same")

	return render(request,"register.html")

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return  redirect('/')
		else:
			messages.info(request,"Credential invalid")
	return render(request,"login.html")

@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('/')


@login_required(login_url='login')
def update(request,pk):
	posts = Comment.objects.get(title=pk)

	if request.method == "POST":
		title = request.POST['title']
		body = request.POST['body']
		
		posts.title = title
		posts.body = body
		posts.save()
		return redirect('/')


	return render(request,"update.html",{'comments':posts})



@login_required(login_url='login')
def delete(request,pk):
	posts = Comment.objects.get(title=pk)
	posts.delete()
	return redirect('/')




@login_required(login_url='login')
def show_the_post(request,comment):
	comment = Comment.objects.get(title=comment)
	return render(request,"show.html",{'comment':comment})
# The code is running fine totally 100 lines of coding