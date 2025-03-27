from django.db import models

class Post(models.Model):
    """
    게시물
    """
    title = models.CharField(max_length=30)
    content = models.TextField()

    # 처음 레코드가 생성될 때 현재 시간 추가
    created_at = models.DateTimeField(auto_now_add=True)
    # 레코드가 업데이트 될 때 현재 시간으로
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}].{self.title}'