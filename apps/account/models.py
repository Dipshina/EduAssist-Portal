import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.commons.models import BaseModel

class User(AbstractUser):
    username = models.CharField(default=uuid.uuid4, max_length=100, blank=True)
    email = models.EmailField(unique=True)
    middle_name = models.CharField(null=True, blank=True, max_length=50)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.email
    
class EmailVerificationKey(BaseModel):
    key = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_activation_key')

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile_picture/")
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    school_college = models.CharField(max_length=100, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    year_of_study = models.CharField(max_length=10, null=True, blank=True)
    graduation_year = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return f"Profile of {self.user.email}"

