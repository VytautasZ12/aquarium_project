from django.db import models


# Create your models here.
class Species(models.Model):
    specie_name = models.CharField(verbose_name="Species name", max_length=100)
    description = models.TextField(verbose_name="Description", max_length=1000)

    def display_fish(self):
        fishs = self.fish.all()
        res = ", ".join(fish.fish_title for fish in fishs)
        return res

    def __str__(self):
        return self.specie_name

    class Meta:
        verbose_name = "Species"
        verbose_name_plural = "Species"


class Fish(models.Model):
    fish_title = models.CharField(verbose_name="Fish title", max_length=100)
    origin = models.CharField(verbose_name="Origin", max_length=50)
    description = models.TextField(verbose_name="Description", max_length=1000, help_text="Short fish description")
    species = models.ForeignKey("Species", on_delete=models.SET_NULL, null=True, related_name="fish")

    def __str__(self):
        return self.fish_title
