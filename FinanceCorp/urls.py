from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.header, name='header'),
    url(r'home/$', views.homepage, name='home'),
    url(r'adddetails/$', views.adddetails, name='adddetails'),
    url(r'view/$', views.viewpayments, name='viewpayments'),
    url(r'addpayee/$', views.addpayee, name='addpayee'),
    url(r'addlender/$', views.addlender, name='addlender'),
    url(r'lenderdetails/$', views.savelender, name='savelender'),
    url(r'payeedetails/$', views.savepayee, name='savepayee'),
    url(r'update(|[\d]+-[\w]+)/$', views.update, name='update'),
    url(r'lender/$', views.lenderdetails, name='lenderdetails'),
    url(r'payee/$', views.payeedetails, name='payeedetails'),
    url(r'sortby(firstname|amount|duedate)/$', views.sort, name='sortdropbox'),
    url(r'id([\d]+)/$', views.fullstatement, name='fullstatement'),
    url(r'addpayment(lender|payee)([\d]+)/$', views.addpayment, name='addpayment'),
    url(r'demo/', views.demoform, name='demoform'),
    url(r'search/$', views.search, name='search'),
    url(r'newupdate([\d]+)/$', views.detailsupdate, name='update'),
    url(r'([\d]+)([\w]+)delete/$', views.delete, name='delete'),
    url(r'updatesave(payee|lender)-/$', views.update_save, name='updatesave'),
    url(r'savepayment/$', views.savepayment, name='savepayment'),
    url(r'(firstname|amount|duedate)paye/$', views.payeesort, name='sortpayee'),
    url(r'([\d]+)payeeid', views.payeepayment, name='payeepayment')
]
