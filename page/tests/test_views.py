from django.test import TestCase

# Create your tests here.


# TODO: write mixin


class IndexViewTest(TestCase):
    def test_if_url_exists_at_desired_location(self):
        response = self.client.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_if_url_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'page/index.html')


class WhoAmIViewTest(TestCase):
    def test_if_url_exists_at_desired_location(self):
        response = self.client.get('/who-am-i')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class PostsViewTest(TestCase):
    def test_if_url_exists_at_desired_location(self):
        response = self.client.get('/posts')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_if_url_uses_correct_template(self):
        response = self.client.get('/posts')
        self.assertTemplateUsed(response, 'page/posts.html')


class ProjectsViewTest(TestCase):
    def test_if_url_exists_at_desired_location(self):
        response = self.client.get('/projects')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
