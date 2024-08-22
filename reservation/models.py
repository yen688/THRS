from django.db import models

# Create your models here.
# 建立reserve資料表，包括id、name、phone、date、time、level等欄位
class Reserve(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.TimeField()
    level = models.CharField(max_length=50)

    class Meta:
        db_table = 'reserve'
        ordering = ['date', 'time']

    def __str__(self):
        return self.name