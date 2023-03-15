from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Post(models.Model):

    post_text = models.CharField(max_length=138)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='posts')
    
    def __str__(self):
        return(
            f'{self.author} '
            f'({self.created_date:%Y-%m-%d %H:%M}): '
            f'{self.post_text}...'
        )
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    following = models.ManyToManyField('self', 
                                      related_name='followed_by', 
                                      symmetrical=False,
                                      blank=True)
    
    def __str__(self):
        return self.user.username
    

# Auto-generate Profile on new User Registration
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # Auto-follow self
        user_profile.following.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)