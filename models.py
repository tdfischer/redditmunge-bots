from django.db import models

class Bot(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    description = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('bot_details', [self.username])

    @models.permalink
    def get_edit_url(self):
        return ('edit_bot', [self.username])

    def __unicode__(self):
        return self.username
