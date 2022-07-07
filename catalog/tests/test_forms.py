from django.test import TestCase

from catalog.forms import AuthorCreationForm


class FormsTests(TestCase):
    def test_author_creation_form_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test First",
            "last_name": "Test Last",
            "pseudonym": "Test Pseudonym",
        }
        form = AuthorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
