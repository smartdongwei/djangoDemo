from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'bookName' in request.GET :
        bookName = request.GET['bookName']
        if not bookName:
            error = True
        else:
            books = Book.objects.filter(title__icontains = bookName )
            return render_to_response('search_result.html',{'books':books,'query':bookName})

    return render_to_response('search_form.html',{'error': error})