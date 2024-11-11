


'''def asterik_triangle_soln(n):
    return n**2

ans= asterik_triangle_soln(6)
print(ans)

fruits = ['banana', 'apple', 'orange']
len_var = len(fruits)
print(len_var)

detail={'name':'Gbenga',
 'address': '8, prague, czech republic',
 'age': 20
 }
det_dict = detail['address']
print(det_dict)'''


'''def convert_temp(celcius):
    kelvin = 273 + celcius
    return kelvin

kelvin_temp = convert_temp(25)
print(kelvin_temp)


number = [1,2,3,4,5,6,7,8,9,10]
for n in number:
    print(n)

add_plus = 4 + 5
print(add_plus)

def factor_ial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
calc = factor_ial(5)
print(calc)


va_num = [2, 5, 8, 9]
def squared_num(n):
    return n**2

m_val = list(map(squared_num, va_num))
print(m_val)'''

FILEPATH = 'todos1.txt'

def get_todos(filepath = FILEPATH):
    """ Read a text file and return to_do
    items list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos( todos_org,filepath = FILEPATH):
    """ Write to_do items list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_org)


if __name__ == "__main__":
    print('Good')
    print('Hi')




