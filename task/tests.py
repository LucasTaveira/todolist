from rest_framework.test import APIClient
from django.test import TestCase
from unittest.mock import patch, MagicMock

from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = MagicMock(spec=Task)
        self.task.id = 1
        self.task.title = 'Task 1'
        self.task.description = 'Description 1'
        self.task.status = 'o'
        
    @patch('todolist.task.views.Task.objects.all')    
    def test_task_list(self, mock_objects_all):
        mock_objects_all.return_value = [self.task]
        
        response = self.client.get('/api/v1/task/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'Task 1')
        self.assertEqual(response.data[0]['description'], 'Description 1')
        
    @patch('todolist.task.views.Task.objects.get')    
    def test_task_create(self, mock_objects_get):
        mock_objects_get.return_value = self.task
        
        response = self.client.post('/api/v1/task/', 
            {'title': 'Task 2', 'description': 'Description 2', 'status':'c'}, 
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(mock_objects_get.call_count, 1)
        
    @patch('todolist.task.views.Task.objects.get')
    def test_task_update(self, mock_objects_get):
        mock_objects_get.return_value = self.task
        
        response = self.client.put(f'/api/v1/task/{self.task.id}/', 
            {'title': 'Task 1 Updated', 'description': 'Description 1 Updated'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_objects_get.call_count, 1)

    @patch('todolist.task.views.Task.objects.get')
    def test_task_delete(self, mock_objects_get):
        mock_objects_get.return_value = self.task
        
        self.client.delete(f'/api/v1/task/{self.task.id}/')
        self.assertEqual(mock_objects_get.call_count, 1)
        self.assertEqual(mock_objects_get.return_value.delete.call_count, 1)
