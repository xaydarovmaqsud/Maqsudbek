from django.db import models

class Balance(models.Model):
    user = models.OneToOneField('account.User',on_delete=models.SET_NULL,null=True)
    value = models.FloatField(default=0)

class Payment(models.Model):
    balance = models.ForeignKey('payment.Balance',on_delete=models.SET_NULL,null=True,related_name='payments')
    cashier = models.ForeignKey('account.User',on_delete=models.SET_NULL,null=True,related_name='input_payments')
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
