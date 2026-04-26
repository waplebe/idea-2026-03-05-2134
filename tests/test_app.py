import unittest
from unittest.mock import patch
from app import app, db
from models import Task

class TestApp(unittest.TestCase):

    @patch('app.db')
    def setUp(self, mock_db):
        app.config['TESTING'] = True
        db.init_app(app)
        mock_db.return_value = MockSQLAlchemy(app)

    @patch('app.db')
    def test_get_tasks(self, mock_db):
        tasks = [
            Task(id=1, title="Task 1", description="Description 1", completed=False),
            Task(id=2, title="Task 2", description="Description 2", completed=True)
        ]
        mock_db.query.all.return_value = tasks
        response = app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), tasks)

    @patch('app.db')
    def test_get_task(self, mock_db):
        task = Task(id=1, title="Task 1", description="Description 1", completed=False)
        mock_db.query.get_or_404.return_value = task
        response = app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), task.to_dict())

    @patch('app.db')
    def test_create_task(self, mock_db):
        data = {'title': 'New Task', 'description': 'New Description'}
        response = app.post('/tasks', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), data)

    @patch('app.db')
    def test_update_task(self, mock_db):
        task = Task(id=1, title="Task 1", description="Description 1", completed=False)
        mock_db.query.get_or_404.return_value = task
        data = {'title': 'Updated Task'}
        response = app.put('/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), task.to_dict())

    @patch('app.db')
    def test_delete_task(self, mock_db):
        task = Task(id=1, title="Task 1", description="Description 1", completed=False)
        mock_db.query.get_or_404.return_value = task
        response = app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Task deleted'})

class MockSQLAlchemy(object):
    def __init__(self, app):
        self.app = app
        self.session = {}

    def create_all(self):
        pass

    def query(self, model):
        return self

    def commit(self):
        pass

    def delete(self, model):
        pass

if __name__ == '__main__':
    unittest.main()