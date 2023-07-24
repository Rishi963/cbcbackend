from django.contrib import admin
from backend.models import *
# Register your models here.

admin.site.register(Studentreg)
admin.site.register(Branch)
admin.site.register(Reference)
admin.site.register(Course)

admin.site.site_header = "STUDI BREEZE"
admin.site.index_title = "Welcome"
admin.site.site_title = "Admin Panel"