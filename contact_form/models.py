from django.db import models


class Contact(models.Model):

    from_email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.message
