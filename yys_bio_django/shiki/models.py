from django.db import models
from django.utils.html import mark_safe


class Role(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def icon_image(self):
        return mark_safe('<img src=%s style="background-color:red;"/>' % self.icon.url)


class Lane(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Shiki(models.Model):
    name = models.CharField(max_length=200)
    GENDER = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    gender = models.CharField(choices=GENDER)
    avatar = models.ImageField(blank=True)
    role_ids = models.ManyToManyField(Role, blank=True)
    lane_ids = models.ManyToManyField(Lane, blank=True)
    fav_point = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_roles(self):
        return "\n".join([r.name for r in self.role_ids.all()])

    def get_lanes(self):
        return "\n".join([lane.name for lane in self.lane_ids.all()])

    def avatar_image(self):
        return mark_safe('<img src=%s />' % self.avatar.url)
    avatar_image.short_description = "Avatar"
