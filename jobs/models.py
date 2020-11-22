from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(editable=False, default=None)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def job_count(self):
        return self.jobs.all().count() * 500

class Job(models.Model):

    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    )
    job_type = models.CharField(max_length=20,blank=True, default=None, choices=CHOICES)
    location = models.CharField(max_length=300, blank=True, default=None)
    description = models.TextField(blank=True, default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, default=None)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)


    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-id',)