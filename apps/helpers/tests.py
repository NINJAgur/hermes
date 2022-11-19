from django.test import TestCase

# Create your tests here.
class HelpersTestCase(TestCase):
    def test_wrong_uri_returns_404(self):
        response = self.client.get('/something/really/weird/')
        self.assertEqual(response.status_code, 404)

    def test_post_error(self):
        self.client.raise_request_exception = False
        response = self.client.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 500)