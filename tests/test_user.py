from models.user import User


def test_create_user():
    user = User("John Doe", "john@example.com")

    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.projects == []


def test_add_project():
    user = User("John Doe", "john@example.com")

    class DummyProject:
        pass

    project = DummyProject()
    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0] == project