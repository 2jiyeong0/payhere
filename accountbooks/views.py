from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accountbooks.models import Accountbook
from accountbooks.serializers import AccountbookCreateSerializer, AccountbookDetailSerializer

class AccountbookView(APIView):
    permission_classes = [IsAuthenticated]

    # 가계부 작성
    def post(self, request):
        serializer = AccountbookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountbookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # 가계부 상세 조회
    def get(self, request, accountbook_id):
        accountbook = get_object_or_404(Accountbook, id=accountbook_id)
        if request.user == accountbook.author:
            serializer = AccountbookDetailSerializer(accountbook)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "접근 권한 없음"}, status=status.HTTP_403_FORBIDDEN)

    # 가계부 수정
    def put(self, request, accountbook_id):
        accountbook = get_object_or_404(Accountbook, id=accountbook_id)
        if request.user == accountbook.author:
            serializer = AccountbookCreateSerializer(accountbook, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "접근 권한 없음"}, status=status.HTTP_403_FORBIDDEN)

    # 가계부 삭제
    def delete(self, request, accountbook_id):
        accountbook = get_object_or_404(Accountbook, id=accountbook_id)
        if request.user == accountbook.author:
            accountbook.delete()
            return Response({"message": "삭제 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "접근 권한 없음"}, status=status.HTTP_403_FORBIDDEN)

