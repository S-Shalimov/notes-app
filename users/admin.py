from django.contrib import admin
from .models import Note, Profile, TODO, Note


admin.site.register(Profile)
admin.site.register(TODO)
admin.site.register(Note)