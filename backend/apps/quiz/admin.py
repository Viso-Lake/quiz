from django.contrib import admin
from .models import (
    Admin,
    Answer,
    Feedback,
    History,
    Options,
    Questions,
    Quiz,
    Rank,
    User,
)

admin.site.register(Admin)
admin.site.register(Answer)
admin.site.register(Feedback)
admin.site.register(History)
admin.site.register(Options)
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(Rank)
admin.site.register(User)
