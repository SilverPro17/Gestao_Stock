from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto

MOVIMENTO = (
    ('e', 'Entrada'),
    ('s', 'Saída'),
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('Número de Fatura', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%y'))

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})

    @property
    def nf_formated(self):
        return str(self.nf).zfill(3)


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='itens'  # Corrigido o related_name
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
