from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약 사항

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

# 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정!
# makemigrations => 모델의 변경사항을 추적해서 기록
# 마이그레이션(migrate) => 데이터베이스에 모델의 내용을 반영(테이블 생성)
# Create your models here.
