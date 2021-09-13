from django.test import TestCase, Client
from django.urls import reverse

class RegistrationTests(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_signUp_view_POST(self):
        response = self.client.post(reverse('signUp'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signUp.html')
        
class DashboardTests(TestCase):
    def test_models_fields(self):
        pass