from django import forms


class TeacherForm(forms.Form):
    name = forms.CharField(label="Имя преподавателя")
    age = forms.IntegerField(label="Возраст преподавателя")
    position = forms.CharField(label="Должность преподавателя")
    academic_title = forms.CharField(label="Ученоё звание преподавателя")
    academic_state = forms.CharField(label="Степень преподавателя")


