from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'admin_template.html')
