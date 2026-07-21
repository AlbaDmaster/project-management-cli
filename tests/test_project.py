from models.project import Project
from models.task import Task


def test_create_project():
    project = Project(
        "Website",
        "Build company website",
        "2026-12-31"
    )

    assert project.title == "Website"
    assert project.description == "Build company website"
    assert project.due_date == "2026-12-31"
    assert project.tasks == []


def test_add_task():
    project = Project(
        "Website",
        "Build company website",
        "2026-12-31"
    )

    task = Task("Finish homepage")

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0] == task