def print_1_to_n(n,depth=0):
    indent = " " * depth
    print(f"{indent} Called with n = {n}")
    
    if(n == 0):
        print(f"{indent} base case reached. Returning...")
        return
    print_1_to_n(n-1,depth+1)
    print(f"{indent} printing: {n}")