📘 Student API with FastAPI
This is a simple FastAPI application for managing student data using RESTful endpoints. It allows users to create, read, update, and delete student records stored in an in-memory dictionary.

🚀 Features
Retrieve student info by ID or name

Filter students by intake session

Create new student records

Update existing student details

Delete student entries

🧱 Built With
FastAPI - Web framework for building APIs with Python

Pydantic - Data validation and settings management using Python type hints

📦 How to Run
Install dependencies (preferably in a virtual environment):

bash
Copy
Edit
pip install fastapi uvicorn
Run the server:

bash
Copy
Edit
uvicorn main:app --reload
Replace main with the name of your Python file (without .py)

Open your browser and go to:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

📚 API Endpoints
Method	Endpoint	Description
GET	/	Welcome endpoint
GET	/student/{student_id}	Get student by ID
GET	/student_by_name?name={name}	Get student by name (query param)
GET	/student_by_intake/{student_id}	Get student by intake (query param)
POST	/create_student/{student_id}	Add a new student
PUT	/update_student/{student_id}	Update existing student
DELETE	/delete_student/{student_id}	Delete a student
📝 Notes
stdent and update_student are Pydantic models for validating student data.

The data is stored in a Python dictionary and will reset every time the server restarts.