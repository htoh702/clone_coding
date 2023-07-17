Instagram clone_coding
======================

## 프로젝트 설명:

이 프로젝트는 기존에 있는 인스타그램을 클론 코딩하여 재구성하는 것을 목표로 합니다. Django 웹 프레임워크를 사용하여 웹 애플리케이션을 개발하고, 사용자 계정 관리와 각 계정의 정보를 저장하는데 MySQL 데이터베이스를 이용합니다.

## 프로젝트 개요:

이 프로젝트는 인스타그램의 주요 기능을 재현하는 웹 애플리케이션을 만드는 것입니다. 사용자들은 가입하여 계정을 생성하고, 로그인하여 자신의 프로필을 구성하고 사진을 업로드하며, 다른 사용자들과 소셜 네트워크의 형식으로 상호작용할 수 있습니다.

## 기술 스택:

Django 웹 프레임워크: Python 기반 웹 프레임워크로, 웹 서버 개발을 쉽게 할 수 있도록 도와줍니다.
MySQL 데이터베이스: 사용자 계정과 프로필 정보를 저장하는 데 사용됩니다.
HTML, CSS, JavaScript: 프론트엔드 개발을 위한 기술들로, 사용자 인터페이스를 구현하는데 사용됩니다.

## 기능 목록:

사용자 등록과 로그인 기능: 사용자는 이메일과 비밀번호로 가입하고 로그인할 수 있습니다.
프로필 관리: 사용자는 자신의 프로필을 업데이트하고 사진을 업로드할 수 있습니다.
게시물 업로드: 사용자는 사진과 캡션을 첨부하여 게시물을 업로드할 수 있습니다.
소셜 기능: 사용자는 다른 사용자의 게시물에 좋아요를 누르고 댓글을 남길 수 있습니다.

## Django에서 HTML 파일과 요청 처리:

Django는 MTV(Model-Template-View) 패턴을 사용하여 HTML 파일과 요청을 처리합니다. Model은 데이터를 관리하는 부분, Template은 프론트엔드 인터페이스를 구성하는 부분, View는 사용자의 요청을 처리하고 데이터와 템플릿을 결합하여 응답을 생성하는 부분입니다.

## MySQL 데이터베이스:

MySQL 데이터베이스는 Django의 모델(Model)을 사용하여 사용자 계정 정보와 프로필 정보를 저장하는 데 사용됩니다. 사용자가 회원 가입하면 계정 정보가 MySQL 데이터베이스에 저장되며, 사용자가 프로필을 업데이트하거나 사진을 업로드할 때 프로필 정보와 게시물 정보가 해당 테이블에 저장됩니다.

***

## 프로젝트 구성

1. 프로젝트 실행

Djnago 개발 서버를 실행하여 MySQL 데이터베이스와 함께 프로젝트를 테스트 합니다.

```
> python manage.py runserver
```

- 터미널에 위의 코드를 입력하고 서벌르 실행합니다.


***

2. 계정 생성

<img width="2056" alt="start_screen" src="https://github.com/htoh702/clone_coding/assets/79206548/4a37f452-a16c-449c-ab4f-3809dfb13dcd">

     
- 해당 프로젝트를 실행하면 처음 접하게 되는 초기 화면입니다. 계정이 없을 시 "가입히가" 버튼을 누르면 가입 화면으로 이동할 수 있습니다.
     

<img width="2056" alt="screen1" src="https://github.com/htoh702/clone_coding/assets/79206548/918916f2-25c1-499d-9989-afa003880243">
     

- 메일 주소, 성명, 사용자 이름, 비밀번호를 입력하고, 계정을 입력하면 계정을 생성할 수 있습니다.

     
<img width="1321" alt="databse" src="https://github.com/htoh702/clone_coding/assets/79206548/fdce0a1d-eeaf-407a-9804-d4624934b21d">
     

- MySQL에서 성공적으로 데이터가 생성된 것을 확인할 수 있습니다.
     

***

3. 게시물 업로드

<img width="2056" alt="screen2" src="https://github.com/htoh702/clone_coding/assets/79206548/764483b2-de1b-4e5d-a384-8bd246b1cd66">

- 계정을 생성하여 들어가게 되면 처음 접하게 되는 홈화면입니다. 상단 "+" 이미지 버튼 박스를 누르게 되면 업로드를 하기 위한 과정이 실행됩니다.

<img width="2056" alt="upload_screen1" src="https://github.com/htoh702/clone_coding/assets/79206548/3431c2a5-b304-4471-9a8e-5c3c6d22cac3">

- 업로드 하고자 하는 이미지를 화면에 띄어진 새로운 창안으로 드래그하여 옮겨 넣으면 이미지 업로드가 실행됩니다.

<img width="2055" alt="upload_screen2" src="https://github.com/htoh702/clone_coding/assets/79206548/eb56e5d3-6405-4365-9dfc-e9f8e04d833f">

- 이미지 업로드가 끝나면 게시물을 설명하는 입력란이 나오며 게시글 작성이 끝나면 "공유하기" 버튼을 누르면 게시물 업로드가 실행됩니다.

<img width="2056" alt="screen3" src="https://github.com/htoh702/clone_coding/assets/79206548/88868793-6957-4da8-aca1-3086d07f0ef5">

- 새로운 게시물이 성공적으로 올라온 것을 확인할 수 있습니다.

<img width="585" alt="screen4" src="https://github.com/htoh702/clone_coding/assets/79206548/2bca818a-8f7f-4e89-ab41-e55d6d42f409">

- 게시물에 댓글을 남길 수 있으며, 계정에 따라 구분이 되고 있는 것을 확인할 수 있습니다.

***

4. 프로필 변경

<img width="471" alt="profile3" src="https://github.com/htoh702/clone_coding/assets/79206548/59236774-6595-4e3c-817e-716f04c9fb37">

- 상단 우측 계정 이미지를 누르면 2가지의 항목을 확인할 수 있으며, 각 항목은 프로필을 변경하는 기능과 로그아웃 기능을 가지고 있습니다.

<img width="2056" alt="profile" src="https://github.com/htoh702/clone_coding/assets/79206548/f0fcfd24-85b6-4a1a-abc5-2c1508ffa1b3">

- 프로파일을 변경하기 위한 마이페이지로 이동후 "편집하기" 버튼을 누르면 이미지를 업로드 할 수 있습니다.

<img width="2056" alt="profile2" src="https://github.com/htoh702/clone_coding/assets/79206548/9c4d0f12-b777-4dad-ade2-fdc98e11e56b">

- 성공적으로 프로필이 변경된 것을 확인할 수 있습니다.
