from django.shortcuts import render

#dummy post
posts = [
    {   'author': 'Nahid',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date': 'December 23, 2022'   
    },
    {   'author': 'Ashiq',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date': 'December 24, 2022'   
    }
]

# Create your views here.
def homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'}) 

