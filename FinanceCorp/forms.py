from django import forms


class AddLenderPayment(forms.Form):
    pass


class DemoForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=100)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 100:
            raise forms.ValidationError('Not Valid Input')


class UpdateForm(forms.Form):
    amount = forms.IntegerField()
    interest = forms.IntegerField()
    duedate = forms.DateField()
    interestamount = forms.IntegerField()
