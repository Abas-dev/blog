from django.shortcuts import render
from .models import Blogger,BlogDetails,Categories

# Create your views here.
def home(request):
    detail = BlogDetails.objects.all()
    context = {'detail':detail}
    return render(request, 'blog/index.html',context)

def details(request,id):
    detail = BlogDetails.objects.get(id=id)
    context = {'detail':detail}
    return render(request, 'blog/single.html',context)

