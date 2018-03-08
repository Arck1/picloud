from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
    path('robots.txt/', views.robots, name='robots'),

    path('auth/signup/', views.signup, name="signup"),
    path('auth/signin/', views.signin, name="signin"),
    path('auth/signout/', views.signout, name="signout"),
    path('activate/<uid>/<token>/', views.activate, name='activate'),

    # auth встроенное приложение, сброс пароля, переопределяющие шаблоны в registration/*
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    re_path(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    re_path(r'post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    re_path(r'post/(?P<pk>\d+)/checked/$', views.post_checked, name='post_checked'),

    path('user/<user_id>', views.user_page, name='user_page'),
    path('user/<user_id>/posts', views.user_posts, name='user_posts'),

    path('search/', views.search, name="search"),
    path('memes/', views.memes, name="memes"),
    path('settings/', views.settings, name="settings"),
    path('message/', views.message, name="message"),
    path('validation/', views.validation, name="validation"),
    path('change_password/', views.change_password, name='change_password'),
    path('change_avatar/', views.change_avatar, name='change_avatar'),
    path('change_user/', views.change_user, name='change_user'),
    path('universities/', views.universities_list, name='universities_list'),
    path('universities/<university_id>/', views.university_page, name='university_page'),
    path('program/<program_id>', views.program_page, name='program_page'),
    path('subject/<subject_id>', views.subject_page, name='subject_page'),
    path('contacts', views.contacts, name='contacts'),

    path('get_universities/', views.get_universities, name='get_universities'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_chairs/', views.get_chairs, name='get_chairs'),
    path('get_programs/', views.get_programs, name='get_programs'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
    path('get_posts/', views.get_posts, name='get_posts'),
    path('search_posts/', views.search_posts, name='search_posts'),
]
