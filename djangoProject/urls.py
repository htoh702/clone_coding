"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import instagram_clone.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', instagram_clone.views.Main.as_view(), name='main'),
    path('content/upload', instagram_clone.views.UploadFeed.as_view()),
    path('content/reply', instagram_clone.views.UploadReply.as_view()),
    path('content/like', instagram_clone.views.ToggleLike.as_view()),
    path('content/bookmark', instagram_clone.views.CheckBookmark.as_view()),
    path('', user.views.Login.as_view(), name='login'),
    path('join', user.views.Join.as_view(), name='join'),
    path('logout', user.views.LogOut.as_view(), name='logout'),
    path('profile', instagram_clone.views.Profile.as_view()),
    path('profile/upload', user.views.UploadProfile.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # media 파일을 조회하기 위한 코드
