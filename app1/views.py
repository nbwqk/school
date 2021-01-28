from django.db.models import Sum, Avg, Max, Min
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app1 import models
from app1 import forms


def add_course(request):
    course=models.Course.objects.all()
    if request.method=='POST':
        # 用提交数据生成表单
        form=forms.Add_course(request.POST)
        # 通过验证，返回True
        if form.is_valid():
            course_name=form.cleaned_data.get('course')
            models.Course.objects.create(c_name=course_name)
            return render(request,'add_course.html',locals())
        else:
            return render(request,'add_course.html',locals())
    return render(request,'add_course.html',locals())


def add_teacher(request):
    course=models.Course.objects.all()
    grade=models.Grade.objects.all()
    teacher=models.Teacher.objects.all()
    if request.method=='POST':
        form=forms.Add_teacher(request.POST)
        if form.is_valid():
            t_name=form.cleaned_data['t_name']
            t_sex=form.cleaned_data['t_sex']
            t_age=form.cleaned_data['t_age']
            c_name=form.cleaned_data['course']
            g_name=form.cleaned_data['grade']
            c=models.Course.objects.get(c_name=c_name)
            g=models.Grade.objects.get(g_name=g_name)
            models.Teacher.objects.create(t_name=t_name,t_sex=t_sex,t_age=t_age,
                                          course=c,grade=g)
            return render(request,'add_teacher.html',locals())
        else:
            return render(request,'add_teacher.html',locals())
    return render(request,'add_teacher.html',locals())


def add_school(request):
    teacher=models.Teacher.objects.all()
    school=models.School.objects.all()
    if request.method=='POST':
        form=forms.Add_school(request.POST)
        if form.is_valid():
            s_name=form.cleaned_data['s_name']
            s_master=form.cleaned_data['s_master']
            t=models.Teacher.objects.get(t_name=s_master)
            models.School.objects.create(s_name=s_name,master=t)
            return render(request,'add_school.html',locals())
        else:
            return render(request,'add_school.html',locals())
    return render(request,'add_school.html',locals())


def add_grade(request):
    school=models.School.objects.all()
    teacher=models.Teacher.objects.all()
    grade=models.Grade.objects.all()
    if request.method=='POST':
        form=forms.Add_grade(request.POST)
        if form.is_valid():
            g_name=form.cleaned_data['g_name']
            s=form.cleaned_data['school']
            s1=models.School.objects.get(s_name=s)
            g_master=form.cleaned_data['g_master']
            t=models.Teacher.objects.get(t_name=g_master)
            models.Grade.objects.create(g_name=g_name,school=s1,g_master=t)
            return render(request,'add_grade.html',locals())
        else:
            return render(request, 'add_grade.html', locals())
    return render(request,'add_grade.html',locals())


def add_banji(request):
    grade=models.Grade.objects.all()
    teacher=models.Teacher.objects.all()
    banji=models.Banji.objects.all()
    if request.method=='POST':
        form=forms.Add_banji(request.POST)
        if form.is_valid():
            b_name=form.cleaned_data['b_name']
            g=models.Grade.objects.get(g_name=form.cleaned_data['grade'])
            b_master=models.Teacher.objects.get(t_name=form.cleaned_data['b_master'])
            models.Banji.objects.create(b_name=b_name,grade=g,b_master=b_master)
            return render(request,'add_banji.html',locals())
        else:
            render(request, 'add_banji.html', locals())
    return render(request,'add_banji.html',locals())


def add_student(request):
    grade=models.Grade.objects.all()
    student=models.Student.objects.all()
    if request.method=='POST':
        form=forms.Add_student(request.POST)
        if form.is_valid():
            s_name=form.cleaned_data['s_name']
            s_sex=form.cleaned_data['s_sex']
            s_age=form.cleaned_data['s_age']
            g=models.Grade.objects.get(g_name=form.cleaned_data['grade'])
            b=models.Banji.objects.get(b_name=form.cleaned_data['banji'],grade=g)
            models.Student.objects.create(s_name=s_name,s_sex=s_sex,s_age=s_age,
                                          grade=g,banji=b)
            return render(request,'add_student.html',locals())
        else:
            return render(request, 'add_student.html', locals())
    return render(request,'add_student.html',locals())


def first_banji(func):
    def inner(*args,**kwargs):
        grade=args[0].session.get('grade')
        banji=args[0].session.get('banji')
        if grade != None and banji != None:
            return func(*args,**kwargs)
        else:
            return redirect(reverse('app1:score_banji'))
    return inner

