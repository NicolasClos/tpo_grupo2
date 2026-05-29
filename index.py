from initial_definitions import getInitialValues
from validations import isValidAmount
from colors import printGreen, printCyan, printRed, printDim, printBold
from display import showHeader, showBillsSummary, showTransactions
from utils import sortTransactions

# ── INICIO ──────────────────────────────────────────────────────────────────
showHeader()
print("")

printCyan("Cargando billetes disponibles en el cajero...")
thousand_bill, fivehundred_bill, twohundred_bill, onehundred_bill = getInitialValues()

total_value = thousand_bill * 1000 + fivehundred_bill * 500 + twohundred_bill * 200 + onehundred_bill * 100
printGreen(f"  ✔ Total cargado: ${total_value}")
print("")

# transactions guarda tuplas: (monto, b1000, b500, b200, b100)
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
            printRed("  ✘ No es posible entregar ese monto con los billetes disponibles.")
        else:
            thousand_bill    -= b1000
            fivehundred_bill -= b500
            twohundred_bill  -= b200
            onehundred_bill  -= b100
            total_value      -= needed_amount

            showBillsSummary(b1000, b500, b200, b100)
            printDim(f"     Saldo restante en cajero: ${total_value}")

            transactions.append((needed_amount, b1000, b500, b200, b100))

    print("")
    needed_amount = int(input("Ingrese el monto a retirar (-1 para salir): "))

if len(transactions) > 0:
    sortTransactions(transactions)
    showTransactions(transactions)

print("")
printBold("¡Hasta luego!")
