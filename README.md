# Referral Project

This project demonstrates how to deploy a Django application using Docker.

## Prerequisites

Before you begin, ensure you have Docker installed on your system. You can download and install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop).

## Usage

### Building the Docker Image

To build the Docker image for the Django project, follow these steps:

1. Clone the repository:

```sh
git clone <repository-url>
```
2. Navigate to the project directory
  
3. Build the Docker image
```sh
docker-compose up --build
```
This command will start the Docker container and expose port 8000 on your local machine. You can access the Django application at [http://localhost:8000](http://localhost:8000).

## API Testing

To test the APIs of the Django application, you can use tools like Postman or curl. Here are the details for testing the APIs:

1. **User Registration Endpoint**:
   - URL: `http://localhost:8000/register/`
   - Method: POST
   - Body: JSON containing name, email, password and
     optional referral_code (referral code can be username of that referrer or code if code is available, code (this code will used as custom referral code for that user)
   - Response: Unique user ID and token
   
2. **User Details Endpoint**:
   - URL: `http://localhost:8000/user-details/`
   - Method: GET
   - Header: Authorization token (obtained during registration)
   - Response: User details including name, email, referral code, and timestamp
   
3. **User Referrals Endpoint**:
   - URL: `http://localhost:8000/user-referrals/`
   - Method: GET
   - Header: Authorization token (obtained during registration)
   - Response: List of users who registered using the current user's referral code
## Note: Add token in headers for API 2 and 3 as follows: Authorization:Token token_key
   
