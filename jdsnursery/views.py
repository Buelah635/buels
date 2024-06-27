from django.shortcuts import render
from django.http import HttpResponse
from . forms import ContactForm

# Create your views here.
def home(request):
	return render(request,'jdsnursery/home.html')

def contact(request):
	form = ContactForm()
	return render(request,'jdsnursery/contact.html',{"form":form})
def learn(request):
	return render(request,'jdsnursery/includes/learn.html')

def evaluate(request):
	return render(request,'jdsnursery/evaluate.html')	