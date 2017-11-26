from django.shortcuts import render
from .forms import DataForm
from datetime import datetime, timedelta, date, time
import usertime, timbra
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        form = DataForm()
        return render(request, 'clockout/home.html', {'form': form})
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            in_morning = datetime.combine(date.today(),form.cleaned_data['in_morning'])
            out_lunch = datetime.combine(date.today(),form.cleaned_data['out_lunch'])
            in_lunch = datetime.combine(date.today(),form.cleaned_data['in_lunch'])
            min_lunch_length = timedelta(minutes=form.cleaned_data['min_lunch_length'])
            total_hours = timedelta(hours=int(form.cleaned_data['total_hours']))

            try:
                ut = usertime.UserTime(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)
            except ValueError:
                return HttpResponse('not valid',status=400)
            ur = timbra.calculate(ut)
            output = {
                'morning_work': ur.morning_work,
                'lunch_break':ur.lunch_break,
                'afternoon_work': ur.afternoon_work,
                'out_evening': ur.out_evening
            }
            return render (request, 'clockout/result.html', output)
        else:
            return HttpResponse('not valid',status=400)