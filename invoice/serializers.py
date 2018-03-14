from rest_framework import serializers


class IntuitInvoiceDetailSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=45)
    deposit = serializers.CharField(max_length=45)
    balance = serializers.CharField(max_length=45)
    docNumber = serializers.CharField(max_length=45)
    privateNote = serializers.CharField(max_length=45)
    dueDate = serializers.CharField(max_length=45)
    shipDate = serializers.CharField(max_length=45)
    trackingNum = serializers.CharField(max_length=45)
    totalAmt = serializers.CharField(max_length=45)
    printStatus = serializers.CharField(max_length=45)
    emailStatus = serializers.CharField(max_length=45)
    exchangeRate = serializers.CharField(max_length=45)
    globalTaxCalculation = serializers.CharField(max_length=45)
    eInvoiceStatus = serializers.CharField(max_length=45)
    billAddress = serializers.CharField(max_length=45)
    shipAddress = serializers.CharField(max_length=45)
    billEmail = serializers.CharField(max_length=45)
    customerRef = serializers.CharField(max_length=45)
    currencyRef = serializers.CharField(max_length=45)
    customerMemo = serializers.CharField(max_length=45)
    departmentRef = serializers.CharField(max_length=45)
    txnTaxDetail = serializers.CharField(max_length=45)
    deliveryInfo = serializers.CharField(max_length=45)


class IntuitInvoiceListSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=45)
    description = serializers.CharField(max_length=45)
