"""chatapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authentication import views as aviews
from django.contrib.auth import views as auth_views
from chat import views as cviews
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',aviews.starting,name='starting'),
    path('register',aviews.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name="authentication/login.html"),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name="chat/logout.html"),name='logout'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='authentication/login.html')),
    path('profile',cviews.profile,name='profile'),
    path('search',cviews.search_users,name='search'),
    path('publicroom/',cviews.home,name='home'),
    path('<str:room>/',cviews.room,name='room'),
    path('privatechat/<str:room>/<str:chattinguser>/',cviews.privateroom,name='privateroom'),
    path('deletemessages/<int:roomid>/',cviews.MessageListView.as_view(template_name='chat/message_list.html'),name='deletemessages'),
    path('deletemessages/<int:roomid>/<int:pk>/',cviews.MessageDeleteView.as_view(template_name='chat/message_delete.html'),name='messagedelete'),
     path('privatecheckview',cviews.privatecheckview,name='privatecheckview'),
    path('publicroom/checkview',cviews.checkview,name='checkview'),
    path('send',cviews.send,name='send'),
    path('getMessages/<str:room>/',cviews.getMessages,name='getMessages'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('captcha/',include('captcha.urls')),
]

# style='float: right;'
