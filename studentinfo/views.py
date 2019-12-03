from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import student

def displayinformation(request,rrr):
   # print(rrr)
    template=loader.get_template("studentdetails.html")
    prod=student.objects.get (rollno=rrr)

    data = {"rollno":prod.rollno,
            "name":prod.name,
            "course":prod.course,
            "year":prod.year,
            "gtname":prod.gtname,
            }
    res = template.render(data, request)
    return HttpResponse(res)
def studentdetails(request):
    template = loader.get_template("student.html")
    students = student.objects.all()
    mydata = {"student": students}
    res = template.render(mydata, request)
    return HttpResponse(res)
# Create your views here.
