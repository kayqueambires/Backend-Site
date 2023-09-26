from django.shortcuts import render
from .models import Post
import requests
import json
from django.shortcuts import redirect

def home(request):
    return redirect('visualization')


def fetch_data(request):
    if not Post.objects.exists():
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            data = json.loads(response.text)
            for item in data:
                post = Post(userId=item['userId'], title=item['title'], body=item['body'])
                post.save()
            return redirect('display_data') 
        else:
            return render(request, 'fetch_data.html', {'message': 'Error to find API data'})
    else:
        return redirect('display_data')

def display_data(request):
    posts = Post.objects.all()
    return render(request, 'display_data.html', {'posts': posts})

def visualization(request):
    return render(request, 'visualization.html')


