# CTF Engine

A simple, functional web-based Capture The Flag (CTF) engine built with Flask. This application allows users to register, log in, view challenges, and track their score. It is designed as a foundational project for learning web development and security concepts.

## Features

- User Authentication (Register, Login, Logout)
- Challenge Listing Page
- User Profile with Score Tracking
- Session Management with Flask-Login
- Database Integration with Flask-SQLAlchemy
- Production-ready deployment with Gunicorn

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (for development)
- **Authentication:** Flask-Login
- **ORM:** SQLAlchemy
- **WSGI Server:** Gunicorn

## Setup and Installation

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- \`pip\` (Python's package installer)
- \`git\`

### 1. Clone the Repository

Clone the project to your local machine:
\`\`\`bash
git clone https://github.com/VANTA-1/CTF_Engine.git
cd CTF_Engine
\`\`\`

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

- **On macOS/Linux:**
  \`\`\`bash
  python3 -m venv venv
  source venv/bin/activate
  \`\`\`

- **On Windows:**
  \`\`\`bash
  python -m venv venv
  venv\Scripts\activate
  \`\`\`

### 3. Install Dependencies

Install all required Python packages from the \`requirements.txt\` file:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Initialize the Database

The application uses a database to store user and challenge information. Before running the app for the first time, you need to create the database tables and seed it with initial data.

Run the initialization script:
\`\`\`bash
python scripts/deploy/init_db.py
\`\`\`
This command will create a \`ctf.db\` file in your project directory and populate it with a test user and a sample challenge.

### 5. Run the Application

You can run the application in two ways:

- **Development Server (for testing):**
  \`\`\`bash
  python run.py
  \`\`\`
  The application will be available at \`http://127.0.0.1:5000\`.

- **Production Server (with Gunicorn):**
  \`\`\`bash
  gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app
  \`\`\`
  The application will be available at \`http://127.0.0.1:8000\`.

## Usage

1.  Open your web browser and navigate to the application's URL (e.g., \`http://127.0.0.1:8000\`).
2.  Click on the "Register" link to create a new account.
3.  After registering, you will be automatically logged in.
4.  Navigate to the "Challenges" page to see the available challenges.
5.  Click the "Logout" link to end your session.

You can also log in with the pre-seeded test account:
- **Username:** \`testuser\`
- **Password:** \`password123\`

## Project Structure

\`\`\`
CTF_Engine/
├── app/
│   ├── __init__.py          # Application Factory
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes (login, register, logout)
│   │   └── main.py          # Main routes (index, profile, challenges)
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py        # Database models (User, Challenge)
│   └── templates/           # HTML templates
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       └── challenges.html
├── scripts/deploy/
│   └── init_db.py           # Database initialization script
├── venv/                    # Virtual environment directory (ignored by Git)
├── instance/                # Instance folder for database (ignored by Git)
├── ctf.db                   # SQLite database file (created by init_db.py)
├── requirements.txt         # Project dependencies
├── run.py                   # Development server runner
├── wsgi.py                  # Production WSGI entry point
└── README.md                # This file
\`\`\`

## License

This project is open-source and available under the [MIT License](LICENSE).

## Future Improvements

- Implement challenge submission logic and flag verification.
- Add an admin panel for managing challenges and users.
- Integrate a more robust database like PostgreSQL.
- Add Docker support for containerized deployment.

