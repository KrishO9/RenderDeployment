# pages/tests.py
from django.test import SimpleTestCase, Client
from django.urls import reverse

class PageViewTests(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_view_status_code(self):
        response = self.client.get(reverse('home_page')) # Use reverse for URL names
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_content(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, "<h1> Hello There </h1>", html=True)
        self.assertContains(response, "<p> Just the home page </p>", html=True)

    def test_greet_view_status_code(self):
        response = self.client.get(reverse('greet_user', args=['Alice']))
        self.assertEqual(response.status_code, 200)

    def test_greet_view_content_with_name(self):
        name = "Bob"
        response = self.client.get(reverse('greet_user', args=[name]))
        self.assertContains(response, f"<h1>Hello, {name}!</h1>", html=True)
        self.assertContains(response, "<p>Nice to meet you.</p>", html=True)

    def test_greet_view_content_with_different_name(self):
        name = "Charlie"
        response = self.client.get(reverse('greet_user', args=[name]))
        self.assertContains(response, f"<h1>Hello, {name}!</h1>", html=True)