from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado.')
            return redirect('contact:login')
            

    context = {
        'form': form
    }
    return render(request, 'contact/register.html', context)

def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Entrou!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido!')

    context = {
        'form': form,
    }

    return render(
        request, 
        'contact/login.html',
        context)

def logout_view(request):
    auth.logout(request)
    messages.warning(request, 'Saiu!')
    return redirect('contact:login')

@login_required
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data= request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
    context = {
        'form': form,
    }
    return render(
        request, 
        'contact/user_update.html', 
        context,
        )