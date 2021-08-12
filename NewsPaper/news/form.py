from django.forms import ModelForm, BooleanField
from .models import Post
from allauth.account.forms import SignupForm, EmailAddress
from django.contrib.auth.models import Group



# Создаём модельную форму
class PostForm(ModelForm):
    check_box = BooleanField(label='Yes')  # добавляем галочку, или же true-false поле
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля.
    class Meta:
        model = Post
        fields = ['title', 'author', 'postCategory', 'text', 'check_box']

class CommonSignup(SignupForm):
    def save(self, request):

        user = super(CommonSignup, self).save(request)
        common_group = Group.objects.get(name='Common')
        common_group.user_set.add(user)
        return user