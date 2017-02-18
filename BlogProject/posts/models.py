
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save  # related to slug
from django.utils.text import slugify
from django.conf import settings


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # auto_now_add True will updated when the variable is save initialy, just one time
    # auto_now will be saved any time is saved

    # If it was python 2 should be __unicode__
    def __str__(self):
        return self.title

    # to be able to get absolute URL
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})
        # return "/posts/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    # slug = slugify(instance.title)
    # # Possible slugify use case
    # # Post Item 1 -> post-item-1
    # exists = Post.objects.filter(slug=slug).exists()
    # if exists:
    #     slug = "%s-%s" %(slug, instance.id)
    # instance.slug = slug
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

