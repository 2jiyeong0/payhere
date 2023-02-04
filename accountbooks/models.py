from django.db import models
from users.models import User

class Accountbook(models.Model):
    amount = models.PositiveIntegerField('사용 금액')
    content = models.TextField("메모", max_length=500)
    created_at = models.DateTimeField("가계부 생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("가계부 수정 시간", auto_now=True)

    author = models.ForeignKey(User, verbose_name="고객", on_delete=models.CASCADE)

    class Meta:
        db_table = "accountbook"
        ordering = ['-created_at']

    def __str__(self):
        return f"[날짜]{self.created_at}, [금액]{self.amount}"
