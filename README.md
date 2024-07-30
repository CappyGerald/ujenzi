# Project Manager Web App

This project is a web application designed to help construction companies manage their projects. Users can track activities, costs, personnel, materials, equipment, deadlines, milestones, and revenue.

## Features

- Add, edit, and delete projects
- Track machinery, activities, personnel, milestones, and more
- User authentication and role-based access control
- Comprehensive project overview and management capabilities

## Technologies Used

- Python
- Django
- HTML and CSS
- SQLite (or other database systems supported by Django)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/CappyGerald/project_manager.git
    cd project_manager
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations and create the database:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser for the admin panel:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to:

    ```
    http://127.0.0.1:8000/
    ```

## Usage

### Adding Projects

1. Log in to the application.
2. Navigate to the "Projects" section.
3. Click "Add Project" and fill in the required details.
4. Save the project to track activities, costs, personnel, and more.

### Managing Machinery

1. Navigate to the "Machinery" section.
2. Add, edit, or delete machinery details.

### Tracking Activities

1. Navigate to the "Activities" section.
2. Add, edit, or delete activity details.

### Personnel Management

1. Navigate to the "Personnel" section.
2. Add, edit, or delete personnel details.

### Milestones

1. Navigate to the "Milestones" section.
2. Add, edit, or delete milestone details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.


## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

