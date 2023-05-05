import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from base.models import Payment

def parse_csv_file(file):
    payments = []
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        payer, payee, amount = row
        payment = Payment(payer=payer, payee=payee, amount=amount)
        payments.append(payment)
    return payments