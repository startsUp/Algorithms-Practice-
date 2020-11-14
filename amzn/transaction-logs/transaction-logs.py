from collections import Counter, deque

def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """
    transactions = Counter()
    for log in logs:
        sender, reciever, amt = log.split(' ')
        transactions[sender] += 1
        if sender != reciever:
            transactions[reciever] += 1
    
    print(transactions)
    ans = deque()
    for t in transactions:
        if transactions[t] >= threshold:
            ans.appendleft(t)
    return list(ans)