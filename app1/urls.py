"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views

app_name='app1'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('xueji/', include('app1.urls'))
    path('add_course/',views.add_course,name='add_course'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('add_school/',views.add_school,name='add_school'),
    path('add_grade/',views.add_grade,name='add_grade'),
    path('add_banji/',views.add_banji,name='add_banji'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_score/',views.add_score,name='add_score'),
    path('score_banji/',views.score_banji,name='score_banji'),
]
