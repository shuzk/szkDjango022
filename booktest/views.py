from django.shortcuts import render, redirect
from booktest.models import *
from datetime import date
from django.db.models import F
from django.db.models import Q, Sum

# 查询所有图书并显示
def index(request):
    list = BookInfo.objects.all()
    list1 = BookInfo.objects.filter(id=1)
    list2 = BookInfo.objects.filter(btitle__contains='传')
    list3 = BookInfo.objects.filter(btitle__endswith='部')
    list4 = BookInfo.objects.filter(btitle__isnull=False)
    list5 = BookInfo.objects.filter(id__in=[1, 3, 5])
    list6 = BookInfo.objects.filter(id__gt=3)
    list7 = BookInfo.objects.exclude(id=3)
    list8 = BookInfo.objects.filter(bpub_date__year=1980)
    list9 = BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1))
    list10 = BookInfo.objects.filter(bread__gte=F("bcomment"))
    list11 = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

    list12 = BookInfo.objects.filter(bread__gt=20, id__lt=3)

    list13 = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
    list14 = BookInfo.objects.filter(~Q(pk=3))

    list15 = BookInfo.objects.aggregate(Sum('bread'))
    list16 = BookInfo.objects.count()
    return render(request, 'booktest/index.html', {'list': list})


# 创建新图书
def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995, 12, 30)
    book.save()
    # 转向到首页
    return redirect('/')


# 逻辑删除指定编号的图书
def delete(request, id):
    book = BookInfo.objects.get(id=int(id))
    book.delete()
    # 转向到首页
    return redirect('/')
