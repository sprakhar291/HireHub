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