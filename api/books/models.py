from django.db import models


class Book(models.Model):
    title = models.CharField(
        verbose_name="Título do Livro",
        max_length=255,
        blank=False,
        null=False,
    )
    author = models.CharField(
        verbose_name="Autor",
        max_length=255,
        blank=False,
        null=False,
    )
    description = models.TextField(verbose_name="Descrição / Sumário")
    is_available = models.BooleanField(
        verbose_name="Disponivel para emprestimo.",
        default=False,
    )
    pages = models.PositiveBigIntegerField(
        verbose_name="Quantidade de páginas",
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
