from django.contrib import admin
from .models import Likes, DisLikes , Comments , Articles
# Register your models here.
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(DisLikes)
admin.site.register(Likes)
