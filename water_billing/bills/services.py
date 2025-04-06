from datetime import date, timedelta
from django.utils import timezone
from .models import MeterReading, Bill, WaterRate
from django.db.models import Max
from decimal import Decimal

def calculate_and_create_bill(meter_reading):
    if meter_reading.is_billed:
        raise ValueError(f"Meter reading {meter_reading.id} is already billed.")

    account = meter_reading.account

    # Find the latest previous reading for the account
    previous_reading = MeterReading.objects.filter(
        account=account,
        reading_date__lt=meter_reading.reading_date,
        is_billed=True
    ).order_by('-reading_date').first()

    previous_reading_value = previous_reading.reading_value if previous_reading else Decimal('0.00')
    consumption = meter_reading.reading_value - previous_reading_value

    # Get the active water rate
    active_rate = WaterRate.objects.filter(effective_date__lte=meter_reading.reading_date, is_active=True).order_by('-effective_date').first()
    if not active_rate:
        raise ValueError("No active water rate found for this reading date.")

    amount_due = consumption * active_rate.rate_per_unit

    # Determine billing period (basic example)
    billing_period_start = previous_reading.reading_date if previous_reading else meter_reading.reading_date - timedelta(days=30)  # Approximate
    billing_period_end = meter_reading.reading_date
    due_date = billing_period_end + timedelta(days=15)

    # Create the bill
    bill = Bill.objects.create(
        user=account,  # Changed 'account' to 'user' to match the Bill model
        meter_reading=meter_reading,
        previous_reading_value=previous_reading_value,
        consumption=consumption,
        rate_used=active_rate,
        amount_due=amount_due,
        billing_period_start=billing_period_start,
        billing_period_end=billing_period_end,
        due_date=due_date
    )

    meter_reading.is_billed = True
    meter_reading.save()

    return bill