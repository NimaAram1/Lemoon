from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .forms import UserCreateFormAdmin, UserChangeFormAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# get user model 
User = get_user_model()

class UserAdmin(BaseAdmin):
    add_form = UserCreateFormAdmin
    form = UserChangeFormAdmin
    list_display = ["email","first_name","last_name","birth_date","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields":["email"]}),
        ("اطلاعات شخصی", {"fields":["first_name","last_name","birth_date"]}),
        ("دسترسی ها", {"fields":["is_admin","is_active"]}),
    ]
    add_fieldsets = [
        (None, {"fields":["email","first_name","last_name",
        "birth_date","password","repeated_password"]})
    ]
    
    search_fields = ["email","last_name"]
    ordering = ["-is_admin","email"]
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)    