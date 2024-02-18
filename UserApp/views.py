from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


def user_profile(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    return render(request, 'UserApp/user_profile.html', {'user_profile': user_profile})


@login_required(login_url='AuthenticationApp:login')
def create_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
<<<<<<< HEAD
        # Si aucun UserProfile n'existe, en créer un pour l'utilisateur actuel
=======
>>>>>>> 275d7765e9dd1b476bacfce6d6bfc918eb07bad2
        user_profile = UserProfile(user=request.user)
        user_profile.save()
        
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('UserApp:user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UserApp/create_profile.html', {'form': form})


@login_required(login_url='AuthenticationApp:login')
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
<<<<<<< HEAD
        # Si aucun UserProfile n'existe, en créer un pour l'utilisateur actuel
=======
>>>>>>> 275d7765e9dd1b476bacfce6d6bfc918eb07bad2
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('UserApp:user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UserApp/edit_profile.html', {'form': form})

