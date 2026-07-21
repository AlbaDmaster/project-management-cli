from models.task import Task


def test_create_task():
    task = Task("Finish report")

    assert task.title == "Finish report"
    assert task.status == "Pending"
    assert task.assigned_to is None


def test_complete_task():
    task = Task("Finish report")

    task.complete()

    assert task.status == "Completed"