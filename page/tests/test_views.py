from django.test import TestCase, RequestFactory

from .. import views

# Create your tests here.


# TODO: write mixin


class IndexViewTest(TestCase):
    url = '/'
    template_name = 'page/index.html'

    def test_if_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_if_url_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, self.template_name)


class WhoAmIViewTest(TestCase):
    url = '/who-am-i'

    def test_if_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class PostsViewTest(TestCase):
    url = '/posts'
    template_name = 'page/posts.html'

    def test_if_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_if_url_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, self.template_name)

    def test_if_posts_is_in_context(self):
        request = RequestFactory().get(self.url)
        view = views.PostsView()
        view.setup(request)

        view.object_list = view.get_queryset()
        context = view.get_context_data()

        self.assertIn('posts', context)


class ProjectsViewTest(TestCase):
    url = '/projects'

    def test_if_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
