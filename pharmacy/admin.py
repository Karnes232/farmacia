from django.contrib import admin
from .models import User, Posts, Sales, Inventroy

# Register your models here.

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Sales)
admin.site.register(Inventroy)