from django.contrib import admin

from techTestCodingTeam.restaurant.models import Food, FoodCategory

admin.site.register(FoodCategory)
admin.site.register(Food)
