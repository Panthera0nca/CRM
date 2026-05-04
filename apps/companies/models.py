from django.db import models


class Company(models.Model):
    INDUSTRY_CHOICES = [
        ('tech', 'Tecnología'),
        ('finance', 'Finanzas'),
        ('health', 'Salud'),
        ('retail', 'Retail'),
        ('education', 'Educación'),
        ('other', 'Otro'),
    ]
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.name
