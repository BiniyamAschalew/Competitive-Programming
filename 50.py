def compute(a, b):
    c = a * b
    c = int(c/2)
    return c

if __name__ == '__main__':
    input = input().split()
    a = int(input[0])
    b = int(input[1])
    print(compute(a, b))