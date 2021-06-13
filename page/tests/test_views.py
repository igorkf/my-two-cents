from django.test import TestCase

# Create your tests here.


class IndexViewTest(TestCase):
    def test_if_url_exists_at_desired_location(self):
        response = self.client.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertTemplateUsed(response, 'page/index.html')

    def test_if_url_uses_corret_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'page/index.html')
