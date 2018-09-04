from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from ormm import models
# Create your views here.


def app(request):
    if request.method == 'POST':
        print(request.POST)
        appname = request.POST.get('appname')
        hostlist = request.POST.getlist('hostlist')
        print(appname,hostlist)
        obj = models.Application.objects.create(name=appname)

        obj.r.add(*hostlist)
        return HttpResponse('ok')

    app_list = models.Application.objects.all()
    host_list = models.Host.objects.all()
    for row in app_list:
        print(row.name,row.r.all()) #r其实就是值的关联的HOST这个对象   -->web <QuerySet [<Host: Host object (1)>, <Host: Host object (4)>]>
    return render(request,'app.html',{'all_list':app_list,'host_list':host_list})



def appajx(request):
    pass