@first_banji  # 如果session中没有年级和班级的值，就先自动跳转到选择年级和班级
def add_score(request):
    course=models.Course.objects.all()
    # 从session中接受年级和班级
    grade=request.session.get('grade')
    banji=request.session.get('banji')
    # 在数据库中找到对应的年级，创建年级对象
    g=models.Grade.objects.get(g_name=grade)
    # 在数据库中找到对应的班级，创建班级对象
    b=models.Banji.objects.get(grade=g,b_name=banji)
    # 在数据库中找到对应年级和班级的学生
    student=models.Student.objects.filter(grade=g,banji=b)
    score=models.Score.objects.all()
    if request.method=='POST':
        form=forms.Add_score(request.POST)
        print(request.POST.get('grade'))
        print(form)
        if form.is_valid():
            s_name=form.cleaned_data['s_name']
            request.session['s_name']=s_name
            request.session['course']=form.cleaned_data['course']
            c=models.Course.objects.get(c_name=form.cleaned_data['course'])
            s=models.Student.objects.get(grade=g,banji=b,s_name=form.cleaned_data['student'])
            s_time=form.cleaned_data['s_time']
            # request.session['s_time']=s_time
            s_value=form.cleaned_data['s_value']
            models.Score.objects.create(s_name=s_name,course=c,student=s,
                                        s_value=s_value,s_time=s_time)
            return render(request,'add_score.html',locals())
        else:
            return render(request,'add_score.html',locals())
    return render(request,'add_score.html',locals())


def score_banji(request):
    # 添加分数前先选择考试的年级和班级
    grade=models.Grade.objects.all()
    if request.method=='POST':
        g=request.POST.get('grade')
        b=request.POST.get('banji')
        # 选择的年级和班级存入session，以便其他页面访问
        request.session['grade']=g
        request.session['banji']=b
        return redirect(reverse('app1:add_score'))
    return render(request,'score_banji.html',locals())

# 清空session
def clear_session(request):
    request.session.flush()
    return HttpResponse('清空session')


def tongji(request):
    s_name=request.session.get('s_name')
    course=request.session.get('course')
    grade = request.session.get('grade')
    banji = request.session.get('banji')
    # s_time=request.session.get('s_time')
    s_num=models.Score.objects.count()
    s_sum=models.Score.objects.aggregate(sum=Sum('s_value'))
    zongfen=s_sum['sum']
    s_avg=models.Score.objects.aggregate(avg=Avg('s_value'))
    pingjunfen=round(s_avg['avg'],2)
    # 最高分
    s_max=models.Score.objects.aggregate(max=Max('s_value'))
    zuigaofen=s_max['max']
    # 计算90分以上的人数
    num_youxiu=models.Score.objects.filter(s_value__gte=90).count()
    # 计算80(包括80)——90(不包括90)之间的人数
    num_lianghao=models.Score.objects.filter(s_value__gte=80,s_value__lt=90).count()
    # 计算70(包括70)——80(不包括90)之间的人数
    num_yiban = models.Score.objects.filter(s_value__gte=70, s_value__lt=80).count()
    # 计算60(包括60)——70(不包括70)之间的人数
    num_xvnuli = models.Score.objects.filter(s_value__gte=60, s_value__lt=70).count()
    # 最低分
    s_min=models.Score.objects.aggregate(min=Min('s_value'))
    zuidifen=s_min['min']
    #  不合格人数过滤集
    s_buhege=models.Score.objects.filter(s_value__lt=60)
    # 计算不合格人数
    num_buhege=s_buhege.count()
    # 合格人数过滤集
    s_hege=models.Score.objects.filter(s_value__gte=60)
    # 计算合格人数
    num_hege=s_hege.count()
    # 计算合格率
    hegelv=num_hege/s_num
    # 计算合格率百分数
    hegelv_persent=format(round(hegelv,6),'.2%')
    # 计算优秀率
    youxiulv=num_youxiu/s_num
    # 计算优秀率百分数
    youxiulv_persent=format(round(youxiulv,6),'.2%')
    print('总人数是：',s_num)
    print(s_sum)
    print('总分是：',s_sum['sum'])
    print(s_max)
    print('最高分是：',s_max['max'])
    print(s_min)
    print('最低分是：',s_min['min'])
    print(s_avg)
    print('平均分是：','%.1f'%(s_avg['avg']))
    print('不合格人数：',num_buhege)
    print('合格人数:',num_hege)
    print('合格率：',hegelv_persent)
    print('优秀率：',youxiulv_persent)
    print('90分以上人数：',num_youxiu)
    print('80-90分之间的人数：',num_lianghao)
    print('70-80分之间的人数：',num_yiban)
    print('60-70分之间的人数：', num_xvnuli)
    return render(request,'tongji.html',locals())