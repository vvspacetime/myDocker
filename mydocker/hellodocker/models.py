from django.db import models

class RtCatApp(models.Model):
    create_date = models.DateTimeField('date create',auto_now=True)
    def __str__(self):
        return self.create_date.__str__()
