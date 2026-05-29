def isAmountAvailable(needed_amount, total_value):
    if needed_amount > total_value:
        print("  ✘ No contamos con ese dinero en el cajero.")
        return False
    return True

def isAmountMultipleOf100(needed_amount):
    if needed_amount % 100 != 0:
        print("  ✘ El monto ingresado no es correcto (debe ser múltiplo de $100).")
        return False
    return True

def isValidAmount(needed_amount, total_value):
    return isAmountAvailable(needed_amount, total_value) and isAmountMultipleOf100(needed_amount)
