from django.contrib import admin
from .models import Business
from .models import Review
from .models import User
from .models import Profile




# Register your models here.

admin.site.register(Business)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Profile)