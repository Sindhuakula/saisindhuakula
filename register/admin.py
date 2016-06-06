from django.contrib import admin

# Register your models here.
from register.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)