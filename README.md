# Project Management CLI

A command-line application built with Python that helps users manage projects and tasks efficiently. The application allows users to create accounts, organize projects, add tasks, track task completion, and save data between sessions using JSON persistence.

## Features

* Create and manage users
* Create projects with descriptions and due dates
* Add tasks to projects
* Mark tasks as completed
* View users, projects, and tasks in a formatted table
* Automatically save and load data using JSON
* Command-line interface built with `argparse`
* Beautiful terminal output using `rich`
* Automated tests using `pytest`

## Project Structure

```text
project-management-cli/
├── data/
│   └── database.json
├── models/
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   ├── task.py
│   └── __init__.py
├── tests/
│   ├── test_cli.py
│   ├── test_project.py
│   ├── test_task.py
│   └── test_user.py
├── utils/
├── main.py
├── storage.py
├── requirements.txt
├── Pipfile
└── README.md
```

## Requirements

* Python 3.10 or newer
* pip
* Rich
* Pytest

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the CLI using:

```bash
python3 main.py
```

To see all available commands:

```bash
python3 main.py --help
```

## Running the Tests

Run all tests using:

```bash
python3 -m pytest -v
```

Example output:

```text
========================
7 passed in 0.20s
========================
```

## Technologies Used

* Python 3
* argparse
* JSON
* Rich
* Pytest

## Data Persistence

Application data is stored in:

```text
data/database.json
```

Data is automatically loaded when the application starts and saved whenever changes are made.

## Example Workflow

1. Create a user.
2. Create a project.
3. Add tasks to the project.
4. Mark tasks as completed.
5. View project progress.
6. Exit the application. All data is automatically saved.

## Future Improvements

* Edit existing projects and tasks
* Delete users, projects, and tasks
* Search and filter tasks
* Priority levels
* Task categories
* Due date reminders
* Export project reports

## Author

**Albashir Abdi**

## License

This project was created for educational purposes.
