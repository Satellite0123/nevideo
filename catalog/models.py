from django.db import models
# from django.conf import settings

# Create your models here.

class VideoData(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    published_on = models.DateField()
    link = models.URLField()
    host = models.CharField(max_length=20)
    language = models.CharField(max_length=10)
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    votes = models.PositiveIntegerField()
    comments_count = models.PositiveIntegerField()
    # from_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Category(models.Model):
    language = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    last_updated = models.DateField()
    works_num = models.IntegerField()
    videos_num = models.IntegerField()

# class PatientsApplications(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     message = models.TextField()
#     is_opened = models.IntegerField()
#     created_at = models.DateTimeField()
#     family_doctor = models.ForeignKey(Doctor, related_name='family_doctor', on_delete=models.DO_NOTHING, null=True)
#     doctor = models.ForeignKey(Doctor, related_name='doctor', on_delete=models.DO_NOTHING, blank=True, null=True)
#     hospital = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
