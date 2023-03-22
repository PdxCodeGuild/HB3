from django.apps import AppConfig


class GroceryListConfig(AppConfig):
    #code to start my sepcifc configs, deals with the data, and allows more django keys
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grocery_list'
