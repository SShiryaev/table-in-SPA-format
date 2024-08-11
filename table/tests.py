from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from table.models import TableEntry


class TableTestCase(APITestCase):

    def setUp(self):
        self.table = TableEntry.objects.create(
            date=datetime.now().date(),
            name='test0',
            quantity=0,
            distance=0.0
        )

    def test_table_retrieve(self):
        url = reverse('table:table-detail', args=(self.table.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('date'), self.table.date.strftime('%Y-%m-%d')
        )

    def test_table_create(self):
        url = reverse('table:table-list')
        new_data = {
            "date": "2022-02-24",
            "name": "test1",
            "quantity": 1,
            "distance": 0.1
        }
        response = self.client.post(url, new_data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            TableEntry.objects.all().count(), 2
        )

    def test_table_update(self):
        url = reverse('table:table-detail', args=(self.table.pk,))
        new_data = {
            "name": "something_bad",
        }
        response = self.client.patch(url, new_data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'something_bad'
        )

    def test_table_delete(self):
        url = reverse('table:table-detail', args=(self.table.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            TableEntry.objects.all().count(), 0
        )

    def test_table_list(self):
        url = reverse('table:table-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.table.pk,
                        'date': self.table.date.strftime('%Y-%m-%d'),
                        'name': self.table.name,
                        'quantity': self.table.quantity,
                        'distance': self.table.distance
                    }
                ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data, result)
