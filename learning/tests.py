from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountAuthenticationTests(TestCase):
    password = 'River!Notebook!84-Sky'

    def test_signup_creates_account_signs_user_in_and_shows_username(self):
        response = self.client.post(reverse('signup'), {
            'username': 'curious_student',
            'password1': self.password,
            'password2': self.password,
        })

        self.assertRedirects(response, reverse('home'))
        self.assertTrue(
            get_user_model().objects.filter(username='curious_student').exists()
        )
        self.assertContains(
            self.client.get(reverse('home')),
            '<strong>curious_student</strong>',
        )

    def test_signup_rejects_mismatched_passwords(self):
        response = self.client.post(reverse('signup'), {
            'username': 'curious_student',
            'password1': self.password,
            'password2': 'a-different-password',
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            get_user_model().objects.filter(username='curious_student').exists()
        )

    def test_login_accepts_valid_credentials(self):
        get_user_model().objects.create_user(
            username='returning_student',
            password=self.password,
        )

        response = self.client.post(reverse('login'), {
            'username': 'returning_student',
            'password': self.password,
        })

        self.assertRedirects(response, reverse('home'))
        self.assertContains(
            self.client.get(reverse('home')),
            '<strong>returning_student</strong>',
        )

    def test_login_rejects_incorrect_password(self):
        get_user_model().objects.create_user(
            username='returning_student',
            password=self.password,
        )

        response = self.client.post(reverse('login'), {
            'username': 'returning_student',
            'password': 'incorrect-password',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(self.client.get(reverse('home')), 'Log in')
        self.assertNotContains(
            self.client.get(reverse('home')),
            'returning_student',
        )

    def test_logout_ends_session_and_returns_home(self):
        get_user_model().objects.create_user(
            username='leaving_student',
            password=self.password,
        )
        self.client.login(username='leaving_student', password=self.password)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('home'))
        self.assertContains(self.client.get(reverse('home')), 'Sign up')
        self.assertNotContains(
            self.client.get(reverse('home')),
            'leaving_student',
        )

    def test_login_and_signup_pages_load(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
        self.assertEqual(self.client.get(reverse('signup')).status_code, 200)
