from django.test import TestCase, RequestFactory


class ViewMixinTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def get(self, view, url):
        request = self.factory.get(url)
        response = view.as_view()(request)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
