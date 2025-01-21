from django.contrib.auth.decorators import user_passes_test
   from django.shortcuts import render

   @user_passes_test(lambda u: u.userprofile.role == 'Librarian')
   def librarian_view(request):
       return render(request, 'librarian_dashboard.html')
