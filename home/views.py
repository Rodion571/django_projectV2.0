from django.shortcuts import render, redirect
from django.views.generic.dates import timezone_today

from home.models import Category, Gallery, Chef, Event, Contact
from home.forms import ReservationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')

    categories = Category.objects.filter(is_visible=True).order_by('sort')
    gallery = Gallery.objects.filter(is_visible=True)
    chefs = Chef.objects.all()
    events = Event.objects.filter(date_and_time__gte=timezone_today(), is_visible=True)
    contacts = Contact.objects.all()
    book_a_table_form = ReservationForm()

    context = {
        'categories': categories,
        'gallery': gallery,
        'chefs': chefs,
        'events': events,
        'contacts': contacts,
        'book_a_table_form': book_a_table_form,
    }

    return render(request, 'index.html', context)

def thanks(request):
    return render(request, 'thanks.html')