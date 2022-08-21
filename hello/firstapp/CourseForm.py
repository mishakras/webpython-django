from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(label="Название предмета")
    age = forms.IntegerField(label="Длительность предмета")


