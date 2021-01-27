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


def add_score(request):
    return None


def score_banji(request):
    grade=models.Grade.objects.all()
    if request.method=='POST':
        g=request.POST.get('grade')
        b=request.POST.get('banji')
        return render(request,'add_score.html',{'grade':g,'banji':b})
    return render(request,'score_banji.html',locals())