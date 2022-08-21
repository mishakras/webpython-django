from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Имя студента")
    age = forms.IntegerField(label="Возраст студента")
    group = forms.IntegerField(label="Группа студента")

