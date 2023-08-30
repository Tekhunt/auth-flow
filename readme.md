# Auth flow - Backend

Visit `localhost:port/docs` to access the API documents and test the backend
<img width="1499" alt="Screenshot 2023-08-30 at 19 43 56" src="https://github.com/Tekhunt/auth-flow/assets/65784601/3be695ef-e89c-4db4-981f-b6d97b3d7b58">

Welcome to the backend repository of [Auth flow]. This part of the project is responsible for handling user authentication and API requests using Django and Django Rest Framework.

## Getting Started

To get started with the backend part of the project, follow these steps:

1. Clone this repository (SSH): `git clone git@github.com:Tekhunt/auth-flow.git`
- Clone this repository (HTTPS): `git clone https://github.com/Tekhunt/auth-flow.git`
2. Navigate to the project directory: `cd auth-flow`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

The backend will run on `http://localhost:8000` by default.

## Features

- User registration and login endpoints
- JWT token-based authentication
- Integration with the frontend for authentication flow
- User model customization for additional fields
- Secure password handling using Django's built-in features

## API Endpoints

- `/api/v1/usercreate/`: User registration endpoint
- `/api/login/`: User login endpoint
- `/api/v1/users/`: Fetch user

