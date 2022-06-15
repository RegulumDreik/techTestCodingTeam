from rest_framework import serializers

from techTestCodingTeam.restaurant.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    """Serializer for food model."""

    additional = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='internal_code',
    )

    class Meta:
        """Class meta info."""

        model = Food
        fields = (
            'internal_code',
            'code',
            'name_ru',
            'description_ru',
            'description_en',
            'description_ch',
            'is_vegan',
            'is_special',
            'cost',
            'additional',
        )


class FoodListSerializer(serializers.ModelSerializer):
    """Serializer for list of food categories."""

    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        """Class meta info."""

        model = FoodCategory
        fields = (
            'id',
            'name_ru',
            'name_en',
            'name_ch',
            'order_id',
            'foods',
        )
