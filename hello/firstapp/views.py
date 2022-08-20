from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World! Это мой первый проект на Django!")


def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id_p=1, name="Максим"):
    output = "<h2>Пользователь</h2><h3>id_p: {0} Имя: {1}</hЗ>".format(id_p, name)
    return HttpResponse(output)
