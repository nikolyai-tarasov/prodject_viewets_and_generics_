

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Treatise, Lesson
from users.models import User



class SubsTestCase(APITestCase):
    def setUp(self):
        self.treatise = Treatise.objects.create(name='test', description='test_d')
        self.user = User.objects.create(email='kolya.tarasov1@mail.com', username='kuzon12', password='pass1')
        self.user_ = User.objects.create(email='kolya.tarasov2@mail.com', username='kuzon2', password='pass2')
        self.lesson = Lesson.objects.create(name='test_', link_to_video='youtube.com', treatise=self.treatise,
                                            description='tests_description', owner=self.user_)
        self.client.force_authenticate(user=self.user)
        self.client.force_authenticate(user=self.user_)

    def test_subs(self):
        """ Тестирование подписки на курс """
        data = {
            "user": self.user.pk,
            "treatise_id": self.treatise.pk,
        }
        url = reverse("users:subs", )
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json().get('message'),
            'Подписка добавлена'
        )
