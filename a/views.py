from django.shortcuts import render,HttpResponse
from  django.shortcuts import redirect
from a import models
from django.utils.safestring import mark_safe
import json

LIST = []

for i in range(109):
    LIST.append(i)


def tt(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    per_page_count = 5
    start = (current_page -1) * per_page_count #p = 1 current_page = 0  第一页0 -10  ; p=2 current = 10 ;当前页10 - 20
    end = (current_page) * per_page_count
    data = LIST[start:end] #列表切片
    all_count = len(LIST)
    print(data)
    count,y = divmod(all_count,per_page_count) #divmod 分页功能
    # count +=1
    if y:count += 1

    page_list = []

    for i in range(1,count+1):
        if i == current_page: #如果点击的是当前页数字,则增加一个高亮的样式
            temp = '<a class="page active" href="/a/tt/?p=%s">%s</a>'%(i,i)
        else:
            temp =  '<a class="page" href="/a/tt/?p=%s">%s</a>'%(i,i)
        page_list.append(temp)

    page_str = mark_safe("".join(page_list)) #安全起见默认都是字符串,此处用Mark_safe 转换,前端用 str|safe
    print(page_str)
    return render(request,'tt.html',{'li':data,'page_str':page_str})




def atemp(request):
    all_host = models.Host.objects.all()

    return render(request,'atemp.html',{'all_host':all_host,'name':'zhoutao'})

def index(request):
    host_list = models.Host.objects.all()
    all_app = models.App.objects.all()
    all_user = models.UserGroup.objects.all()
    all_u = models.User.objects.all()

    return render(request,'aindex.html',{'host_list':host_list,'all_app':all_app,'all_user':all_user,'all_u':all_u})


def addhost(request):
    if request.method == 'POST':

        h = request.POST.get('hostname')
        i = request.POST.get('ipaddr')
        p = request.POST.get('port')
        applist = request.POST.getlist('applist')
        models.Host.objects.create(hostname=h,ip=i,port=p)
        for i in applist:
            obj = models.App.objects.get(aid=i)
            obj.h_a.add(models.Host.objects.get(hostname=h)) #ADD的时候必须是CLASS对象,不是queryset
        return HttpResponse('ok')


def edithost(request):
    ret = {'status': True, 'error': None, 'data': None}
    hid = request.POST.get('hid')
    obj = models.App.objects.filter(h_a__hid=hid).all() #通过host表的id 去反查app表拿到对应关系,即所有存在hid的app
    appname_list = []
    for i in obj:
        appname_list.append(i.aid)
    ret['data'] = appname_list
    print(ret)
    return  HttpResponse(json.dumps(ret))


def updatehost(request):
    if request.method == 'POST':
        h = request.POST.get('hostname')
        hid = request.POST.get('hid')
        i = request.POST.get('ipaddr')
        p = request.POST.get('port')
        applist = request.POST.getlist('applist') #这里存在的都必须要添加的, 如果有则跳过,如果没有则添加




        models.Host.objects.filter(hid=hid).update(hostname=h,ip=i,port=p)
        o = models.App.objects.all()
        for i in o:
            obj = models.App.objects.get(aid=i.aid)
            if str(i.aid) in applist: #如果aid在选择的app中
                obj.h_a.add(models.Host.objects.get(hostname=h))
            else:
                obj.h_a.remove(models.Host.objects.get(hostname=h))
        return HttpResponse('ok')
# Create your views here.


def aadmin(request):
    if request.method == 'POST':
        groupname = request.POST.get('groupname')
        user_list = request.POST.getlist('applist')
        print(groupname,user_list)
        obj = models.UserGroup.objects.create(groupname=groupname)
        obj.ug_u.add(*user_list)
        return HttpResponse('ok')

    host_list = models.Host.objects.all()
    all_app = models.App.objects.all()
    all_user = models.UserGroup.objects.all()
    all_u = models.User.objects.all()

    return render(request,'aadmin.html',{'host_list':host_list,'all_app':all_app,'all_user':all_user,'all_u':all_u})


def admindel(request):
    groupname = request.POST.get('groupname')
    print(groupname)
    obj = models.UserGroup.objects.filter(groupname=groupname).first()
    obj.ug_u.clear()
    models.UserGroup.objects.filter(groupname=groupname).delete()

    return HttpResponse('ok')