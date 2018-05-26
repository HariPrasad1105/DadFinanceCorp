import datetime
from twilio.rest import Client
import os
import django

account_sid = "ACf2098cc5548541a9ce1d326787796a9e"
auth_token = "30e7b182c401dc85b73421e7f06a8783"

client = Client(account_sid, auth_token)


def send_lender_message(lender_object):
        today = int(datetime.datetime.now().strftime("%d"))
        print(lender_object)
        for i in lender_object:
            if i.reminddate - today == 3:
                msg = "Daddy, This is a reminder to  Collect " + str(i.interestamount) + ' from ' + str(
                    i.firstname) + ' on ' + str(i.duedate) + '. Due Amount: ' + str(i.dueamount)
                message = client.messages.create(
                    body=msg,
                    from_="+12014256211",
                    to="+919866482608"
                )
                print(message.sid)
            if i.reminddate - today == 0:
                msg = "Daddy, Collect " + str(i.interestamount) + ' from ' + str(i.firstname) + ". Due Amount: " + str(
                    i.dueamount)
                message = client.messages.create(
                    body=msg,
                    from_="+12014256211",
                    to="+919866482608"
                )
                i.dueamount += i.interestamount
                i.save()
                print(message.sid)


def send_payee_message(payee_object):
        today = int(datetime.datetime.now().strftime('%d'))
        for i in payee_object:
            if i.reminddate - today == 3:
                msg = "Daddy, This is a reminder to  Collect " + str(i.interestamount) + ' from ' + str(
                    i.firstname) + ' on ' + str(i.duedate) + '. Due Amount: ' + str(i.dueamount)
                message = client.messages.create(
                    body=msg,
                    from_="+12014256211",
                    to="+919866482608"
                )
                print(message.sid)
            if i.reminddate - today == 0:
                msg = "Daddy, Collect " + str(i.interestamount) + ' from ' + str(i.firstname) + ". Due Amount: " + str(
                    i.dueamount)
                message = client.messages.create(
                    body=msg,
                    from_="+12014256211",
                    to="+919866482608"
                )

                print(message.sid)


if __name__ == '__main__':
    import sys
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
    os.environ["DJANGO_SETTINGS_MODULE"] = "DadFinanceCorp.settings"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DadFinanceCorp.settings")
    django.setup()
    from FinanceCorp.models import Lender, Payee
    object_ = Lender.objects.all()
    object1_ = Payee.objects.all()
    send_lender_message(object_)
    send_payee_message(object1_)
# sendsms_object.send_payee_message()
