from datetime import time
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError

from .models import Service, Reservation


class BaseReservationForm(forms.Form):
    timestamp = forms.DateTimeField()
    service = forms.ModelChoiceField(Service.objects.all())
    employee = forms.ModelChoiceField(User.objects.all())

    def clean_timestamp(self):
        timestamp = self.cleaned_data["timestamp"]
        if (
            timestamp.minute not in (0, 30)
            or timestamp.second != 0
            or timestamp.microsecond != 0
        ):
            raise ValidationError(f"Provided time slot { timestamp } is invalid")
        return timestamp

    def clean(self):
        service = self.cleaned_data.get("service")
        employee = self.cleaned_data.get("employee")
        timestamp = self.cleaned_data.get("timestamp")

        errors = {}

        if service and employee and employee not in service.staff.all():
            errors["employee"] = ValidationError(
                f"Sorry, {employee} does not perform this service {service}, choose other employee. "
            )

        # musimy spsrawdizć czy w czasie  [timestamp; timestamp +service.duration] nie występuje jakaś rezerwacja

        if timestamp and service and employee:
            if Reservation.objects.filter(
                timestamp__gte=timestamp,
                timestamp__lt=timestamp + service.duration
                # employee=employee
            ):
                errors["timestamp"] = ValidationError(
                    f"In this period other reservation already exist. Please, choose different date."
                )

        if timestamp and service:
            reservation_time = timestamp.time()
            reservation_time_end = (timestamp + service.duration).time()
            if reservation_time < time(10, 00) or reservation_time_end > time(19, 0):
                errors["timestamp"] = ValidationError(
                    "Chosen time exceed our working hours."
                )

        if errors:
            raise ValidationError(errors)


class ReservationForm(forms.ModelForm):
    privacy_policy = forms.BooleanField(
        required=True,
        label="I accept privacy policy",
        help_text="<a href= '/pages/privacy-policy'>link </a> ",
    )
    terms_of_services = forms.BooleanField(
        required=True,
        label="I accept terms & conditions.",
        help_text="<a href= '/pages/terms_of_services'>link</a> ",
    )

    class Meta:
        model = Reservation
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "privacy_policy",
            "terms_of_services",
        ]
