import os


# Django의 기본 유저가 INSTALLED_APPS -> django.contrib.auth에서 models의 user가 있으니까 불러온다
# 그래서 명시적으로 얘를 안불러온다라고 적어줘야 한다.
# 우리가 쓴 user를 앞으로 쓰겠다고 overriding을 해준다.

AUTH_USER_MODEL = "users.User"

# Login required decorator나 Login required Mixedin을 통해서 다른페이지로 이동이 됐을 때 로그인이라는 key로 받게 된다.
LOGIN_URL = '/login/'

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입 되었습니다."
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인 되었습니다."
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다."

INTERNAL_IPS = [
    '127.0.0.1',
]

LOGIN_REDIRECT_URL = '/login/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.github.GithubOAuth2',
    ]
SOCIAL_AUTH_GITHUB_KEY = os.environ.get("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get("SOCIAL_AUTH_GITHUB_SECRET")
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/login/'
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
]
