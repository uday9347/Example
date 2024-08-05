from django.contrib import admin
from testapp.models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display=['fname','lname','uname','em','passw','repassw']

admin.site.register(Login,LoginAdmin)