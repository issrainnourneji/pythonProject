from django.contrib import admin
from .models import *

# Register your models here.
class EventAdmin (admin.ModelAdmin) : 
    list_display =(
        'username',
        'email'
    )
    ordering= ('username',)
    list_filter = ('email', )
    fieldsets =(
        (   'CLE',
            {
                'classes':('collapse',),
                'fields': (('password',))
            } )
    ,
    (
        'ABOUT',
        {
            'fields':(
                'username',
                'email'
            )
        }
    )
    )
admin.site.register(Person , EventAdmin)
