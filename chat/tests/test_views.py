from django.test import TestCase, Client
from django.urls import reverse
from dashboard.models import Room

class RegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signUp_view_POST(self):
        response = self.client.post(reverse('signUp'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signUp.html')

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username='user', password='123')

    def test_dashboard_view_GET(self):
        response = self.client.get(reverse('rooms'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/rooms/home.html')

    def test_dashboard_view_without_rooms_OST(self):
        response = self.client.post(reverse('rooms'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/rooms/home.html')

    def test_dashboard_view_with_POST(self):
        room = Room()
        room.name = '<room_name>'
        room.save()

        response = self.client.post(reverse('rooms'), {'room_button': '<room_name>'})

        self.assertEquals(response.status_code, 302)
