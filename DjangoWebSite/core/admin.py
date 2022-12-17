from django.contrib import admin

from .models import *


class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'file')
    list_display_links = ('id', 'message', 'title')
    search_fields = ('title', 'message')


admin.site.register(Files, FilesAdmin)
admin.site.register(Messages, MessagesAdmin)
