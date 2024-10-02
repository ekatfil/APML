from django.db import models

class TextInput(models.Model):
    text = models.TextField("Запрос")
    result = models.BooleanField("Результат")

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return f"{ self.result }: { self.text }"
