from django.shortcuts import render


def index(request):
    context = {
        "title": "Dashboard",
    }
    return render(request, "app/index.html", context)


def posts(request):
    context = {
        "title": "Posts Page"
    }
    return render(request, "app/posts.html", context)


def categories(request):
    context = {
        "title": "Categories Page"
    }
    return render(request, "app/categories.html", context)


def comments(request):
    context = {
        "title": "Comments Page"
    }
    return render(request, "app/comments.html", context)


def users(request):
    context = {
        "title": "Users Page"
    }
    return render(request, "app/users.html", context)


def test(request):
    context = {
        "title": "Testing Page"
    }
    return render(request, "app/test.html", context)
