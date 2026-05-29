RED    = '\033[91m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
CYAN   = '\033[96m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
RESET  = '\033[0m'

def printRed(text):    print(f"{RED}{text}{RESET}")
def printGreen(text):  print(f"{GREEN}{text}{RESET}")
def printYellow(text): print(f"{YELLOW}{text}{RESET}")
def printCyan(text):   print(f"{CYAN}{text}{RESET}")
def printBold(text):   print(f"{BOLD}{text}{RESET}")
def printDim(text):    print(f"{DIM}{text}{RESET}")
