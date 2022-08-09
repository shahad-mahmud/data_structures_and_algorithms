def table(n, i):
    if i > 10: return 
    
    print(f"{n} * {i} = {n*i}")
    table(n, i+1)

if __name__ == "__main__":
    n = int(input('Enter n: '))
    print('-' * 15)
    
    table(n, 1)