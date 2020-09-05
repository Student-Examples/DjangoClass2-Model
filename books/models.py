from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год", default=2015)
    author = models.CharField(max_length=255, verbose_name="Автор",
                              null=True, blank=True)

    class Meta:
        ordering = ["year"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

