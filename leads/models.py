from django.db import models
from django.db.models.signals import post_save  # User 만들면 자동으로 User Profile 만들어주기 위해. pre_save도 있으나 우리는 post_save 이용할 꺼
from django.contrib.auth.models import AbstractUser #User만들때 사용
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    # When you make an account, you are dafault organizer
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    # if user creates an account, he only has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #Agent is optional
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    #One Agent can have only one User
    #User가 지워지면 Agent가 지워짐
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # If the UserProfile is deleted, all the agents are deleted as well. 
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


# Create User Profile
# instance로 User를 받음
def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)    # created : T(새로 생성), F(단순 수정, save만 누름 등) 
    if created:
        UserProfile.objects.create(user=instance)


# Django Signal 사용해보기. 
# save가 끝난 후 작동함
post_save.connect(post_user_created_signal, sender=User)