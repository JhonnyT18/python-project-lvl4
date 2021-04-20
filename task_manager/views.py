from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    context = {
        'welcome': _('Welcome to Task Manager!')
    }
    return render(request, 'task_manager/index.html', context)
