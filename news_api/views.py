from django.shortcuts import render
import requests
from .models import Post
API_KEY = '8a0608a18c264ff1a7fa9a85c1b56162'


# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    sources = request.GET.get('sources')
    q = request.GET.get('q')
    if request.method=='POST':
           if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
               post=Post()
               post.name=request.POST.get('name')
               post.email=request.POST.get('email')
               post.phone=request.POST.get('phone')
               post.message=request.POST.get('message')
               post.save()

               return render(request,'news_api/home.html')
  
    elif country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    
    elif q:
        url = f'https://newsapi.org/v2/top-headlines?q={q}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    

    else:

        url = f'https://newsapi.org/v2/top-headlines?sources={sources}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    

    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)
    

    




    
   

