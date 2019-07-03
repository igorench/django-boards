# this file is used to write unit tests for the app
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home, board_topics, new_topic
from ..forms import NewTopicForm
from ..models import Board, Topic, Post
from ..views import BoardListView


class HomeTests(TestCase):
    # Observe that now we added a setUp method for the HomeTests as well. That's
    # because now we are going to need a Board instance and also we moved the
    # url and responce to the setUp, so we can reuse the same responce in the
    # new test.
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.')
        url = reverse('home')
        self.responce = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.responce.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse(
            'board_topics', kwargs={'pk': self.board.pk})
        # We are testing if the responce body has the text href="/boards/1/"
        self.assertContains(
            self.responce, 'href="{0}"'.format(board_topics_url))
