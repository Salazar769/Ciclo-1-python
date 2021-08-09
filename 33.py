def fibonnacci(n):
    if n ==0:
        return 0 
elif n == 1:
    return fibonnacci(n-2) + fibonnacci(n - 1)
print(fibonnacci(45))