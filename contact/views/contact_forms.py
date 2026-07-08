from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'SUCCESS! Created contact')
            return redirect('contact:index')
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

@login_required(login_url='contact:login')
def update(request, contact_id):
    form_action = reverse('contact:update', args=(contact_id,))
    contact = get_object_or_404(Contact, pk = contact_id, owner= request.user)

    if request.method == 'POST':
        
        form = ContactForm(request.POST, request.FILES, instance = contact,)
        if form.is_valid():
            contact = form.save(commit=False)
            # contact.show = False
            print(request.method)
            contact.save()
            messages.success(request, 'Updated contact')
            return redirect('contact:index')
        else:
            print(form.errors)

            context = {
                'form': form,
                'form_action': form_action,
            }         
       
    else:
        context = {
            'form': ContactForm(instance = contact),
            'form_action': form_action,
        }
        print(request.method)


    return render (
        request,
        'contact/update_contact.html',
        context
    )
        
@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show = True, 
                                owner= request.user)
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

        