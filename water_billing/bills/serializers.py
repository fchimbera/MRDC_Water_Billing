from rest_framework import serializers
from .models import MeterReading, Bill, WaterRate
from django.contrib.auth import get_user_model

User = get_user_model()

class WaterRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterRate
        fields = '__all__'

class MeterReadingSerializer(serializers.ModelSerializer):
    account = serializers.CharField(write_only=True, source='account_id') # Expect account_id in input
    account_detail = serializers.PrimaryKeyRelatedField(read_only=True, source='account') # For output

    class Meta:
        model = MeterReading
        fields = ['id', 'account', 'account_detail', 'reading_date', 'reading_value', 'created_at', 'is_billed', 'is_active']
        read_only_fields = ['id', 'created_at', 'is_billed', 'account_detail']

    def create(self, validated_data):
        account_id = validated_data.pop('account_id')
        try:
            user = User.objects.get(account_id=account_id)
        except User.DoesNotExist:
            raise serializers.ValidationError(f"User with account_id '{account_id}' does not exist.")
        meter_reading = MeterReading.objects.create(account=user, **validated_data)
        return meter_reading

class BillSerializer(serializers.ModelSerializer):
    water_rate = WaterRateSerializer(read_only=True)
    meter_reading = MeterReadingSerializer(read_only=True)

    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ['user', 'previous_reading_value', 'consumption', 'rate_used', 'amount_due', 'billing_period_start', 'billing_period_end']