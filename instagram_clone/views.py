from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from rest_framework.response import Response
import os
from djangoProject.settings import MEDIA_ROOT
from uuid import uuid4
from user.models import User
from django.contrib.auth.hashers import check_password


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # select * from instagram_clone_feed;//query
        # .order_by('-id') id를 역순으로 가져온다

        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        for feed in feed_list:
            print(feed.content)

        return render(request, 'instagram_clone/Main.html', context=dict(feed=feed_list, user=user))  # 3번째 인자는 데이터가 사용될 때 작성한다.(댁셔너리로 작성)

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email is None:
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다'))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다'))

        request.session['loginCheck'] = True
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인에 성공했습니다'))


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex     # random 으로 이름을 생성
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)     # 성공을 의미하는 200


class Profile(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # select * from instagram_clone_feed;//query
        # .order_by('-id') id를 역순으로 가져온다

        email = request.session.get('email', None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'user/login.html')

        for feed in feed_list:
            print(feed.content)

        return render(request, 'instagram_clone/profile.html', context=dict(feed=feed_list, user=user))  # 3번째 인자는 데이터가 사용될 때 작성한다.(댁셔너리로 작성)


# Create your views here.
