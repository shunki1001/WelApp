from django.contrib import admin

from welapp.models import WelModel
from .models import WelModel

# Register your models here.

admin.site.register(WelModel)