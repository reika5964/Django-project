from django.shortcuts import render
from blogs.models import Blogs
from django.db.models import Sum

# Create your views here.
def panel(request):
    writer = "reika5964"
    blogs = Blogs.objects.filter(writer=writer)
    blogCount= blogs.count()
    total = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    return render(request,"backend/index.html",{"blogs":blogs,"writer":writer,"blogCount":blogCount,"total":total})
