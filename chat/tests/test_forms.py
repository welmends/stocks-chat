from django.test import SimpleTestCase, TestCase

from dashboard.forms import CreateRoomForm
from registration.forms import UserSignUpForm


class RegistrationTests(TestCase):
    def test_user_signUp_form_is_valid(self):
        form = UserSignUpForm(data={"username": "username", "password1": "passwd"})

        self.assertTrue(form.is_valid())

    def test_user_signUp_form_is_not_valid(self):
        form = UserSignUpForm(data={"username": "<username>", "password1": "<passwd>"})

        self.assertFalse(form.is_valid())


class DashboardTests(TestCase):
    def test_create_room_form_is_valid(self):
        form = CreateRoomForm(data={"name": "room"})

        self.assertTrue(form.is_valid())

    def test_create_room_form_is_not_valid(self):
        form = CreateRoomForm(data={"name": "_room"})

        self.assertFalse(form.is_valid())
