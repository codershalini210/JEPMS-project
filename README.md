# Job & Employability Progression Management System (JEPMS)

## Project Overview

The Job & Employability Progression Management System (JEPMS) is a Python and Django full-stack web application designed to help employment advisers manage employers, job vacancies and job applications in one centralised system.

The application provides a login-protected interface where authorised staff can create, view, update, delete, search and filter records. It uses Django for backend functionality, Django templates and Bootstrap for the user interface, and SQLite for data storage.

This project is developed as a Level 3 Software Development capstone project to demonstrate requirements analysis, application design, database management, full-stack development, testing, security, version control and deployment.

## Business Problem

Employment advisers may use separate spreadsheets and documents to manage employer details, vacancies and job applications. This approach can result in duplicated records, inconsistent information, difficulty finding records and limited visibility of application progress.

JEPMS aims to address these problems by providing a centralised system that:

- Stores employer, vacancy and job application records in a relational database.
- Links vacancies to employers and applications to vacancies.
- Provides a consistent process for recording and updating information.
- Allows staff to search and filter job applications.
- Displays application statuses to support progression monitoring.
- Restricts access to authorised users through authentication.

## Features

The planned application features include:

- **User authentication:** Login and logout functionality.
- **Dashboard:** Summary counts for employers, vacancies and job applications.
- **Employer management:** Create, view, update and delete employer records.
- **Vacancy management:** Manage vacancies linked to employers.
- **Job application management:** Record and update applications linked to vacancies.
- **Status tracking:** Track application progress using predefined statuses such as Applied, Interview, Offer, Rejected and Withdrawn.
- **Search and filtering:** Find applications by learner name, employer, vacancy or status.
- **Form validation:** Validate required fields and relevant input values.
- **Success and error messages:** Provide feedback after user actions.
- **Responsive interface:** Use Bootstrap to support desktop and mobile-width layouts.
- **Automated testing:** Test models, forms, views, authentication and CRUD operations.
- **Django Admin:** Provide administrative access to application records where configured.

Features should be marked as complete only after implementation and testing.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Backend web framework |
| Django Templates | Dynamic HTML rendering |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap | Responsive user interface |
| SQLite | Relational database |
| Git | Version control |
| GitHub | Source code hosting and project tracking |
| Django Test Framework | Automated testing |
| PythonAnywhere | Proposed hosting platform |

## Installation

### Prerequisites

Install the following before starting:

- Python compatible with the selected Django version
- Git
- Visual Studio Code or another code editor
- A modern web browser

### 1. Clone the repository

Replace the example URL with the actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd jepms
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, install Django first:

```bash
python -m pip install django
```

After installing the required dependencies and verifying the application, generate the file:

```bash
python -m pip freeze > requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

The application is ready for local use when the server starts successfully and the configured application pages load.

## Database Setup

JEPMS uses SQLite as its initial database. Django supports SQLite by default, so a separate database server is not required.

The database schema is managed through Django models and migrations.

### Main database entities

**1. Employer**

Stores employer information, including:

- Name
- Contact name
- Email address
- Phone number
- Website
- Notes
- Creation date

**2. Vacancy**

Stores job vacancy information, including:

- Employer
- Job title
- Description
- Location
- Salary information
- Closing date
- Vacancy status
- Creation date

Each vacancy is linked to one employer.

**3. JobApplication**

Stores application information, including:

- Learner name
- Learner email, where required or supplied
- Related vacancy
- Application date
- Application status
- Notes
- Creation and update dates

Each job application is linked to one vacancy.

### Database relationships

- One employer can have multiple vacancies.
- One vacancy can have multiple job applications.

These relationships are implemented using Django `ForeignKey` fields.

### Database commands

Create migration files after changing models:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Open the Django administrative interface, if configured:

http://127.0.0.1:8000/admin/

Use fictional sample data for development and testing. Do not commit real personal information or confidential employment records to the public repository.

## Running Tests

JEPMS uses Django's automated testing framework to check application functionality and reliability.

### 1. Run all automated tests

```bash
python manage.py test
```

### 2. Test coverage

The test suite should cover:

- Model creation and relationships
- Form validation
- Employer CRUD operations
- Vacancy CRUD operations
- Job application CRUD operations
- Login and logout functionality
- Access restrictions for unauthenticated users
- Application status validation
- Search and filtering
- Invalid input handling
- Dashboard record counts

### 3. Record test results

After running the tests, record:

- Date of testing
- Python and Django versions
- Number of tests executed
- Number of tests passed and failed
- Defects identified
- Fixes applied and retest results

Do not report tests as passed unless the test output confirms the result.

## Deployment

The application is planned for deployment to PythonAnywhere, subject to account availability and platform compatibility.

### Proposed deployment steps

1. Confirm that the application works locally.
2. Run automated tests and resolve relevant failures.
3. Commit and push the latest working code to GitHub.
4. Create or configure the PythonAnywhere web application.
5. Clone the repository into the hosting environment.
6. Create a compatible virtual environment.
7. Install dependencies using `requirements.txt`.
8. Configure the WSGI file and Django settings.
9. Configure the production secret key, `DEBUG=False` and `ALLOWED_HOSTS`.
10. Apply database migrations in the hosted environment.
11. Configure and serve static files using the platform's supported method.
12. Reload the web application.
13. Test authentication, CRUD operations, validation and search on the hosted website.
14. Record the deployed URL, deployed commit and test results.

### Deployment details

- **Hosting platform:** PythonAnywhere (planned)
- **Repository:** `https://github.com/codershalini210/JEPMS-project`
- **Live URL:** `<YOUR_DEPLOYED_APPLICATION_URL>`
- **Deployment status:** Update after deployment and verification.

Do not publish secret keys, passwords or other sensitive configuration values in GitHub.

## Limitations

The initial version of JEPMS has the following limitations:

- It is an educational prototype and is not intended for production employment-management use.
- Role-based access control may not be included in the initial version.
- The application depends on users entering accurate information.
- Live job-board integrations and automatic vacancy imports are not included.
- Email notifications and automated reminders may be added in future versions.
- SQLite is suitable for a small learning project but may not meet the needs of a larger production deployment.
- Reporting and data export functionality may be limited.
- The application does not independently verify job applications or employer details.
- Deployment availability and supported configuration depend on the hosting provider and account.

### Future improvements

Possible enhancements include:

- Adviser and supervisor roles with appropriate permissions.
- An audit trail for application status changes.
- CSV export with suitable privacy controls.
- Dashboard charts and date-based reporting.
- Vacancy closing-date reminders.
- PostgreSQL support and managed database backups.
- Expanded accessibility and responsive design testing.
- Continuous integration and automated deployment.

---

**Project status:** Update this README as development progresses. Document implemented features, actual test results, known defects and deployment evidence accurately.
