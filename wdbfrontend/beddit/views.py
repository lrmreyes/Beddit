from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    
    return render(request, 'homepage.html', context)

def postpage(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post':post}
    
    return render(request, 'postpage.html', context)