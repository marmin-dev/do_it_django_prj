from django.db import models
import os

class Post(models.Model):
    """
    게시물
    """
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
    # 처음 레코드가 생성될 때 현재 시간 추가
    created_at = models.DateTimeField(auto_now_add=True)
    # 레코드가 업데이트 될 때 현재 시간으로
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}].{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]