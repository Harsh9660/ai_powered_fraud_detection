from django.contrib import admin
from .models import Transaction, frauddetection, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)
    ordering = ('username',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'transaction_amount', 'transaction_currency', 'transaction_type', 'transaction_timestamp', 'transaction_is_fraud')
    list_filter = ('transaction_currency', 'transaction_type', 'transaction_is_fraud', 'transaction_timestamp')
    search_fields = ('transaction_id', 'user__username')
    ordering = ('-transaction_timestamp',)

@admin.register(frauddetection)
class FrauddetectionAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'model_name', 'model_accuracy', 'model_precision', 'model_recall', 'model_f1_score', 'model_timestamp', 'model_is_fraud', 'model_prediction')
    list_filter = ('model_name', 'model_is_fraud', 'model_prediction', 'model_timestamp')
    search_fields = ('transaction__transaction_id', 'model_name')
    ordering = ('-model_timestamp',)