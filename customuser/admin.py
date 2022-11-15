from django.contrib import admin

# Register your models here.
from .models import *   # will import all classes

# Register your models here.
admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Contact)

