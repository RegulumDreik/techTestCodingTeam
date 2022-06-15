from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from api.v1.foods.serializer import FoodListSerializer
from techTestCodingTeam.restaurant.models import Food, FoodCategory


class FoodsAPI(ListAPIView):
    """Food api view."""

    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(
        food__is_publish=True,
    ).prefetch_related(
        Prefetch(
            'food',
            Food.objects.filter(is_publish=True),
        ),
    )
