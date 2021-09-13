from django.test import SimpleTestCase
from dashboard.forms import CreateRoomForm

class RegistrationTests(SimpleTestCase):
    def test_create_room_form_is_valid(self):
        form = CreateRoomForm(data={
            'name': 'room'
        })

        self.assertTrue(form.is_valid())

    def test_create_room_form_is_valid(self):
        form = CreateRoomForm(data={
            'name': '_room'
        })

        self.assertFalse(form.is_valid())
