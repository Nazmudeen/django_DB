from django.contrib import admin
from .models import employee



# Register your models here.
#admin.site.register(employee)


class EmployeeAdmin(admin.ModelAdmin):
    #fields=(('name','address'))
    list_display=('name','address')
    ordering=('name',)
    search_fields=('name','address')
admin.site.register(employee,EmployeeAdmin)