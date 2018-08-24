from django.contrib import admin
from game.models import Game, Scenario


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'scenario', 'status']


class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Game, GameAdmin)
admin.site.register(Scenario, ScenarioAdmin)
