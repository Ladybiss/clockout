from django import forms


class DataForm(forms.Form):
    in_morning = forms.TimeField(label='Morning clock in',)
    out_lunch = forms.TimeField(label='Lunch break start',)
    in_lunch = forms.TimeField(label='Lunch break end',)
    total_hours = forms.ChoiceField(label='Required working hours', initial=8, widget=forms.Select, choices=[(str(x), str(x)) for x in range(1, 25)])
    min_lunch_length = forms.IntegerField(label='Mandatory lunch break duration', min_value=1, max_value=180, initial=30)