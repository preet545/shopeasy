# Shop Easy Microservices

## Overview
This repository contains the microservices for user authentication, session management, and password reset for the Shop Easy application.

## Installation
 ```
    pip install Flask
    python app.py
    python app_auth.py
```

### Microservice A: User Authentication, Session Management, and Password Reset

#### Endpoints

1. **Register a new user**
   - **URL:** `/register`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "email": "user@example.com",
       "password": "securepassword"
     }
     ```
   - **Response:**
     - **201 Created** if the registration is successful.
     - **400 Bad Request** if the email is already registered.
   
2. **User login**
   - **URL:** `/login`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "email": "user@example.com",
       "password": "securepassword"
     }
     ```
   - **Response:**
     - **200 OK** if the login is successful.
     - **400 Bad Request** if the email or password is incorrect.

3. **Reset password**
   - **URL:** `/reset_password`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "email": "user@example.com"
     }
     ```
   - **Response:**
     - **200 OK** if the password reset email is sent.
     - **400 Bad Request** if the email is not registered.

### Example Calls

#### Register a New User
```python
import requests

url = "http://localhost:8000/register"
data = {
    "email": "user@example.com",
    "password": "securepassword"
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
