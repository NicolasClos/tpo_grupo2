def showBillsSummary(b1000, b500, b200, b100):
    print("  Extraccion exitosa:")
    if b1000 > 0: print("     Billetes de $1000: " + str(b1000))
    if b500  > 0: print("     Billetes de $500:  " + str(b500))
    if b200  > 0: print("     Billetes de $200:  " + str(b200))
    if b100  > 0: print("     Billetes de $100:  " + str(b100))

def showTransactions(transactions):
    print("\nResumen de extracciones")
    for i in range(len(transactions)):
        t = transactions[i]
        print("  " + str(i + 1) + ". Monto: $" + str(t[0]))
        print("     $1000x" + str(t[1]) + "  $500x" + str(t[2]) + "  $200x" + str(t[3]) + "  $100x" + str(t[4]))
