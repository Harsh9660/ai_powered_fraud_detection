from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    transaction_id = models.CharField(max_length=100)
    transaction_amount = models.FloatField()
    transaction_currency = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=10)
    transaction_timestamp = models.DateTimeField(auto_now_add=True)
    transaction_is_fraud = models.BooleanField(default=False)
    
class frauddetection(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    model_accuracy = models.FloatField()
    model_precision = models.FloatField()
    model_recall = models.FloatField()
    model_f1_score = models.FloatField()
    model_timestamp = models.DateTimeField(auto_now_add=True)
    model_is_fraud = models.BooleanField(default=False)
    model_prediction = models.BooleanField(default=False)