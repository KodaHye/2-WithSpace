from django.contrib import admin
from .models import Space, Booking, Review, Question, Answer

admin.site.register(Space)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Answer)