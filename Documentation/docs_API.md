# Umjolo API Documentation

## Authentication Endpoints

### POST /api/login
Login user

**Request:**
```json
{
    "email": "user@example.com",
    "password": "password123"
}


{
    "status": "success",
    "token": "jwt_token_here",
    "user": {
        "id": 1,
        "name": "Happy M",
        "email": "user@example.com"
    }
}
