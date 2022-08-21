from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Course(models.Model):
    hours = models.IntegerField()
    name = models.CharField(max_length=50)


class Teacher(Person):
    position = models.CharField(max_length=50)
    academic_title = models.CharField(max_length=50, default="")
    academic_state = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)


class Group(models.Model):
    number = models.IntegerField()
    courses = models.ManyToManyField(Course)


class Student(Person):
    Group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
