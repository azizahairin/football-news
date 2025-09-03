from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406438504',
        'name': 'Azizah Khairinniswah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)