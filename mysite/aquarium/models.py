from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Specie(models.Model):
    specie_name = models.CharField(verbose_name=_("Species name"), max_length=200)
    description = HTMLField(verbose_name=_("Description"), max_length=5000)
    fishs = models.ManyToManyField(to='Fish', related_name='specie')
    cover = models.ImageField(verbose_name=_("Cover"), upload_to='covers', null=True, blank=True)

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
    fish_title = models.CharField(verbose_name=_("Fish title"), max_length=150)
    origin = models.CharField(verbose_name=_("Origin"), max_length=150)
    description = models.TextField(verbose_name=_("Description"), max_length=5000, help_text=_("Short fish description"))
    species = models.ForeignKey("Specie", on_delete=models.SET_NULL, null=True, related_name="fishes")
    cover = models.ImageField(verbose_name=_("Cover"), upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"{self.fish_title}"

    def num_reviews(self):
        return self.reviews.count()


class FishReview(models.Model):
    fish = models.ForeignKey(to="Fish", verbose_name="Zuvis", on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='reviews')
    reviewer = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=2000)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _('Reviews')
        ordering = ['-date_created']


class Profilis(models.Model):
    user = models.OneToOneField(to=User, verbose_name=_("User"), on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", verbose_name="Nuotrauka",
                                  upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    class Meta:
        verbose_name = "Profilis"
        verbose_name_plural = 'Profilis'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.nuotrauka.path)
