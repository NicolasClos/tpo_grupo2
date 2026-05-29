from initial_definitions import getInitialValues
from validations import isValidAmount
from display import showBillsSummary, showTransactions

def sortTransactions(transactions):
    n = len(transactions)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if transactions[j][0] < transactions[j + 1][0]:
                temp = transactions[j]
                transactions[j] = transactions[j + 1]
                transactions[j + 1] = temp


print("--- CAJERO AUTOMÁTICO ---")
print("")

print("Cargando billetes disponibles en el cajero...")
bills = getInitialValues()
thousand_bill    = bills[0]
fivehundred_bill = bills[1]
twohundred_bill  = bills[2]
onehundred_bill  = bills[3]

total_value = thousand_bill * 1000 + fivehundred_bill * 500 + twohundred_bill * 200 + onehundred_bill * 100
print("  Total cargado: $" + str(total_value))
print("")

transactions = []

needed_amount = int(input("Ingrese el monto a retirar (-1 para salir): "))

while needed_amount != -1:
    print("")
    if isValidAmount(needed_amount, total_value):
        remaining = needed_amount

        b1000 = min(remaining // 1000, thousand_bill)
        remaining -= b1000 * 1000

        b500 = min(remaining // 500, fivehundred_bill)
        remaining -= b500 * 500

        b200 = min(remaining // 200, twohundred_bill)
        remaining -= b200 * 200

        b100 = min(remaining // 100, onehundred_bill)
        remaining -= b100 * 100

        if remaining != 0:
            print("  No es posible entregar ese monto con los billetes disponibles.")
        else:
            thousand_bill    -= b1000
            fivehundred_bill -= b500
            twohundred_bill  -= b200
            onehundred_bill  -= b100
            total_value      -= needed_amount

            showBillsSummary(b1000, b500, b200, b100)
            print("     Saldo restante en cajero: $" + str(total_value))

            transactions.append([needed_amount, b1000, b500, b200, b100])

    print("")
    needed_amount = int(input("Ingrese el monto a retirar (-1 para salir): "))

if len(transactions) > 0:
    sortTransactions(transactions)
    showTransactions(transactions)

print("")
print("¡Hasta luego!")
