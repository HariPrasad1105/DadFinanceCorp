from django.contrib import admin
from .models import Lender, Payee, LenderPaymentDetails, PayeePaymentDetails

# Register your models here.


admin.site.register(Lender)
admin.site.register(Payee)
admin.site.register(LenderPaymentDetails)
admin.site.register(PayeePaymentDetails)