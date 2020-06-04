from django.contrib import admin
from mainapp.models import Game, Genre, GameComment, UserGame, ComplaintGCG, Tag


class GameAdmin(admin.ModelAdmin):

    list_display = ('name', 'avatar_tag',
                    'genre_name',
                    'active',

                    'android',
                    'ios',
                    'windows',
                    'psp',
                    'xbox',
                    )
    readonly_fields = ['avatar_tag']
    list_filter = (
         # 'name',
         'added',
         'language',
         'paidContent',
         'advertising',

    )


admin.site.register(Game, GameAdmin)
admin.site.register(GameComment)
admin.site.register(Genre)
admin.site.register(UserGame)
admin.site.register(ComplaintGCG)
admin.site.register(Tag)
# admin.site.register(TegGame)

