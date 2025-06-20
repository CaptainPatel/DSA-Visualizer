def factorial(n,depth=0):
    indent = "  " * depth
    print(f"{indent}Calling factorial({n})")

    if n == 0 or n == 1:
        print(f"{indent}Returning 1 (base case)")
        return 1

    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}Returning {result} from factorial({n})")
    return result