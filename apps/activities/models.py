from django.db import models


class Activity(models.Model):
    TYPE_CHOICES = [
        ('call', 'Llamada'),
        ('email', 'Email'),
        ('meeting', 'Reunión'),
        ('note', 'Nota'),
    ]
    activity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    date = models.DateTimeField()
    deal = models.ForeignKey(
        'deals.Deal', null=True, blank=True,
        on_delete=models.CASCADE, related_name='activities'
    )
    contact = models.ForeignKey(
        'contacts.Contact', null=True, blank=True,
        on_delete=models.CASCADE, related_name='activities'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

    def __str__(self):
        return f"{self.get_activity_type_display()} - {self.date:%Y-%m-%d}"
