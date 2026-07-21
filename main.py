import argparse

from models import User, Project, Task
from storage import save_data, load_data
from rich.console import Console
from rich.table import Table

console = Console()

# -------------------------
# In-memory storage
# -------------------------

users = {}

# Load saved data
loaded_users = load_data()

for user_data in loaded_users:
    user = User(
        user_data["name"],
        user_data["email"]
    )

    for project_data in user_data["projects"]:
        project = Project(
            project_data["title"],
            project_data["description"],
            project_data["due_date"]
        )

        for task_data in project_data["tasks"]:
            task = Task(
                task_data["title"],
                task_data["assigned_to"]
            )

            task.status = task_data["status"]
            project.add_task(task)

        user.add_project(project)

    users[user.name] = user


# -------------------------
# User Functions
# -------------------------

def add_user(args):
    if args.name in users:
        print("❌ User already exists.")
        return

    user = User(args.name, args.email)
    users[args.name] = user

    save_data(users)

    print(f"✅ User '{args.name}' created successfully.")


def list_users(args):
    if not users:
        console.print("[red]No users found.[/red]")
        return

    table = Table(title="Users")

    table.add_column("Name", style="cyan")
    table.add_column("Email", style="green")

    for user in users.values():
        table.add_row(user.name, user.email)

    console.print(table)


# -------------------------
# Project Functions
# -------------------------

def add_project(args):
    user = users.get(args.user)

    if user is None:
        print("❌ User not found.")
        return

    project = Project(
        args.title,
        args.description,
        args.due_date
    )

    user.add_project(project)

    save_data(users)

    print(f"✅ Project '{args.title}' added to {user.name}.")


def list_projects(args):
    user = users.get(args.user)

    if user is None:
        console.print("[red]User not found.[/red]")
        return

    if not user.projects:
        console.print("[yellow]No projects found.[/yellow]")
        return

    table = Table(title=f"{user.name}'s Projects")

    table.add_column("Title", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Due Date", style="green")

    for project in user.projects:
        table.add_row(
            project.title,
            project.description,
            project.due_date
        )

    console.print(table)


# -------------------------
# Task Functions
# -------------------------

def add_task(args):
    user = users.get(args.user)

    if user is None:
        print("❌ User not found.")
        return

    project = None

    for p in user.projects:
        if p.title == args.project:
            project = p
            break

    if project is None:
        print("❌ Project not found.")
        return

    task = Task(
        args.title,
        args.assigned_to
    )

    project.add_task(task)

    save_data(users)

    print(f"✅ Task '{task.title}' added to project '{project.title}'.")


def list_tasks(args):
    user = users.get(args.user)

    if user is None:
        console.print("[red]User not found.[/red]")
        return

    project = None

    for p in user.projects:
        if p.title == args.project:
            project = p
            break

    if project is None:
        console.print("[red]Project not found.[/red]")
        return

    if not project.tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title=f"Tasks - {project.title}")

    table.add_column("Title", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Assigned To", style="magenta")

    for task in project.tasks:
        table.add_row(
            task.title,
            task.status,
            task.assigned_to if task.assigned_to else "-"
        )

    console.print(table)


def complete_task(args):
    user = users.get(args.user)

    if user is None:
        print("❌ User not found.")
        return

    project = None

    for p in user.projects:
        if p.title == args.project:
            project = p
            break

    if project is None:
        print("❌ Project not found.")
        return

    for task in project.tasks:
        if task.title == args.title:
            task.complete()

            save_data(users)

            print(f"✅ Task '{task.title}' marked as completed.")
            return

    print("❌ Task not found.")


# -------------------------
# CLI
# -------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # -----------------
    # add-user
    # -----------------
    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Create a new user"
    )

    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    add_user_parser.set_defaults(func=add_user)

    # -----------------
    # list-users
    # -----------------
    list_users_parser = subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    list_users_parser.set_defaults(func=list_users)

    # -----------------
    # add-project
    # -----------------
    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Add a project"
    )

    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument(
        "--due-date",
        dest="due_date",
        required=True
    )

    add_project_parser.set_defaults(func=add_project)

    # -----------------
    # list-projects
    # -----------------
    list_projects_parser = subparsers.add_parser(
        "list-projects",
        help="List projects"
    )

    list_projects_parser.add_argument("--user", required=True)

    list_projects_parser.set_defaults(func=list_projects)

    # -----------------
    # add-task
    # -----------------
    add_task_parser = subparsers.add_parser(
        "add-task",
        help="Add a task"
    )

    add_task_parser.add_argument("--user", required=True)
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument(
        "--assigned-to",
        dest="assigned_to",
        default=None
    )

    add_task_parser.set_defaults(func=add_task)

    # -----------------
    # list-tasks
    # -----------------
    list_tasks_parser = subparsers.add_parser(
        "list-tasks",
        help="List tasks"
    )

    list_tasks_parser.add_argument("--user", required=True)
    list_tasks_parser.add_argument("--project", required=True)

    list_tasks_parser.set_defaults(func=list_tasks)

    # -----------------
    # complete-task
    # -----------------
    complete_task_parser = subparsers.add_parser(
        "complete-task",
        help="Mark task as completed"
    )

    complete_task_parser.add_argument("--user", required=True)
    complete_task_parser.add_argument("--project", required=True)
    complete_task_parser.add_argument("--title", required=True)

    complete_task_parser.set_defaults(func=complete_task)

    # -----------------

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()