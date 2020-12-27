from django.contrib import admin
from .models import User,Message
from django.contrib.auth.admin import UserAdmin

class User_Admin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('id','date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(User,User_Admin)

# Register your models here.
#<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
#<script src="http://91.234.35.26/iwiki-admin/v1.0.0/admin/js/jquery.nicescroll.min.js"></script>
