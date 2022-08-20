from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
    return render(request, "firstapp/home.html")


def template(request):
    return render(request, "firstapp/index.html")


def products(request, productid=-1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id_p=1, name="Максим"):
    output = "<h2>Пользователь</h2><h3>id_p: {0} Имя: {1}</hЗ>".format(id_p, name)
    return HttpResponse(output)


def student(request, id_p=-1):
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]  # массив
    user = {"name": "Максим,", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "firstapp/student.html", data)


def students(request, id_p=-1):
    stud = ["Крас", "Секунов", "Петров"]
    return TemplateResponse(request, "firstapp/students.html", context={"stud": stud})
