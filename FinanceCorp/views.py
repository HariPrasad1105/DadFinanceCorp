import datetime
from itertools import chain
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .forms import DemoForm
from .models import Lender, Payee, LenderPaymentDetails, PayeePaymentDetails


def header(request):
    return render(request, 'header.html')


def homepage(request):
    reference = Lender.objects.all()
    return render(request, 'home.html', {'reference': reference})


def adddetails(request):
    return render(request, 'adddetails.html')


def viewpayments(request):
    return render(request, 'viewpayments.html')


def addpayee(request):
    return render(request, 'addpayee.html')


def addlender(request):
    return render(request, 'addlender.html')


def savelender(request):
    firstname, surname, amount, interest, duedate = str(request.POST['firstname']), str(request.POST['surname']), request.POST['amount'], request.POST['interest'], request.POST['duedate']
    interestamount, dueamount = (int(amount)/100)*int(interest), 0
    reminddate = int(str(duedate)[8:10])
    a = Lender(firstname=firstname, surname=surname, amount=amount, interest=interest, duedate=duedate, reminddate=reminddate, interestamount=interestamount, dueamount=dueamount, type='lender')
    a.save()
    return render(request, 'addlender.html', {'message': 'Successfully saved'})


def savepayee(request):
    firstname, surname, amount, interest, duedate, period = str(request.POST['firstname']), str(request.POST['surname']), request.POST['amount'], request.POST['interest'], request.POST['duedate'], request.POST['period']
    interestamount, dueamount = ((int(amount)/100)*int(interest)*int(period)), 0
    remindate = int(str(duedate)[8:10])
    a = Payee(firstname=firstname, surname=surname, amount=amount, interest=interest, period=period, duedate=duedate, reminddate=remindate, interestamount=interestamount, dueamount=dueamount, type='payee')
    a.save()
    return render(request, 'addpayee.html', {'message': 'Successfully saved'})


def update(request, tag):
    if not tag:
        return render(request, 'update.html')
    else:
        id, type_ = tag.split('-')
        if type_ == 'lender':
            a = Lender.objects.filter(pk=id)
            return render(request, 'searchresult.html', {'object': a, 'msg': 'returned'})
        else:
            a = Payee.objects.filter(pk=id)
            return render(request, 'searchresult.html', {'object': a, 'msg': 'returned'})


def payeedetails(request):
    payee = Payee.objects.all()
    return render(request, 'payeedetails.html', {"object": payee})


def lenderdetails(request):
    lender = Lender.objects.all()
    return render(request, 'lenderdetails.html', {'object': lender})


def sort(request, sortby):
    if sortby == 'firstname':
        a = Lender.objects.order_by('firstname')
    elif sortby == 'amount':
        a = Lender.objects.order_by('-amount')
    else:
        a = Lender.objects.order_by('-duedate')
    return render(request, 'lenderdetails.html', {'object': a})


def fullstatement(request, id):
    a = LenderPaymentDetails.objects.filter(lenderID=id).order_by('paymentDate')
    return render(request, 'fullstatement.html', {'object': a})


def addpayment(request, type_, id):
    if type_ == 'lender':
        object_ = Lender.objects.filter(pk=int(id))
    else:
        object_ = Payee.objects.filter(pk=int(id))
    return render(request, 'addPayment.html', {'object': object_})


def demoform(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return render(request, 'demo.html', {'form': form, 'age': age, 'name': name})
    else:
        form = DemoForm()
        return render(request, 'demo.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    if query:
        result2 = Lender.objects.filter(Q(firstname__icontains=query) | Q(surname__icontains=query))
        result1 = Payee.objects.filter(Q(firstname__icontains=query) | Q(surname__icontains=query))
        result = list(chain(result1, result2))
    pages = Paginator(result, 10)
    if result:
        message = 'not empty'
    else:
        message = 'empty'
    context = {
       'items': pages.page(1).object_list,
        'newmsg': message,
    }
    return render(request, 'searchresult.html', context)


def detailsupdate(request, pk):
    object_ = Lender.objects.filter(id=pk)
    return render(request, 'detailsupdate.html', {'object': object_})


def delete(request, id, type_):
    print(type_, id)
    if type_ == 'lender':
        a = Lender.objects.filter(pk=id)
        a.delete()
    else:
        a = Payee.objects.filter(pk=id)
        a.delete()
    return render(request, 'home.html')


def update_save(request, type):
    id = request.POST['id']
    if type == 'lender':
        a = Lender.objects.filter(pk=id)
        for object_ in a:
            object_.amount = request.POST['amount']
            object_.interest = request.POST['interest']
            object_.interestamount = (int(request.POST['amount'])/100)*int(request.POST['interest'])
    else:
        a = Payee.objects.filter(pk=id)
        for object_ in a:
            object_.amount = request.POST['amount']
            object_.interest = request.POST['interest']
            object_.interestamount = (int(request.POST['amount'])/100)*int(request.POST['interest'])
    object_.save()
    return render(request, 'home.html')


def savepayment(request):
    radiobuttonvalue = request.POST['radiobuttonamount']
    if request.POST['type'] == 'lender':
        lender_instance = Lender.objects.get(id=int(request.POST["id"]))
        if radiobuttonvalue == 'interest':
            lender_instance.dueamount -= int(request.POST['amount'])
        else:
            lender_instance.amount -= int(request.POST['amount'])
        a = LenderPaymentDetails.objects.create(lenderID=lender_instance, paymentDate=request.POST['paymentdate'], amount=int(request.POST['amount']))
        lender_instance.save()
        a.save()
    else:
        payee_object = Payee.objects.get(id=int(request.POST['id']))
        a = PayeePaymentDetails.objects.create(payeeID=payee_object, paymentDate=request.POST['paymentdate'], amount=int(request.POST['amount']))
        a.save()
    return render(request, 'home.html')


def payeesort(request, sortby):
    if sortby == 'firstname':
        object_ = Payee.objects.order_by('firstname')
    elif sortby == 'amount':
        object_ = Payee.objects.order_by('-amount')
    else:
        object_ = Payee.objects.order_by('duedate')
    return render(request, 'payeedetails.html', {'object': object_})


def payeepayment(request, id):
    object_ = PayeePaymentDetails.objects.filter(payeeID=id)
    return render(request, 'fullstatement.html', {'object': object_})