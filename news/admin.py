from django.contrib import admin

# Register your models here.
from news.models import New, NewComment, ComplaintGCN

admin.site.register(New)
admin.site.register(NewComment)
admin.site.register(ComplaintGCN)

