# Healthcare Backend API

A RESTful backend system for a healthcare application built with Django and Django REST Framework. This system provides secure user authentication and comprehensive management of patient and doctor records.

## 🚀 Features

- **JWT Authentication** - Secure user registration and login using JSON Web Tokens
- **Patient Management** - Complete CRUD operations for patient records
- **Doctor Management** - Full management system for doctor profiles
- **Patient-Doctor Mapping** - Assign and manage relationships between patients and doctors
- **User-Based Access Control** - Users can only access their own created records
- **PostgreSQL Database** - Robust and scalable data storage
- **Input Validation** - Comprehensive error handling and data validation
- **RESTful Architecture** - Clean and intuitive API design

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL 12 or higher

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sufail07/Healthcare-backend.git
cd Healthcare-backend
```

### 2. Create and activate virtual environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database for the project with the name Healthcare:

### 5. Set up environment variables

Create a `.env` file in the project root directory:

```env
DB_PASSWORD=your_password
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/api/
```

### Authentication Endpoints

#### Register a new user
```http
POST /api/auth/register/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "message": "User registered successfully"
}
```

#### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Patient Management Endpoints

**Note:** All patient endpoints require authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

#### Create a patient
```http
POST /api/patients/
Content-Type: application/json
Authorization: Bearer <token>

{
    "name": "Jane Smith",
    "age": 35,
    "gender": "Female",
    "phone": "+1234567890",
    "address": "123 Main St, City",
    "medical_history": "No significant history"
}
```

#### Get all patients
```http
GET /api/patients/
Authorization: Bearer <token>
```

#### Get specific patient
```http
GET /api/patients/<id>/
Authorization: Bearer <token>
```

#### Update patient
```http
PUT /api/patients/<id>/
Content-Type: application/json
Authorization: Bearer <token>

{
    "name": "Jane Smith",
    "age": 36,
    "phone": "+1234567890"
}
```

#### Delete patient
```http
DELETE /api/patients/<id>/
Authorization: Bearer <token>
```

### Doctor Management Endpoints

#### Create a doctor
```http
POST /api/doctors/
Content-Type: application/json
Authorization: Bearer <token>

{
    "name": "Dr. Michael Brown",
    "specialization": "Cardiology",
    "phone": "+1234567890",
    "email": "dr.brown@hospital.com",
    "experience_years": 15
}
```

#### Get all doctors
```http
GET /api/doctors/
Authorization: Bearer <token>
```

#### Get specific doctor
```http
GET /api/doctors/<id>/
Authorization: Bearer <token>
```

#### Update doctor
```http
PUT /api/doctors/<id>/
Content-Type: application/json
Authorization: Bearer <token>

{
    "name": "Dr. Michael Brown",
    "specialization": "Cardiology",
    "experience_years": 16
}
```

#### Delete doctor
```http
DELETE /api/doctors/<id>/
Authorization: Bearer <token>
```

### Patient-Doctor Mapping Endpoints

#### Assign doctor to patient
```http
POST /api/mappings/
Content-Type: application/json
Authorization: Bearer <token>

{
    "patient": "Jane Smith",
    "doctor": "Dr. Michael Brown"
}
```

#### Get all mappings
```http
GET /api/mappings/
Authorization: Bearer <token>
```

#### Get doctors for a specific patient
```http
GET /api/mappings/<patient_id>/
Authorization: Bearer <token>
```

#### Remove doctor from patient
```http
DELETE /api/mappings/<id>/
Authorization: Bearer <token>
```

## 🔒 Security Features

- **JWT Authentication** - Secure token-based authentication
- **Password Hashing** - Passwords are securely hashed using Django's default hasher
- **Environment Variables** - Sensitive data stored in environment variables
- **User Isolation** - Users can only access their own patient records
- **Input Validation** - All inputs are validated before processing


## 📁 Project Structure

```
Healthcare-backend/
├── healthcare/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                     # Main application
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # URL routing
├── manage.py
├── requirements.txt
├── .env                    # Environment variables
└── README.md
```

## 🛠️ Technologies Used

- **Django** - High-level Python web framework
- **Django REST Framework** - Toolkit for building Web APIs
- **PostgreSQL** - Advanced open-source relational database
- **djangorestframework-simplejwt** - JWT authentication for DRF
- **python-dotenv** - Environment variable management


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Sufail**
- GitHub: [@Sufail07](https://github.com/Sufail07)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

⭐ Star this repository if you find it helpful!
