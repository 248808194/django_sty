from django.shortcuts import render
from django.shortcuts import HttpResponse
from  django.shortcuts import render
from  django.shortcuts import redirect
import os
from django.views import View
from django.urls import reverse  # 根据name生成一个新的url
from cmdb import  models



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = models.UserInfo.objects.filter(username=username,password=password).first()
        if result:
            return  redirect('cmdb/index')



    return  render(request,'login.html')


def index(request):

    return  render(request,'index.html')



def user_info(request):
    if request.method == 'GET':
        result = models.UserInfo.objects.all()
        return  render(request,'user_info.html',{'user_info':result})

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.create(username=u,password=p)
        return  redirect('/cmdb/user_info')



def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return redirect('/cmdb/user_info')


def user_del(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')

def user_group(request):
    return  render(request,'user_group.html')


def user_edit(request,nid):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(password=p,username=u)
        return redirect('/cmdb/user_info')
    else:

        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'user_edit':obj})





# USER_DICT = {
#     'k1':'v1',
#     'k2':'v2',
#     'k3':'v3',
#     'k4':'v4',
#     'k5':'v5',
# }

# USER_DICT = {
#     '1' : {'NAME':'ROOT1' ,'EMAIL':'ROOT1@123.COM'},
#     '2' : {'NAME':'ROOT2' ,'EMAIL':'ROOT2@123.COM'},
#     '3' : {'NAME':'ROOT3' ,'EMAIL':'ROOT3@123.COM'},
#     '4' : {'NAME':'ROOT4' ,'EMAIL':'ROOT4@123.COM'},
#     '5' : {'NAME':'ROOT5' ,'EMAIL':'ROOT5@123.COM'},
# }
#
#
# def index(request,*args,**kwargs):
#     v = reverse('indexx',kwargs={'nid':12,'pid':23})
#     print(v)
#     return  render(request,'index.html',{'user_dict':USER_DICT,'v':v})
#
#
# def detail(request,*args,**kwargs):
#     print(request.path_info)
#     newurl = reverse('detail',args=(1,))
#     print(newurl)
#     return  render(request,newurl)


# def orm(request):
#     from cmdb import  models
#     TEMP_LIST = []
#增
    #method 1
    # models.UserInfo.objects.create(username='root',password=123)

    #method 2
    # dic = {'username':'zhoutao','password':1234}
    # models.UserInfo.objects.create(**dic)

    #method 3
    # obj = models.UserInfo(username='root1',password=123)
    # obj.save()

#查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='zhoutao',password=111)
    # for i in result:
    #     TEMP_LIST.append({'id':i.id ,'username':i.username,'password':i.password})
    # print(TEMP_LIST)
    # return  render(request,'orm.html',{'user_detail':TEMP_LIST},)
    # return HttpResponse('orm\n')

#删

    # models.UserInfo.objects.all().delete(); #全部删除
    # models.UserInfo.objects.filter(username='root',password='123').delete() #匹配删除

#改
    # models.UserInfo.objects.filter(password=2).update(password=212) #匹配更新
    # models.UserInfo.objects.all().update(username=212) #全部
    # obj = models.UserInfo.objects.filter(username='root',password=1213).first()
    # print(obj)
    # return HttpResponse('orm')





# def detail(request,*args,**kwargs):
#     # print(request.path_info) #获取当前的url
#     # 根据urls下定义的name 生成一个新的url
#     url1 = reverse('detail',args=(123,))
#     print(url1)
#     print(args)
#     # print('arg0',args[0])
#     user_detail = USER_DICT[args[0]]
#     return render(request,'detail.html',{'user_detail':user_detail})
#     # return render(request,url1,{'user_detail':user_detail})
#     return  render(request,url1)




# def login(request):
#     if request.method == 'POST':
#         print(request.POST)
#         # print(request.POST.get('gender'))
#         # print(request.POST.getlist('faver'))
#         # print(request.POST.get('city'))
#         # print(request.POST.getlist()) #复选必须要用getlist方便数据处理
#
#
#         #文件
#         fileobj = request.FILES.get('ufile')
#
#         print(fileobj)
#         upload_dir_files = os.path.join('uploads',fileobj.name)
#         with open(upload_dir_files,'wb') as f1:
#             for i in fileobj.chunks():
#                 f1.write(i)
#
#
#
#
#     return  render(request,'login1.html')