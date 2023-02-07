import sys
import django
import json
from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.db import models
from django.template import Template, Context
from django.utils.crypto import get_random_string

settings.configure(
    DEBUG=True,
    IGNORABLE_404_URLS=[r'^favicon\.ico$'],
    ROOT_URLCONF=sys.modules[__name__],
    INSTALLED_APPS = [__name__],
    SECRET_KEY=get_random_string(50),
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
],
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.filebased.FileBasedDB',
            'NAME': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite3'),
        }
    },
)

django.setup()

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    completed_status = models.BooleanField(default=False)

class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['description']

def index(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GroceryItemForm()

    items = GroceryItem.objects.filter(completed_status=False)
    completed_items = GroceryItem.objects.filter(completed_status=True)
    context = {'items': items, 'completed_items': completed_items, 'form': form}
    
    template = Template("""
        <h1>Grocery List</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save</button>
        </form>
        <h2>Incomplete Items</h2>
        <ul>
            {% for item in items %}
                <li>{{ item.description }}</li>
            {% endfor %}
        </ul>
        <h2>Complete Items</h2>
        <ul>
            {% for item in completed_items %}
                <li>{{ item.description }}</li>
            {% endfor %}
        </ul>
    """)
    return HttpResponse(template.render(Context(context)))

def complete_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.completed_status = True
    item.save()
    return redirect('index')

def undo_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.completed_status = False
    item.save()
    return redirect('index')


def delete_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')

urlpatterns = [
path('', index, name='index'),
path('complete/int:item_id/', complete_item, name='complete_item'),
path('undo/int:item_id/', undo_item, name='undo_item'),
path('delete/int:item_id/', delete_item, name='delete_item'),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)