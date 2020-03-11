from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegistrationForm, UserUpdateForm, UserUpdateProfile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_f = UserUpdateForm(request.POST, instance=request.user)
        update_p = UserUpdateProfile(request.POST,
                                     request.FILES,
                                     instance=request.user.profile)
        if update_f.is_valid() and update_p.is_valid():
            update_f.save()
            update_p.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        update_f = UserUpdateForm(instance=request.user)
        update_p = UserUpdateProfile(instance=request.user.profile)

    context = {
        'update_f': update_f,
        'update_p': update_p
    }
    return render(request, 'users/profile.html',context)
