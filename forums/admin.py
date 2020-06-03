from django.contrib import admin
from forums.models import ForumsComment, ForumsTema, ForumsRazdel, ComplaintGCF


admin.site.register(ForumsComment)
admin.site.register(ForumsTema)
admin.site.register(ForumsRazdel)
admin.site.register(ComplaintGCF)


# Register your models here.
