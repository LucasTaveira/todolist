from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_OPTIONS = {
        "O": "Open",
        "C": "Closed",
    }
    title = models.CharField(
        verbose_name="Titulo da Tarefa", max_length=50, blank=False, null=False)
    description = models.TextField(
        verbose_name="Descrição", blank=True, null=True)
    status = models.CharField(
        max_length=1,
        verbose_name="Status", choices=STATUS_OPTIONS, default="O",
        help_text="O para Open, C para Closed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.title} - {self.STATUS_OPTIONS[self.status]}"