from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from hmm import  models

# Create your views here.

def ajax(request):
    pass



def ttt(request):
    if request.method == 'POST':
        if request.POST.get('method') == 'edit':
            print(request.POST)
            uid = request.POST.get('uid')
            groupid = request.POST.get('groupid')
            u = request.POST.get('username')
            p = request.POST.get('password')
            models.userinfo.objects.filter(uid=uid).update(username=u,password=p,user_group_id=groupid)
            return HttpResponse('ok')
        elif request.POST.get('method') == 'delete':
            uid = request.POST.get('uid')
            models.userinfo.objects.filter(uid=uid).delete()
            return HttpResponse('ok')

        else:
            print(request.POST)
            u = request.POST.get('username')
            p = request.POST.get('password')
            gid = request.POST.get('groupid')

            if p and len(p) > 6:
                models.userinfo.objects.create(
                    username=u,
                    password=p,
                    user_group_id=gid
                )
                return HttpResponse('OK')
            else:
                return HttpResponse('密码不符合要求')

    v1 = models.userinfo.objects.all()
    user_group = models.group.objects.all()
    for i in user_group:
        print(i.groupname,i.gid,i.bvv.all())
    # vv1 = models.group.objects.all().values('groupname','gid','userinfo__uid','userinfo__username','userinfo__password')
    # vvv1 = models.group.objects.all().values_list('groupname','gid','userinfo__uid','userinfo__username','userinfo__password')
    # print(vv1)
    # print(vvv1)

    v2 = models.userinfo.objects.filter(uid__gt=0).values('username','password','user_group__groupname','user_group__gid')

    v3 = models.userinfo.objects.all().values_list('username','password','user_group__groupname','user_group__gid')


    return render(request,'ttt.html',{'v1':v1,'v2':v2,'v3':v3,'user_group':user_group})

def login(request):

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        result = models.userinfo.objects.filter(username=u,password=p).first()

        if result:
            return  redirect('/hmm/index.html')

    return  render(request,'login.html')


def index(request):

    return  render(request,'index.html')


def userinfo(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        groupid = request.POST.get('groupid')
        models.userinfo.objects.create(username=u,password=p,user_group_id=groupid)
    alluser = models.userinfo.objects.all()
    for i in alluser:
        print(i.user_group.groupname) #当循环这个的时候里面自带一个外面管理的对象,改对象则是usergroup那个类,通过这个关系就可以在userinfo中去查找group的字段
    allgroup = models.group.objects.all()
    return render(request,'user_info.html',{'user_info':alluser,'group':allgroup})


def usergroup(request):
    allgroup = models.group.objects.all()
    if request.method == 'POST':
        groupname = request.POST.get('groupname')
        models.group.objects.create(groupname=groupname)
        return  redirect('/hmm/user_group.html')

    return  render(request,'user_group.html',{'user_group':allgroup})

def group_del(request,gid):

    result = models.group.objects.filter(gid=gid).delete()

    if result:
        return redirect('/hmm/user_group.html')



def user_edit(request,uid):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        groupid = request.POST.get('groupid')
        models.userinfo.objects.filter(uid=uid).update(username=u,password=p,user_group_id=groupid)


    allgroup = models.group.objects.all()
    result = models.userinfo.objects.filter(uid=uid).first()

    return render(request,'user_edit.html',{'user_edit':result,'group':allgroup})


def user_del(request,uid):
    models.userinfo.objects.filter(uid=uid).delete()
    return redirect('/hmm/user_info.html')