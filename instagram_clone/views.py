from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from rest_framework.response import Response
import os
from djangoProject.settings import MEDIA_ROOT
from uuid import uuid4


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # select * from instagram_clone_feed;//query
        # .order_by('-id') id를 역순으로 가져온다
        for feed in feed_list:
            print(feed.content)

        return render(request, 'instagram_clone/Main.html', context=dict(feed=feed_list))  # 3번째 인자는 데이터가 사용될 때 작성한다.(댁셔너리로 작성)


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


# Create your views here.
