from django.db import models
from UserApp.models import UserProfile
from CategoryApp.models import Category
from django.utils.text import slugify

class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/', null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)