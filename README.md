# Video Sharing API

A FastAPI-based REST API for secure video sharing with AWS S3 integration and PostgreSQL database.

## Features

- User authentication with JWT
- Video management and sharing
- AWS S3 integration for video storage
- Role-based access control
- PostgreSQL database integration

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- AWS S3
- Python 3.x

## Prerequisites

- Python 3.x
- PostgreSQL
- AWS Account with S3 access

## Installation

1. Clone the repository
2. Install dependencies:

## Environment Variables

Create a `.env` file in the root directory with the following variables:
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_database_name
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
JWT_SECRET=your_jwt_secret



## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Videos
- `GET /api/videos/` - Get video with presigned URL
- `GET /api/videos/{video_id}` - Get video by ID (requires authentication)

## Security Features

- Password hashing using bcrypt
- JWT-based authentication
- CORS middleware enabled
- Role-based access control for videos

## Database Models

### User Model
- ID (Primary Key)
- Email (Unique)
- Password (Hashed)
- Videos (Relationship)

### Video Model
- ID (Primary Key)
- Title
- URL
- Owner ID (Foreign Key)

## Running the Application

To run the development server:
uvicorn src.main:app --reload


The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License