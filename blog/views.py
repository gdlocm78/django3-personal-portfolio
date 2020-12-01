from django.shortcuts import render,get_object_or_404
from .models  import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #[:5]  #Se indica que se mostraran los blogs con la fecha mas reciente y con [:5] se limita a que muestra los ultimos 5 blogs
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def details(request,blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    return render(request,'blog/details.html',{'blog':blog})
