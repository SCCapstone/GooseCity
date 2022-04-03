from django.db import models

from backstage.models import cart


class Payment(models.Model):
    """
    Paymentinfor
    """
    order = models.ForeignKey(cart, on_delete=models.CASCADE, verbose_name='Order')
    trade_id = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Paymentnumber")

    class Meta:
        db_table = 'tb_payment'
        verbose_name = 'Paymentinfor'
        verbose_name_plural = verbose_name
