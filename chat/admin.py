from django.contrib import admin
from django.contrib.admin import ModelAdmin

from chat.models import Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ['shortened', 'sent_by', 'created']
