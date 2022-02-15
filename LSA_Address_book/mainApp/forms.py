from django import forms

class CreateNewList(forms.Form):
    firstName = forms.CharField( max_length=200 , required=False)
    lastName = forms.CharField( max_length=200, required=False)
    homephoneNumber = forms.CharField( max_length=200, required=False)
    workphoneNumber = forms.CharField( max_length=200, required=False)
    mobilephoneNumber = forms.CharField( max_length=200, required=False)
    email = forms.EmailField( max_length=256, required=False)
    address = forms.CharField( max_length=100, required=False)


class CreateNewContact(forms.Form):
    name = forms.CharField( max_length=200, required=False)

class SearchResult(forms.Form):
    searchresult = forms.CharField(max_length=200, required=False)