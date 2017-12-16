from django.db import models


# Create your models here.



class PingJobuid(models.Model):
    PingGuid = models.CharField(max_length=120)
    State = models.CharField(max_length=120, default='started')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PingGuid


class Serveriplist(models.Model):
    Iplist = models.CharField(max_length=120)
    Sent = models.CharField(max_length=120, null=True)
    Recieved = models.CharField(max_length=120, null=True)
    Lost = models.CharField(max_length=120, null=True)
    Ping_Job = models.ForeignKey(PingJobuid, null=True)

    def __str__(self):
        return self.Iplist
