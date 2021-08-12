from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):

    model = User
    form_class = BaseRegisterForm
    success_url = '/login/'


@login_required
def upgrade(request):
    user = request.user
    authors_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
