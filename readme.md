# Bank Statement Service

## Overview
The Bank Statement Service is a set of microservices designed to generate and email a PDF statement containing a user's bank transactions over a specified period. The project consists of four separate services: API Service, Database Service, PDF Generation Service, and Email Service.

## Project Structure
The project is divided into the following main components:

- `api_service`: The Flask application serving as the entry point for generating bank statements.
- `database_service`: Handles fetching and filtering transaction data from a CSV file.
- `pdf_service`: Generates a PDF document from transaction data.
- `email_service`: Sends the generated PDF to the user's email.

## Prerequisites
- Python 3.x
- Pip (Python package manager)

## Installation

1. **Clone the Repository**
```bash
git clone [repository-url]
```

2. **Navigate to the Project Directory**

3. **Set Up a Python Virtual Environment (Optional but Recommended)**
- Create the virtual environment:
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Linux/Mac:
    ```
    source venv/bin/activate
    ```
  - On Windows:
    ```
    venv\Scripts\activate
    ```

4. **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

## Running the Services
  - On Linux/Mac:
    ```
    ./start_services.sh
    ```
  - On Windows:
    ```
    ./start_services.bat
    ```


## Usage

To generate and email a bank statement:

1. Send a POST request to `http://localhost:5000/generate-statement` with the following JSON payload:
```json
{
    "user_email": "user@example.com",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
}
example request:

curl -X POST http://localhost:5000/generate-statement \
-H "Content-Type: application/json" \
-d '{"user_email": "user1@example.com", "start_date": "2022-01-01", "end_date": "2022-12-31"}'

```
## Notes
- The email_sender service is set up to use a local SMTP server. You'll need to configure this to work with a real email server, including authentication and server details.
- run this command 
```bash
python -m smtpd -c DebuggingServer -n localhost:1025
```
for viewing the sent email in the terminal.

