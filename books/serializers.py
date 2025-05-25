from rest_framework import serializers
from .models import Book, PriceHistory

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ['price', 'date_updated']

        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be positive")
            return value
        
class BookSerializer(serializers.ModelSerializer):
    price_history = PriceHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'language', 'publication_date']