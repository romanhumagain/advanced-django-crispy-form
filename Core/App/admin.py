from typing import Any, Callable, Optional, Sequence, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from django.utils.html import format_html 
from . forms import CandidateForm
# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm
    list_filter = ['status']
    readonly_fields = [ 'photo','firstname', 'lastname', 'job', 'email', 'age', 'phone', 'gender', 'experience', 'message' , 'salary' , 'file' ,]
    exclude = ['Status']
    list_display = ['name', 'job', 'experience', 'email', 'phone', 'age', 'created_at', 'Status' , 'image']
    search_fields = ['firstname', 'lastname', 'email']
    list_per_page = 10
    
    def image(self, obj):
        if obj.photo:
            return format_html(f'<a href="{obj.photo.url}"><img src="{obj.photo.url}" width="60" height="60" /></a>')

        return 'No Image'

    image.short_description = 'Image'
    
    def name(self, obj):
        return "%s %s" % (obj.firstname, obj.lastname)
    name.short_description = 'Full Name'  # This is the title for the column in admin
    
    def get_fields(self, request, obj: None) :
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields

    # Function to change the icon
    def is_approved(self, obj):
        if obj.status == "Approved":
            return True
        elif obj.status == "Pending":
            return None
        else:
            return False

    is_approved.boolean = True

    # Function to color the text of the status 
    def Status(self, obj):
        if obj.status == "Approved":
            color = '#28a745'
        elif obj.status == "Pending":
            color = '#fea96e'
        else:
            color = 'red'

        return format_html('<strong><p style="color:{}">{}</p></strong>', color, obj.status)
  
  

admin.site.register(Candidate, CandidateAdmin)