from rest_framework import serializers
from accountbooks.models import Accountbook

# 가계부 리스트 조회
class AccountbookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.email

    class Meta:
        model = Accountbook
        fields = "__all__"


# 가계부 생성
class AccountbookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountbook
        fields = ["amount", "content"]


# 가계부 상세 조회
class AccountbookDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.email

    class Meta:
        model = Accountbook
        fields = "__all__"
