from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Treatise, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.treatise = Treatise.objects.create(name='test', description='test_d')
        self.user = User.objects.create(email='kolya.tarasov1@mail.com', username='kuzon12', password='pass1')
        self.user_ = User.objects.create(email='kolya.tarasov2@mail.com', username='kuzon2', password='pass2')
        self.lesson = Lesson.objects.create(name='test_', link_to_video='youtube.com', treatise=self.treatise,
                                            description='tests_description', owner=self.user_)
        self.client.force_authenticate(user=self.user)
        self.client.force_authenticate(user=self.user_)

    def test_create_lesson(self):
        """ Тестирование создание урока """

        data = {
            'name': 'test',
            'link_to_video': 'youtube.com',
            'treatise': 1,
            'description': 'test_description',
            'owner': 1,
        }
        response = self.client.post(
            '/lesson_create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_retrieve_lesson(self):
        """ Тестирование существования вывода отдельного урока"""
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'),
            self.lesson.name
        )

    def test_update_lesson(self):
        """ Тестирование изменения урока"""
        data = {
            'name': 'test_update',
        }
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        response = self.client.patch(url)
        data_ = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'),
            'test_update'
        )

    def test_destroy_lesson(self):
        """ Тестирование удаления урока """
        url = reverse("materials:lesson_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )
