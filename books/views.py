from django.shortcuts import render, get_object_or_404
from .models import Books

def all_bookss(request):
    bookss=Books.objects.order_by('-date')
    return render(request,'books/all_bookss.html',{'bookss':bookss})
# Create your views here.
def detail(request,books_id):
    books= get_object_or_404(Books,pk=books_id)
    return render(request,'books/detail.html',{'books':books})
