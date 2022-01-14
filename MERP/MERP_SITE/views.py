from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Event, Registration
from .forms import RegisterForm
import string
import random


class LandingPageView(View):
    def get(self, request):
        events = Event.objects.all()
        ctx = {
            "events": events
        }
        return render(request, "index.html", ctx)


class EventsDetailView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        ctx = {
            "event": event
        }
        return render(request, "event.html", ctx)


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            set_of_chars = string.ascii_letters + string.digits
            code = ''.join(random.choice(set_of_chars) for i in range(15))

            registration = Registration.objects.create(
                event=form.cleaned_data["event"],
                name=form.cleaned_data["name"],
                surname=form.cleaned_data["surname"],
                e_mail=form.cleaned_data["e_mail"],
                #**form.cleaned_data,
                reservation_code=code
            )
            return redirect("thanks", registration_id=registration.id)
        #return render(request, "register.html", {"form": form})


class ConfirmationView(View):
    def get(self, request, registration_id):
        regis = get_object_or_404(Registration, id=registration_id)
        ctx = {
            "regis": regis
        }
        return render(request, "confirmation.html", ctx)

