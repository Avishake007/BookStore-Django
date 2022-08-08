from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from myapp.models import BookSchema
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import cloudinary


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        (allBooks,noOfBooks) =  viewBooks(request)
        return render(request, "index.htm", {"books" : allBooks,"noOfBooks" : noOfBooks})


def addBook(request):
    if request.user.is_anonymous:
        
        return redirect("/login")
    else:
       if(request.method == "POST"):
            book_img = request.FILES.get("book_img")
            name= request.POST.get("name")
            author = request.POST.get("author")
            price = request.POST.get("price")
            description = request.POST.get("description")
            book = BookSchema(book_img = book_img,name=name, author=author, price=price, description =description, userId = request.user.id, date=datetime.today())
            book.save()
            messages.success(request, 'Book added successfully!!')
            return redirect("/")
             # user = User(request.POST)
            # user.save()
    return render(request, "book/addBook.htm")
    #return HttpResponse("About Page")

def viewBooks(request):
    allBooks =  BookSchema.objects.all
    noOfBooks = BookSchema.objects.count()

    if request.method == "POST":
        author = request.POST.get("author")

        if author == "":
            allBooks = BookSchema.objects.all
        else:
            allBooks = BookSchema.objects.filter(author = author)
            noOfBooks = allBooks.count()
        
    return (allBooks, noOfBooks)

def viewBook(request, pk):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        book = BookSchema.objects.get(id=pk)
        if request.method == "POST":
            if book.inCart == True:
                book.inCart = False
            else:
                book.inCart = True
            book.save()
    return render(request, "book/viewBook.htm",{"book":book})

def updateBook(request, pk):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        book = BookSchema.objects.get(id=pk)
        
        if request.method == "POST":
            if request.FILES.get("book_img") != None:
                book.book_img= request.FILES.get("book_img")
            book.name= request.POST.get("name")
            book.author = request.POST.get("author")
            book.price = request.POST.get("price")
            book.description = request.POST.get("description")
            book.save()
            messages.success(request, 'Book updated successfully!!')
            return redirect("/viewBook/"+str(book.id))
    return render(request,"book/updateBook.htm",{"book":book})

def deleteBook(request, pk):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        book = BookSchema.objects.get(id=pk)
        if request.method == "POST":
            book.delete()
            messages.success(request, 'Book deleted successfully!!')
            return redirect("/")
    return render(request,"book/deleteBook.htm",{"book":book})

def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'User registered successfully!!')
        return redirect("/login")
    return render(request, "user/register.htm")

def loginUser(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull !!')
            return redirect("/")
        else:
            messages.warning(request, 'Invalid credentials !!')
            return render(request, "login.htm")
    else:
        return render(request, "user/login.htm")

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout Sucessfull!!')
    return redirect("/login")