from django.contrib import admin
from materials.models import Treatise, Lesson

@admin.register(Treatise)
class TreatiseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "description", "owner",)
    list_filter = ("name","description",)
    search_fields = ("id", "name", "owner",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "link_to_video", "treatise", "description", "owner",)
    list_filter = ("name", "treatise",)
    search_fields = ("id", "name", "owner", "treatise",)