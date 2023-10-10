from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from tinymce.models import HTMLField
from datetime import date


# Create your models here.
class Specie(models.Model):
    specie_name = models.CharField(verbose_name="Species name", max_length=200)
    description = HTMLField(verbose_name="Description", max_length=2000)
    fishs = models.ManyToManyField(to='Fish', related_name='specie')
    cover = models.ImageField(verbose_name="Cover", upload_to='covers', null=True, blank=True)

    def display_fishs(self):
        fishs = self.fishs.all()
        res = ", ".join(fish.fish_title for fish in fishs)
        return res

    def __str__(self):
        return f"{self.specie_name}"

    class Meta:
        verbose_name = "Specie"
        verbose_name_plural = "Species"


class Fish(models.Model):
    fish_title = models.CharField(verbose_name="Fish title", max_length=100)
    origin = models.CharField(verbose_name="Origin", max_length=100)
    description = models.TextField(verbose_name="Description", max_length=2000, help_text="Short fish description")
    species = models.ForeignKey("Specie", on_delete=models.SET_NULL, null=True, related_name="fishes")
    cover = models.ImageField(verbose_name="Cover", upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"{self.fish_title}"


class FishReview(models.Model):
    fish = models.ForeignKey(to="Fish", verbose_name="Zuvis", on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    reviewer = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Atsiliepimas", max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']
