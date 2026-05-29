def sortTransactions(transactions):
    n = len(transactions)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if transactions[j][0] < transactions[j + 1][0]:
                temp = transactions[j]
                transactions[j] = transactions[j + 1]
                transactions[j + 1] = temp
