import pandas as pd

def show(array) :
    table = pd.DataFrame(array)
    table.columns = ['nama', 'harga', 'rating', 'likes']
    table.index = range(1, table.shape[0]+1)
    print(table)

# fungsi input data
def more_data() :
    print('\n*****                                                                *****')
    print('* Masukkan data tambahan dengan format "[nama],[harga],[rating],[likes]" *')
    print('* Ketik "quit" jika sudah selesai memasukkan data tambahan               *')
    print('*****                                                                *****\n')

    add_data = input('Masukkan data :\n>> ')

    # input data berhenti ketika pengguna menekan enter
    while add_data != 'quit' and add_data != 'Quit' :
        add_data = add_data.split(',')

        # jumlah elemen tiap data harus sesuai dengan jumlah kolom
        if len(add_data) == 4 :
            try :
                # mengonversi input ke tipe data masing-masing
                new_data = [add_data[0],
                            int(add_data[1]),
                            float(add_data[2]),
                            int(add_data[3])]
                
                data.append(new_data)

            except ValueError :
                if '' in add_data or ' ' in add_data :
                    print('\nElemen tiap data tidak dapat kosong!\n')
                else :
                    print('\nTipe data tidak sesuai!\n')

            except TypeError :
                print('Data invalid!\n')

        else :
            print('\nIsi data tidak sesuai dengan jumlah kolom yang ada!\n')

        add_data = input('>> ')

# fungsi mengurutkan data
def sorting(array) :
    sorted_array = sorted(array, key=lambda sort:(sort[1], -sort[2], -sort[3]))
    return sorted_array

# sample data
data = [['Indomie', 3000, 5, 150],
        ['Laptop', 4000000, 4.5, 123],
        ['Aqua', 3000, 4, 250],
        ['Smart TV', 4000000, 4.5, 42],
        ['Headphone', 4000000, 3.5, 90],
        ['Very Smart TV', 4000000, 3.5, 87]]

# menampilkan data
print('Sample data :')
show(data)

# menambahkan data tambahan
inp = input('\nMasukkan data tambahan? [y/n]\n>> ')
while inp != 'n' and inp != 'N':
    if inp == 'y' or inp == 'Y':
        more_data()
        break
    
    inp = input('\n>> ')

# mengurutkan data
sorted_data = sorting(data)

# menampilkan data terurut
print('\nSorted data :')
show(sorted_data)


""" requirement : pip install openpyxl

    uncomment kode di bawah ini untuk membaca data dari file excel,
    masukkan alamat file diikuti dengan format file,
    berikut ini contoh penggunannya                                 """
    
# excel = pd.read_excel(r'C:\Users\Noh-a\sample.xlsx')

# list_data = excel.values
# list_data = list_data.tolist()

# sorted_excel = sorting(list_data)

# print('\nSorted excel data :')
# show(sorted_excel)
