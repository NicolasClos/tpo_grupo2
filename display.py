from colors import printBold, printGreen, printCyan, printYellow, printDim

def showHeader():
    printBold("╔══════════════════════════════════════╗")
    printBold("║         CAJERO AUTOMÁTICO            ║")
    printBold("╚══════════════════════════════════════╝")

def showBillsSummary(b1000, b500, b200, b100):
    printGreen("  ✔ Extracción exitosa:")
    if b1000 > 0: printCyan(f"     • Billetes de $1000: {b1000}")
    if b500  > 0: printCyan(f"     • Billetes de $500:  {b500}")
    if b200  > 0: printCyan(f"     • Billetes de $200:  {b200}")
    if b100  > 0: printCyan(f"     • Billetes de $100:  {b100}")

def showTransactions(transactions):
    printBold("\n╔══════════════════════════════════════╗")
    printBold("║       RESUMEN DE EXTRACCIONES        ║")
    printBold("╚══════════════════════════════════════╝")
    for i in range(len(transactions)):
        t = transactions[i]
        printYellow(f"  {i + 1}. Monto: ${t[0]}")
        printDim(f"     $1000×{t[1]}  $500×{t[2]}  $200×{t[3]}  $100×{t[4]}")
