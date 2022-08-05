from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HompePageTests(SimpleTestCase):
    def test_url_response(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_url_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutPageTests(SimpleTestCase):
    def test_url_response(self):
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)
    
    def test_url_name(self):
        res = self.client.get(reverse('about'))
        self.assertEqual(res.status_code, 200)

    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")

        