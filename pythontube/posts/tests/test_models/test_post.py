from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostModelTestCase(TestCase):
    # 밑에 있는 모든 test case가 실행되지 이전에 실행이 되는 것
    def setUp(self):

        # Create a user
        self.user = get_user_model().objects.create_user(
            username='test_username',
            password='test_password',
        )

        # Create a post
        self.post_video_id = 'pythontube'
        self.post = self.user.post_set.create(
            video_id=self.post_video_id,
            title="test_title",
        )

    def test_post_model_should_have_youtube_original_url(self):
        """
        Post 모델은 가지고 있는 video_id를 이용해서,
        Youtube 원본 영상의 링크를 생성할 수 있어야 한다.
        """
        youtube_original_url = "https://www.youtube.com/watch?v={post_video_id}".format(
                post_video_id=self.post_video_id,
            )
        # get으로 시작하는 함수에 대한 test code
        self.assertEqual(
            self.post.get_youtube_original_url(),
            youtube_original_url,
        )

        # property에 대한 test code
        self.assertEqual(
            self.post.youtube_original_url,
            youtube_original_url,
        )
