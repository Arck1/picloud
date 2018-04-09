from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from cloud.forms import AvatarChangeForm, UserInfoChangeForm
from cloud.models import UserInfo, Post
from cloud.views.message import message
from cloud.views.posts import post_list


def user_page(request, user_id):
    if request.user.is_authenticated:
        fr_user = get_object_or_404(User, pk=user_id)
        fr_user_info = UserInfo.objects.get(user=fr_user)
        return render(request, 'user.html', locals())
    else:
        return message(request, msg="Авторизуйтесь, чтобы посещать страницы других пользователей.")


def user_posts(request, user_id):
    if request.user.is_authenticated:
        fr_user = User.objects.get(pk=user_id)
        fr_user_posts = Post.objects \
            .filter(author=fr_user) \
            .filter(approved=True) \
            .filter(created_date__lte=timezone.now()) \
            .order_by('created_date') \
            .reverse()
        return post_list(request, display_posts=fr_user_posts)
    else:
        return message(request, msg="Авторизуйтесь, чтобы просматривать посты конкретных пользователей.")


def user_not_checked_posts(request, user_id):
    if request.user.is_authenticated and int(user_id) == request.user.pk:
        user = User.objects.get(pk=user_id)
        not_validate_posts = Post.objects \
            .filter(author=user) \
            .filter(approved=False) \
            .filter(created_date__lte=timezone.now()) \
            .order_by('created_date') \
            .reverse()
        return post_list(request, display_posts=not_validate_posts)
    else:
        return message(request, msg="Вы можете просматривать только проверенные посты этого пользователя.")


def settings_page(request, msg="", error=""):
    change_avatar_form = AvatarChangeForm()
    change_password_form = PasswordChangeForm(request.user)
    change_user_form = UserChangeForm(instance=User.objects.get(pk=request.user.pk))
    change_user_info_form = UserInfoChangeForm(instance=UserInfo.objects.get(user=request.user))
    user = User.objects.get(pk=request.user.pk)
    user_info = UserInfo.objects.get(user=user)
    return render(request, 'settings.html', {
        'user': user,
        'user_info': user_info,
        'change_password_form': change_password_form,
        'change_avatar_form': change_avatar_form,
        'change_user_form': change_user_form,
        'change_user_info_form': change_user_info_form,
        'message': msg,
        'error': error,
    })


def change_avatar(request):
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST,
                                request.FILES,
                                instance=UserInfo.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            request.session['user_ava_url'] = UserInfo.objects.get(user=request.user).avatar.url
            return settings_page(request, msg="Аватар успешно изменен.")
        else:
            return settings_page(request, error="При изменении аватара произошла ошибка.")
    else:
        # не достижимый участок кода, только если на прямую обратиться по адресу
        return settings_page(request)


def change_user(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=User.objects.get(pk=request.user.pk))
        user_info_form = UserInfoChangeForm(request.POST, instance=UserInfo.objects.get(user=request.user))
        if user_form.is_valid() and validate_name(request.POST['first_name'], request.POST['last_name']):
            user_form.save()
        else:
            return settings_page(request, error="Ошибка при изменении данных. " +
                                                "Убедитесь, что длина полей «Имя» и «Фамилия» не превышает 20 символов")
        if user_info_form.is_valid() and validate_course(request.POST['course']):
            user_info_form.save()

            program = UserInfo.objects.get(user=request.user).program
            if program is not None:
                request.session['program_id'] = program.pk
            else:
                request.session['program_id'] = ""
        else:
            return settings_page(request, error="Ошибка при изменении данных. " +
                                                "Убедитесь, что поля «Программа обучения» и «Курс обучения» заполнены")
        return settings_page(request, msg="Данные успешно сохранены.")
    else:
        # недостижимый участок кода, только если на прямую обратиться по адресу
        return settings_page(request)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return settings_page(request, msg='Пароль успешно изменен.')
        else:
            return settings_page(request, error='Пароли введены с ошибкой.')
    else:
        # не достижимый участок кода, только если на прямую обратиться по адресу
        return settings_page(request, error='Пароль должен быть длиннее 8 символов.')


def validate_course(course):
    try:
        c = int(course)
        return 0 <= c <= 10
    except ValueError:
        return False


def validate_name(first_name, last_name):
    return len(first_name) < 20 and len(last_name) < 20
