from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from httpx import get


class UsersAPITestCase(APITestCase):

    def setUp(self) -> None:

        self.client = APIClient()

        self.admin_user = User.objects.create_superuser(
            "DummyTest",
            "dummy_test@localhost.local",
            "ilovelongstrings"
        )

        self.client.login(
            username=self.admin_user.username,
            password=self.admin_user.password
        )

        self.users_url = reverse("users")

    def tearDown(self) -> None:
        self.client.logout()


class UsersTests(UsersAPITestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_user(self):
        url = self.users_url
        auth = (self.admin_user.username, self.admin_user.password)
        response = get(url, auth=auth)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
