from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.c_name

    class Meta:
        db_table='course'

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    t_name=models.CharField(max_length=20,null=False)
    t_sex=models.CharField(max_length=10,blank=True,null=True)
    t_age=models.IntegerField(blank=True,null=True)
    course=models.ForeignKey('Course',on_delete=models.CASCADE,
                                related_name='teacher1',db_column='c_id',
                             null=True,blank=True)
    grade=models.ForeignKey('Grade',on_delete=models.CASCADE,
                                related_name='teacher2',db_column='g_id',
                             null=True,blank=True)

    def __str__(self):
        return self.t_name

    class Meta:
        db_table='teacher'

class School(models.Model):
    id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=20,null=False)
    master=models.ForeignKey('Teacher',on_delete=models.CASCADE,
                             db_column='m_id',related_name='school',
                             blank=True,null=True)

    def __str__(self):
        return self.s_name

    class Meta:
        db_table='school'

class Grade(models.Model):
    id=models.AutoField(primary_key=True)
    g_name=models.CharField(max_length=20,null=False)
    school=models.ForeignKey('School',on_delete=models.CASCADE,
                             db_column='s_id',related_name='grade1',
                             blank=True,null=True)
    g_master=models.ForeignKey('Teacher',on_delete=models.CASCADE,
                               db_column='gm_id',related_name='grade2',
                               blank=True,null=True)

    def __str__(self):
        return self.g_name

    class Meta:
        db_table='grade'

class Banji(models.Model):
    id=models.AutoField(primary_key=True)
    b_name=models.CharField(max_length=20,null=False)
    grade=models.ForeignKey('Grade',on_delete=models.CASCADE,
                               db_column='g_id',related_name='banji1',
                               blank=True,null=True)
    b_master=models.ForeignKey('Teacher',on_delete=models.CASCADE,
                               db_column='t_id',related_name='banji2',
                               blank=True,null=True)

    def __str__(self):
        return self.b_name

    class Meta:
        db_table='banji'

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=20,null=False)
    s_sex=models.CharField(max_length=10,null=True)
    s_age=models.IntegerField(null=True)
    grade = models.OneToOneField('Grade', on_delete=models.CASCADE,
                                 db_column='g_id', related_name='student1',
                                 blank=True, null=True)
    banji=models.OneToOneField('Banji',on_delete=models.CASCADE,
                               db_column='b_id',related_name='student2',
                               blank=True,null=True)

    def __str__(self):
        return self.s_name

    class Meta:
        db_table='student'

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=30,null=True,blank=True)
    course=models.ForeignKey('Course',on_delete=models.CASCADE,
                               db_column='c_id',related_name='score1',
                               null=False)
    s_value=models.FloatField(null=True)
    student=models.ForeignKey('Student',on_delete=models.CASCADE,
                               db_column='s_id',related_name='score2',
                               null=False)
    s_time=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.s_name

    class Meta:
        db_table='score'

