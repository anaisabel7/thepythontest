from django.contrib import admin
from questions.models import User, Question, Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
