def fibonacci(n, seq=None):
    if seq is None:
        seq = []
    if n <= 0:
        return seq
    if len(seq) < 2:
        seq.append(len(seq))
    else:
        seq.append(seq[-1] + seq[-2])
    return fibonacci(n - 1, seq)
n = 18
print(fibonacci(n))