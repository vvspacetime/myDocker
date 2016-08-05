from django.db import models

class RtCatApp(models.Model):
    create_date = models.DateTimeField('date create',auto_now=True)
    number = models.IntegerField('app number',default=0)
    def __str__(self):
        return self.create_date.__str__()
