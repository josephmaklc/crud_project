from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Person
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def my_view1(request):
    return HttpResponse("Hello world!")

def persons(request):
    logger.info("porra: "+request.method)
    if request.method == 'POST':
        data = request.POST
        last_name = data.get('last_name')
        first_name = data.get('first_name')
        age = data.get('age')

        Person.objects.create(
            last_name = last_name,
            first_name = first_name,
            age = age
        )
        return redirect('/')

    queryset = Person.objects.all()

    context = {'persons': queryset}
    return render(request, 'persons.html', context)

def update_person(request,id):
    person = get_object_or_404(Person,id=id)
    if request.method=="POST":
        data = request.POST
        last_name = data.get('last_name')
        first_name = data.get('first_name')
        age = data.get('age')

        person.last_name = last_name
        person.first_name = first_name
        person.age = age
        person.save()
        return redirect("/")

    context = {'person':person}
    return render(request,'update_person.html',context)

def delete_person(request,id):
    person = get_object_or_404(Person,id=id)
    person.delete()
    return redirect("/")
