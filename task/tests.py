from django.test import TestCase, Client
from model_bakery import baker

from task.models import Task

class TestTask(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.task = baker.make(Task,
            id=1,
            title='Task 1',
            description='Description 1',
            status='o'
        )
        self.url_base = '/api/v1/task/'
        self.content_type = 'application/json'
    
    def test_task_list(self):
        url = self.url_base
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'Task 1')
        self.assertEqual(response.data[0]['description'], 'Description 1')

    def test_task_create(self):
        url = self.url_base
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'O'
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(title='Test Task').exists())

    def test_task_update(self):
        url_task = self.url_base
        response_task = self.client.get(url_task)
        task_to_update = response_task.data[0]['id']
        
        url_update = f'{self.url_base}{task_to_update}/'
        data = {
            'title': 'Task 1 Updated',
            'description': 'Description 1 Updated',
            'status': 'O'
        }
        response = self.client.put(url_update, data, self.content_type)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title='Task 1 Updated').exists())

    def test_task_delete(self):
        task = baker.make(Task)
        url = f'{self.url_base}{task.id}/'
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(id=task.id).exists())