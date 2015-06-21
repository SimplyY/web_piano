from django.contrib import admin

# Register your models here.
from django.contrib import admin
from piano.models import *

admin.site.register(User)
admin.site.register(Piano)
admin.site.register(Comment)

