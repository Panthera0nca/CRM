from django.db import models


class Deal(models.Model):
    STAGE_CHOICES = [
        ('lead', 'Lead'),
        ('qualified', 'Calificado'),
        ('proposal', 'Propuesta'),
        ('won', 'Ganado'),
        ('lost', 'Perdido'),
    ]
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='lead')
    contact = models.ForeignKey(
        'contacts.Contact', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='deals'
    )
    company = models.ForeignKey(
        'companies.Company', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='deals'
    )
    close_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'negocio'
        verbose_name_plural = 'negocios'

    def __str__(self):
        return self.title
