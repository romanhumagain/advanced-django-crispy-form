from django.contrib import admin
from .models import *
from django.utils.html import format_html 
# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ['firstname', 'lastname', 'job', 'email', 'age', 'created_at', 'Status']
    search_fields = ['firstname', 'lastname', 'email']
    list_per_page = 10

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