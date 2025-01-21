from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Custom test function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_dashboard.html')
