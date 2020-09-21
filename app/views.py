from django.shortcuts import render


def index(request):
    context = {
        "title": "Dashboard",
        "message": "From Dashboard Page"
    }
    return render(request, "app/index.html", context)


def posts(request):
    context = {
        "title": "Posts Page",
        "message": "From Posts Page"
    }
    return render(request, "app/posts.html", context)


def categories(request):
    context = {
        "title": "Categories Page",
        "message": "From Categories Page"
    }
    return render(request, "app/categories.html", context)


def comments(request):
    context = {
        "title": "Comments Page",
        "message": "From Comments Page"
    }
    return render(request, "app/comments.html", context)


def users(request):
    context = {
        "title": "Users Page",
        "message": "From Users Page"
    }
    return render(request, "app/users.html", context)


def test(request):
    context = {
        "title": "Testing Page",
        "message": "From testing Page"
    }
    return render(request, "app/test.html", context)


def login(request):
    context = {
        "title": "Login Page",
        "message": "From Login Page"
    }
    return render(request, "app/login.html", context)


def logout(request):
    context = {
        "title": "Logout Page",
        "message": "From Logout Page"
    }
    return render(request, "app/logout.html", context)


def details(request):
    context = {
        "title": "Details Page",
        "message": "From Details Page"
    }
    return render(request, "app/details.html", context)
