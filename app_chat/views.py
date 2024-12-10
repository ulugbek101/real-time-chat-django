from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, "app_chat/home_page.html", context)
