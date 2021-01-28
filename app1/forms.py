from django import forms


class Add_course(forms.Form):
    course=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'课程名不能为空',
                                           'max_length':'最长不能超过20个字符'})

class Add_teacher(forms.Form):
    t_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'教师姓名不能为空',
                                           'max_length':'教师姓名最长不能超过20个字符'})
    t_sex=forms.CharField(max_length=20)
    # t_age=forms.IntegerField(max_value=80,min_value=16,
    #                          error_messages={'max_value':'最大年龄不能超过80岁',
    #                                          'min_value':'最小年龄不能低于16岁'})
    t_age=forms.CharField(max_length=20)
    course=forms.CharField(max_length=20)
    grade=forms.CharField(max_length=20)


class Add_school(forms.Form):
    s_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'必须添加学校名称',
                                          'max_value':'不能超过20个字符'})
    s_master=forms.CharField(max_length=20)


class Add_grade(forms.Form):
    g_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'必须添加年级段',
                                          'max_value':'不能超过20个字符'})
    school=forms.CharField(max_length=20)
    g_master=forms.CharField(max_length=20)


class Add_banji(forms.Form):
    b_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'必须添加班级',
                                          'max_value':'不能超过20个字符'})
    grade=forms.CharField(max_length=20)
    b_master=forms.CharField(max_length=20)

class Add_student(forms.Form):
    s_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'必须添加学生姓名',
                                          'max_value':'不能超过20个字符'})
    s_sex=forms.CharField(max_length=20)
    s_age=forms.CharField(max_length=20)
    grade=forms.CharField(max_length=20)
    banji=forms.CharField(max_length=20)

class Add_score(forms.Form):
    s_name=forms.CharField(max_length=20,required=True,
                           error_messages={'required':'必须填写考试名称',
                                          'max_value':'不能超过20个字符'})
    course=forms.CharField(max_length=20)
    grade=forms.CharField(max_length=20)
    banji = forms.CharField(max_length=20)
    student=forms.CharField(max_length=20)
    s_time=forms.DateField()
    s_value=forms.CharField(max_length=20)