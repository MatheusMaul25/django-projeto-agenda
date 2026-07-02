from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            # contact.show = False
            contact.save()
            return redirect('contact:update', contact_id = contact.pk)
        else:
            context = {
                'form': form,
                'form_action': form_action,
            }         
       
    else:
        context = {
            'form': ContactForm(),
            'form_action': form_action,
        }

    return render (
        request,
        'contact/create.html',
        context
    )

def update(request, contact_id):
    form_action = reverse('contact:update', args=(contact_id,))
    contact = get_object_or_404(Contact, pk = contact_id)

    if request.method == 'POST':
        
        form = ContactForm(request.POST, instance = contact)
        print(request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            # contact.show = False
            contact.save()
            return redirect('contact:update', contact_id = contact.pk)
        else:
            context = {
                'form': form,
                'form_action': form_action,
            }         
       
    else:
        context = {
            'form': ContactForm(instance = contact),
            'form_action': form_action,
        }

    return render (
        request,
        'contact/create.html',
        context
    )
        
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show = True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(request, 
                  'contact/contact.html', 
                  {
                    'contact': contact,
                    'confirmation': confirmation,
                      }
                )

        