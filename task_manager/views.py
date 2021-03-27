from django.shortcuts import render


def index(request):
    context = {
        'who': 'Bro',
    }
    return render(request, 'task_manager/index.html', context)
