from django.test import TestCase
from django.contrib.auth.models import User


class AuthorizationTestCase(TestCase):
    def setUp(self):
        admin = User(username='admin', password='admin', is_staff=True, is_superuser=True)
