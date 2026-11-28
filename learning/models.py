from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class LearnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='learner_profile')
    coins = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.coins} coins'


class StudyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_progress')
    year = models.PositiveSmallIntegerField()
    subject_slug = models.SlugField(max_length=30)
    unit_slug = models.SlugField(max_length=60, default='core')
    best_score = models.PositiveSmallIntegerField(default=0)
    question_count = models.PositiveSmallIntegerField(default=0)
    coins_awarded = models.PositiveSmallIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['year', 'subject_slug', 'unit_slug']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'year', 'subject_slug', 'unit_slug'],
                name='unique_user_course_unit_progress',
            ),
            models.CheckConstraint(condition=Q(best_score__lte=models.F('question_count')), name='best_score_not_over_question_count'),
        ]


class LearnerPet(models.Model):
    PET_CHOICES = [
        ('comet_fox', 'Comet Fox'),
        ('moon_cat', 'Moon Cat'),
        ('cloud_bunny', 'Cloud Bunny'),
        ('star_owl', 'Star Owl'),
        ('nebula_axolotl', 'Nebula Axolotl'),
        ('sun_turtle', 'Sun Turtle'),
        ('aurora_dragon', 'Aurora Dragon'),
        ('crystal_deer', 'Crystal Deer'),
        ('ringed_lynx', 'Ringed Lynx'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learner_pets')
    egg_type = models.CharField(max_length=30, default='egg_stardust')
    species = models.CharField(max_length=30, choices=PET_CHOICES, blank=True)
    name = models.CharField(max_length=24, blank=True)
    is_favorite = models.BooleanField(default=False)
    acquired_at = models.DateTimeField(auto_now_add=True)
    hatched_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-acquired_at']

    @property
    def is_egg(self):
        return not self.species


class LearnerInventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_inventory')
    item_slug = models.SlugField(max_length=40)
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'item_slug'], name='unique_user_shop_item'),
        ]
