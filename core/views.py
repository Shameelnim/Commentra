from django.shortcuts import render,redirect
from .models import *
from .forms import CommentForm
# Create your views here.
import random

def home(request):
    comments = list(Comment.objects.all())  # Convert queryset to list
    random.shuffle(comments)  # Shuffle the list
    return render(request, 'index.html', {'comments': comments})
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
