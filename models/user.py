from models.person import Person
from models.project import Project


class User(Person):
    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name)

        self.id = User.id_counter
        User.id_counter += 1

        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address.")
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [
                project.to_dict()
                for project in self.projects
            ]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["name"],
            data["email"]
        )

        user.projects = [
            Project.from_dict(project)
            for project in data.get("projects", [])
        ]

        return user

    def __str__(self):
        return f"User {self.id}: {self.name}"