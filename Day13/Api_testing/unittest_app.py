import unittest
import app as app_module   # Access module-level variables
from app import app


class TaskAPITestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

        # Reset global state before each test
        app_module.tasks.clear()
        app_module.current_id = 1


    # -----------------------
    # Functional Tests
    # -----------------------

    def test_create_task(self):
        response = self.client.post(
            "/api/tasks",
            json={"title": "Learn Testing"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["title"], "Learn Testing")


    def test_get_all_tasks(self):
        self.client.post("/api/tasks", json={"title": "Task 1"})
        response = self.client.get("/api/tasks")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)


    def test_update_task(self):
        self.client.post("/api/tasks", json={"title": "Task 1"})

        response = self.client.put(
            "/api/tasks/1",
            json={"completed": True}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["completed"])


    def test_delete_task(self):
        self.client.post("/api/tasks", json={"title": "Task 1"})
        response = self.client.delete("/api/tasks/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Task deleted"})


    # -----------------------
    # Negative Tests
    # -----------------------

    def test_create_without_title(self):
        response = self.client.post(
            "/api/tasks",
            json={"description": "No title"}
        )
        self.assertEqual(response.status_code, 400)


    def test_get_non_existing_task(self):
        response = self.client.get("/api/tasks/999")
        self.assertEqual(response.status_code, 404)


    def test_update_non_existing_task(self):
        response = self.client.put(
            "/api/tasks/999",
            json={"title": "Updated"}
        )
        self.assertEqual(response.status_code, 404)


    def test_invalid_data_type(self):
        response = self.client.post(
            "/api/tasks",
            json={"title": "Test", "completed": "yes"}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
