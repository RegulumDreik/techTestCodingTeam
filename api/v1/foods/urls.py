from django.urls import path

from api.v1.foods.views import FoodsAPI

urlpatterns = [
    path('', FoodsAPI.as_view()),
]
