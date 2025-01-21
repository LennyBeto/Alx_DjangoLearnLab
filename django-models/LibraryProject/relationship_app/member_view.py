 from django.contrib.auth.decorators import user_passes_test
   from django.shortcuts import render

   @user_passes_test(lambda u: u.userprofile.role == 'Member')
   def member_view(request):
       return render(request, 'member_dashboard.html')
