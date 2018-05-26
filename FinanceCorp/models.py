from django.db import models
from django.db.models import CASCADE


class Lender(models.Model):
    firstname = models.CharField(default='', max_length=100)
    surname = models.CharField(max_length=20, default='')
    amount = models.PositiveIntegerField()
    interest = models.PositiveIntegerField()
    duedate = models.DateField(max_length=10)
    reminddate = models.PositiveSmallIntegerField(null=True)
    interestamount = models.PositiveIntegerField()
    dueamount = models.PositiveIntegerField()
    type = models.CharField(max_length=10, default='lender')

    def __str__(self):
        outputstring = 'firstname : {0}, surname : {1}, amount : {2}, interest : {3}, duedate : {4}, reminddate : {5}, interestamount : ' \
                       '{6}, due : {7}'.format(self.firstname, self.surname, self.amount, self.interest,
                                               self.duedate, self.reminddate, self.interestamount, self.dueamount)
        return outputstring


class LenderPaymentDetails(models.Model):
    lenderID = models.ForeignKey(Lender, on_delete=CASCADE)
    paymentDate = models.DateField(null=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'paymentID : {self.pk} LenderID : {self.lenderID.id} PaymentDate : {self.paymentDate} amount : {self.amount}'


class Payee(models.Model):
    firstname = models.CharField(max_length=100, default='')
    surname = models.CharField(max_length=20, default='')
    amount = models.PositiveIntegerField()
    interest = models.PositiveIntegerField()
    period = models.PositiveSmallIntegerField()
    duedate = models.DateField(max_length=10)
    reminddate = models.PositiveSmallIntegerField(null=True)
    interestamount = models.PositiveIntegerField()
    dueamount = models.PositiveIntegerField()
    type = models.CharField(max_length=10, default='payee')

    def __str__(self):
        outputstring = 'firstname : {0}, surname : {1}, amount : {2}, interest : {3}, duedate : {4}, period : {5}, ' \
                       'reminddate : {6}, interestamount : {7}, due : {8}'.format(self.firstname, self.surname, self.amount,
                                                                                  self.interest, self.duedate, self.period,
                                                                                  self.reminddate, self.interestamount, self.dueamount)
        return outputstring


class PayeePaymentDetails(models.Model):
    payeeID = models.ForeignKey(Payee, on_delete=CASCADE)
    paymentDate = models.DateField(null=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'Payee Id: {self.payeeID}, Amount: {self.amount}, Payment Date: {self.paymentDate}'