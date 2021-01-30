from django.shortcuts import render

# Create your views here.
def homePage(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    
    return render(request, 'homepage.html', context)

def postPage(request, pk):
    quantitytotal = data['quantitytotal']
    post = get_object_or_404(Post, pk=pk)
    context = {'post':post}
    
    return render(request, 'postpage.html', context)