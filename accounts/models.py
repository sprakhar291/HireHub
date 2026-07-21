from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    JOB_SEEKER='job_seeker'
    RECRUITER='recruiter'

    USER_TYPE_CHOICES=[(JOB_SEEKER, 'job_seeker'), (RECRUITER, 'recruiter')]
    user_type=models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=JOB_SEEKER)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15, blank=True)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(blank=True, upload_to='profile_pictures/')
    github=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    portfolio=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Resume(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='resumes/')
    is_default = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title