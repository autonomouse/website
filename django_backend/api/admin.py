from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered


# Register any models that have not been explicitly registered:
for model in apps.get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
