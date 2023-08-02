from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=9999) # 제목
    country = models.CharField(max_length=15) # 장르
    url = models.URLField() # 주소
    img = models.CharField(max_length=9999) # 제목
    visite_count = models.IntegerField(default=0)
    created_at = models.CharField(max_length=30)

    def __str__(self):
        return self.title