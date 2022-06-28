from django.contrib import admin

from core.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "gender")
    list_display_links = (
        "first_name",
        "last_name",
    )
    list_filter = ("gender",)
    search_fields = ("first_name", "last_name")
