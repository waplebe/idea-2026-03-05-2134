# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It allows users to create, read, update, and delete tasks. The frontend provides a basic interface for interacting with the API.

**Why it's useful:**

A task manager is a fundamental tool for productivity. This API provides a foundation for building more complex task management applications or integrating task management functionality into existing systems. It's a good example of a simple, self-contained web service.

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    *   Create a `.env` file in the root directory and populate it with the following environment variables:
        ```
        DATABASE_URL=sqlite:///tasks.db
        ```
    *   Run the backend server:
        ```bash
        python app.py
        ```
        (or `node server.js` or `go run main.go` depending on the backend language)

3.  **Set up the frontend:**
    *   Open `index.html` in your web browser.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `PUT /tasks/{id}`: Updates an existing task by ID. Request body should be a JSON object with the fields to update.
*   `DELETE /tasks/{id}`: Deletes a task by ID.

**Example Usage:**

*   **Create a task:**
    `POST /tasks`
    Request Body:
    ```json
    {
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread",
      "completed": false
    }
    ```

*   **Get all tasks:**
    `GET /tasks`
    Response:
    ```json
    [
      {
        "id": 1,
        "title": "Grocery Shopping",
        "description": "Buy milk, eggs, and bread",
        "completed": false
      }
    ]
    ```

**Testing:**

This project includes basic unit tests to ensure the API endpoints function correctly.  To run the tests:

```bash
python -m unittest discover tests
```

The `tests` directory contains test files for each API endpoint.

**Improvements:**

*   **Error Handling:**  More robust error handling is implemented, returning appropriate HTTP status codes and error messages for invalid requests.
*   **Data Validation:** Added basic data validation to ensure that required fields (like `title`) are present in POST requests.
*   **JSON Serialization:** Added a `to_dict()` method to the `Task` model for easier JSON serialization.
*   **Environment Variable Loading:**  Uses `python-dotenv` to load environment variables from a `.env` file, making the application more configurable.
*   **Documentation:** Updated the README to include information about testing and improvements.

**License:**

MIT License