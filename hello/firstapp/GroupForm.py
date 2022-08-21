from django import forms


class CourseForm(forms.Form):
    number = forms.IntegerField(label="Номер группы")


