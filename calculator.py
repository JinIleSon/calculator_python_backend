i1 = input('값을 입력하세요.')
operator = input('연산자를 입력하세요.')
i2 = input('값을 입력하세요.')

if not (i1.isnumeric() & i2.isnumeric()):
    print('잘못된 수입니다.')
    exit()

i1 = int(i1)
i2 = int(i2)

if operator == '+':
    print('{} {} {} = {}'.format(i1, operator, i2, i1 + i2))
elif operator == '-':
    print('{} {} {} = {}'.format(i1, operator, i2, i1 - i2))
elif operator == '*':
    print('{} {} {} = {}'.format(i1, operator, i2, i1 * i2))
elif operator == '/':
    print('{} {} {} = {}'.format(i1, operator, i2, i1 / i2))
elif operator == '%':
    print('{} {} {} = {}'.format(i1, operator, i2, i1 % i2))
else:
    print('연산자를 잘못 입력하였습니다.')