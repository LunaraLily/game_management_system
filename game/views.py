from django.contrib.auth.decorators import login_required   # ← 新增这一行
from django.http import HttpResponse
from django.shortcuts import render, redirect
from game.models import GameInfo
from django.urls import reverse


@login_required                         # ← 加这一行
def index(request):
    games = GameInfo.objects.all()
    context = {'games': games}
    return render(request, 'index.html', context)


# add_nug、del_nug、edit_nug 保持你原来的代码不变


def add_nug(request):
    #展示数据
    if request.method == 'GET':
        # 将所有数据拿出来
        games = GameInfo.objects.all()

        # 2，将数据传到前端页面
        context = {'games': games}

        return render(request,'add_nug.html',context)

    else:
        #1.数据保存,拿到前端的内容
        name=request.POST.get('name')
        platform=request.POST.get('platform')
        company=request.POST.get('company')


        #从查询中判断是否重名：
        seach_games=GameInfo.objects.filter(name=name)

        if not seach_games:


            #2.保存到数据库
            game_obj=GameInfo()     #向表的当中添加一条空数据
            game_obj.name=name      #向这条空数据的一个单元格赋值
            game_obj.platform=platform
            game_obj.company=company
            game_obj.save()

            #3.跳转到首页
            # return  render(request,'index.html')
            return  redirect("index")


        else:
            #如果有，则返回错误信息
            games = GameInfo.objects.all()

            # 2，将数据传到前端页面
            # context = {'games': games}


            return render(request,'add_nug.html',{'error_mug':'该名字已存在','games': games})


def del_nug(request,id):
    #filter,判断id是否相同
    GameInfo.objects.filter(id=id).delete()

    #2返回到首页，并展示所有的数据


     
    return redirect("index")


def edit_nug(request,id):
    if request.method == 'GET':
        games = GameInfo.objects.all()
        return render(request,"edit_nug.html",{'games':games,'id':id})

    else:
        #读取前端的技能
        name=request.POST.get('name')
        platform=request.POST.get('platform')
        company=request.POST.get('company')

        #2将要修改的数据查询出来
        game_obj=GameInfo.objects.filter(id=id)[0]

        #将要修改的数据进行修改：
        game_obj.name=name
        game_obj.platform=platform
        game_obj.company=company
        game_obj.save()
        return redirect("index")