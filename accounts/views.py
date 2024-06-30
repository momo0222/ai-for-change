from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from .models import StudentProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentProfileForm
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    def form_valid(self, form):
        print("Form is valid")  # Print statement to check if form is valid
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")  # Print statement to check if form is invalid
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        print("Success URL")  # Print statement to check success URL
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        print("Context data")  # Print statement to check context data
        return super().get_context_data(**kwargs)

@login_required
def profile_edit(request):
    # Fetch the current user's StudentProfile instance
    student_profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or any other success URL
    else:
        form = StudentProfileForm(instance=student_profile)

    return render(request, 'accounts/profile_form.html', {'form': form})