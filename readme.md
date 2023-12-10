# Bank Statement Generator

This Django-based banking application allows users to filter transactions by date and email, and download a bank statement in CSV format or send it via email.

## Installation

Follow these steps to set up the banking application locally on your development machine:

1. **Clone the Repository**:

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/your-username/banking-application.git
   ```

2. **Navigate to the Project Directory**:

   Change your working directory to the project's root folder:

   ```bash
   cd banking-application
   ```

3. **Create a Virtual Environment (Optional but Recommended)**:

   It's a good practice to create a virtual environment to isolate the project dependencies:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:

   Install the project's dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

6. **Set Up Environment Variables**:

   Create a `.env` file in the project directory and set the following environment variables:

   ```
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

   Replace `your_email@example.com`, and `your_email_password` with your actual configuration, I am using Google email server.

7. **Apply Migrations**:

   Apply database migrations to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```

## Running the Application

To run the banking application, follow these steps:

1. **Run the Development Server**:

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. **Access the Application**:

   Open a web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the application.

## Usage

- **User Profile Page**: Upon accessing the application, you will see the user profile page, displaying user details, a "Download Bank Statement" button, and a "Filter Transactions" button.

- **Download Bank Statement**: Click the "Download Bank Statement" button to download a CSV file containing all transactions.

- **Filter Transactions**: Click the "Filter Transactions" button to open a popup dialog. Enter an email address, start date, and end date to filter transactions. Click the "Filter" button to view filtered transactions in the table on the same page.

