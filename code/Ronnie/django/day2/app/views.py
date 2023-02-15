from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, City
# Create your views here.
def find_city(request):
    contacts = Contact.objects.get(id=1)
    return HttpResponse(contacts.city.name)

def create_user(request):
    users_city = City.objects.get(id=1)
    if users_city.exist():
        new_contact = Contact(email_address="merrit@email.com", first_name="merrit", last_name="Lawerence", city=users_city)
    
    new_city = City(name="user_input")

def index(request):
    contacts = Contact.objects.order_by('first_name', '-first_name')[:5]