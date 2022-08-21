from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя студента")
    point = forms.IntegerField(label="Отметка студента")
