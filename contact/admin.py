from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """
    Instruct admin what to display
    """
    # list_display tuple tells admin which fields to display in admin
    list_display = (
        'full_name',
        'email',
        'message',
    )

    ordering = ('full_name',)


# Register models along with their respective classes
admin.site.register(Message, MessageAdmin)
