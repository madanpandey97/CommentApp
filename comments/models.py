from django.db import models
from core.models import User, TimeStampModel
from ckeditor.fields import RichTextField

# Create your models here.


class SubComment(TimeStampModel):
    text = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}----{self.id}"


class Comment(models.Model):
    name = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_comment = models.ManyToManyField(SubComment, blank=True)

    def __str__(self):
        return f"{self.user}----{self.id}"



