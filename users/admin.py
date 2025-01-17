from django.contrib import admin

from users.models import User, Subs


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email",)


@admin.register(Subs)
class SubsAdmin(admin.ModelAdmin):
    list_display = ("user", "treatise",)
