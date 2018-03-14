from django.db import models
import requests
import json
import us

# Create your models here.


class QBInvoice(object):
    def __init__(self):
        self.Deposit = 0
        self.Balance = 0
        self.AllowIPNPayment = True
        self.DocNumber = ""
        self.PrivateNote = ""
        self.DueDate = ""
        self.ShipDate = ""
        self.TrackingNum = ""
        self.TotalAmt = ""
        self.ApplyTaxAfterDiscount = False
        self.PrintStatus = "NotSet"
        self.EmailStatus = "NotSet"
        self.ExchangeRate = 1
        self.GlobalTaxCalculation = "TaxExcluded"

        self.EInvoiceStatus = None

        self.BillAddr = None
        self.ShipAddr = None
        self.BillEmail = None
        self.CustomerRef = None
        self.CurrencyRef = None
        self.CustomerMemo = None
        self.DepartmentRef = None
        self.TxnTaxDetail = None
        self.DeliveryInfo = None

        self.CustomField = []
        self.Line = []
        self.LinkedTxn = []

    def __str__(self):
        return str(self.TotalAmt)

    @property
    def data(self):
        return self.__dict__
