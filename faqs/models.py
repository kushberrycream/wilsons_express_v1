from django.db import models


# Create your models here.
class Faqs(models.Model):
    class Meta:
        verbose_name_plural = "FAQ's"

    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=254)
    answer = models.TextField()
    urls = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return self.question
