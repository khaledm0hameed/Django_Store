from django.shortcuts import render

# Create your views here.

from contactus.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
