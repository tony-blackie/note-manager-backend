from django.contrib import admin
from .models import User, Note, Hashtag, Person, Questionnaire

admin.site.register(Person)
# admin.site.register(Folder)
admin.site.register(Hashtag)
admin.site.register(Note)
admin.site.register(Questionnaire)