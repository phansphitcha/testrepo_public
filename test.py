# print("Hello")
# print(123)
# print(True)

# a = input('กรุณาใส่ตัวเลข "1-10"')
# b = input('กรุณาใส่ตัวเลข "1-10"')
# print(a+b)
# print(type(a))

#print(int(a)+int(b))
#print(float(a)+float(b))


def inputNumber():
    try:
        return float(input('กรุณาใส่ตัวเลข '))
    except:
        print('Error Kaa')

a = inputNumber()
b = inputNumber()
c = float("{:.2f}".format(a+b))
print(c)
print(round(a+b,2))
print('Done')


