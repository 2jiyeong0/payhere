from rest_framework import serializers
from accountbooks.models import Accountbook

class AccountbookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountbook
        fields = ["amount", "content"]