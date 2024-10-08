from django import forms
from home.models import Reservation
import datetime

class ReservationForm(forms.ModelForm):

    name = forms.CharField(max_length=50, label='Name',widget=forms.TextInput(attrs={'placeholder': 'Your Name',
                                                                                     'class':'form-control',
                                                                                     'data-rule':'minlen:4',
                                                                                     'data-msg':'Please enter at least 4 chars',
                                                                                     'id':'name'}))
    phone = forms.CharField(max_length=20, label='Phone',widget=forms.TextInput(attrs={'placeholder': 'Your Phone',
                                                                                       'class':'form-control',
                                                                                       'data-rule':'minlen:4',
                                                                                       'data-msg':'Please enter at least 4 chars',
                                                                                       'id':'phone'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                          'class':'form-control',
                                                                          'data-rule':'email',
                                                                          'data-msg':'Please enter a valid email',
                                                                          'id':'email'}))
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'placeholder': 'Date',
                                                                       'class':'form-control',
                                                                       'data-rule':'minlen:4',
                                                                       'data-msg':'Please enter at least 4 chars',
                                                                       'id':'date'}))
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'placeholder': 'Time',
                                                                       'class':'form-control',
                                                                       'data-rule':'minlen:4',
                                                                       'data-msg':'Please enter at least 4 chars',
                                                                       'id':'time'}))
    people = forms.IntegerField(label='People', widget=forms.NumberInput(attrs={'placeholder': '# of people',
                                                                                'class':'form-control',
                                                                                'data-rule':'minlen:1',
                                                                                'data-msg':'Please enter at least 1 chars',
                                                                                'id':'people'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                                            'class':'form-control',
                                                                            'data-rule':'minlen:1',
                                                                            'data-msg':'Please enter at least 1 chars',}))

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError('Invalid date - reservation in the past')
        return date

    class Meta:
        model = Reservation
        fields = ('name', 'phone','email', 'date', 'time', 'people', 'message')