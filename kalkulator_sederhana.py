def kalkulator(input) :
    input = input.split(' ')

    number1 = int(input[0])
    operator = input[1]
    number2 = int(input[2])

    if operator == "+" :
        calc = number1 + number2
    elif operator == "-" :
        calc = number1 - number2
    elif operator == "*" :
        calc = number1*number2
    else :
        calc = number1/number2
    
    return calc

# input user
print('* Ketik "quit" jika sudah selesai menggunakan kalkulator *\n')
inp = input("Masukkan angka untuk dihitung :\n>> ")

while inp != 'quit' and inp != 'Quit' :
    hasil = kalkulator(inp)
    print(hasil)
    add_data = input('>> ')
