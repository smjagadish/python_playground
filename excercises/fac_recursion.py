def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
   num = int(input('enter the num'))
   print(f'result is :{fact(num)}')