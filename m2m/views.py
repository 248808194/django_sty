from django.shortcuts import render,HttpResponse
from m2m import  models
# Create your views here.


def test1(request):
    print(request.META)

    # objboys = [
    #     models.Boy(bname='jack'),
    #     models.Boy(bname='rose'),
    #     models.Boy(bname='alens'),
    # ]
    # models.Boy.objects.bulk_create(objboys)
    # #
    # objgirls = [
    #     models.Girl(gname='helen'),
    #     models.Girl(gname='jamis'),
    #     models.Girl(gname='chenfang')
    # ]
    # models.Girl.objects.bulk_create(objgirls)
    #通过Girl表进行反查
    obj = models.Girl.objects.filter(gname='helen').first().love_set.all() #通过girl去第三章love表下查找 所有和helen有关系的queryset 对象;_set暂时理解为固定语法吧
    # print(obj)
    # for i in obj:
    #     print(i.b.bname) #循环这个对象通过. 来查找boy,即打印出所有和Helen有关系的boy

    #通过love表进行反查
    #g其实就是girl这个类
    obj = models.Love.objects.filter(g__gname='helen').all() #通过love表中g对应的girl这个表,通过g__gname 去girl表中查找名字是helen的所有lovequeryset对象
    # print(obj)
    # for i in obj:
    #     print(i.b.bname)
    # print(models.Boy.objects.all().values('bname'))

    boy_list = models.Love.objects.filter(g__gname='helen').values('b__bname') # queryset内部元素格式是字典
    # print(boy_list)
    boy_list = models.Love.objects.filter(g__gname='helen').values_list('b__bname','b_id') #queryset内部元素格式是元祖
    # print(boy_list) #<QuerySet [{'b__bname': 'jack'}, {'b__bname': 'rose'}, {'b__bname': 'alens'}]>

    return  HttpResponse('200')

