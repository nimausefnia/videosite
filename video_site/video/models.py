from django.db import models

class Video(models.Model):
    title=models.CharField(max_length=10)
    date_posted=models.DateTimeField(auto_now_add=True)
    video_file=models.FileField(upload_to='uploads')
    thumbnail_file=models.FileField(upload_to='uploads')


    def __str__(self) -> str:
        return self.title
