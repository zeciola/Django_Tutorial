from django.db import models
from uuid import uuid4


class User(models.Model):
    ...


class Classroom(models.Model):
    rooms_name = models.CharField(
        max_length=256,
    )
    maximum_occupancy =  models.PositiveSmallIntegerField(
        default=30,
    )

    def __str__(self) -> str:
        return f"<{self.rooms_name}>"


class Teacher(models.Model):
    teacher_uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        description="Student uuid code.",
        unique=True
    )
    first_name = models.CharField(
        max_length=256,
        description="Student first name."
    )
    last_name = models.CharField(
        max_length=256,
        description="Student last name."
    )
    email = models.EmailField(
        max_length=256,
        description="Student pessoal e-mail."
    )
    age = models.PositiveSmallIntegerField(
        description="Student age."
    )
    classroom = models.ManyToManyField(
        Classroom
    )


class Student(models.Model):
    student_uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        description="Student uuid code.",
        unique=True
    )
    first_name = models.CharField(
        max_length=256,
        description="Student first name."
    )
    last_name = models.CharField(
        max_length=256,
        description="Student last name."
    )
    email = models.EmailField(
        max_length=256,
        description="Student pessoal e-mail."
    )
    age = models.PositiveSmallIntegerField(
        description="Student age."
    )
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"<Student: {self.full_name} - {self.student_uuid}>"
