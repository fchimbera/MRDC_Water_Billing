from django.conf import settings
from django.db import models

class WaterRate(models.Model):
    rate_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField(auto_now=False, default=None)  # Date when this rate became effective
    description = models.CharField(max_length=255, blank=True, null=True)  # Optional description of the rate
    is_active = models.BooleanField(default=True)  # Indicates if this rate is currently active
    
    def __str__(self):
        return f"Rate: {self.rate_per_unit} (Effective from {self.effective_date})"

class MeterReading(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meter_readings',
        db_column='account_id',  # Explicitly set the database column name
        to_field='account_id'   # Link to the 'account_id' field in Users
    )
    reading_date = models.DateField()
    reading_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.paid_date and not self.is_paid:
            raise ValueError("paid_date can only be set if is_paid is True.")
        super().save(*args, **kwargs)
    is_billed = models.BooleanField(default=False)  # Indicates if this reading has been billed
    is_active = models.BooleanField(default=True)  # Indicates if the reading is active or not
    
    def __str__(self):
        account_id = getattr(self.account, 'account_id', 'Unknown Account')
        return f"Reading on {self.reading_date} for {account_id}: {self.reading_value}"

class Bill(models.Model):
    # The `on_delete=models.PROTECT` ensures that a WaterRate entry cannot be deleted if it is referenced by a bill.
    rate_used = models.ForeignKey(WaterRate, on_delete=models.PROTECT)  # Link to the rate used for this bill
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bills')
    meter_reading = models.ForeignKey(MeterReading, on_delete=models.CASCADE)
    previous_reading_value = models.DecimalField(max_digits=10, decimal_places=2)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    rate_used = models.ForeignKey(WaterRate, on_delete=models.PROTECT)  # Link to the rate used for this bill
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    billing_period_start = models.DateField()
    billing_period_end = models.DateField()
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill for {self.user.username} ({self.billing_period_end})"