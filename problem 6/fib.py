def fibonacci(n):
    sequence=[0,1]
    while len(sequence) < n+1:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')