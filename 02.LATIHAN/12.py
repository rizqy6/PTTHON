# konversi celcius to farenheit
def konversi_suhu_farenheit(celcius):
    konversi_suhu_farenheit = 9 * celcius / 5 + 32
    return konversi_suhu_farenheit
# konversi farenheit to celcius
def konversi_suhu_celcius(farenheit):
    konversi_suhu_celcius = 5/9 * (farenheit - 32)
    return konversi_suhu_celcius


def main():
    print('     Program Konversi Suhu   ')
    print("""\
            1. Celcius   ke Farenheit
            2. Farenheit ke Celcius
        """)
    input1 = int(input('Masukan angka 1 atau 2 \t: '))
    if input1 == 1:
        temperature = int(input('Masukan Skala Celcius \t: '))
        print(f'Suhu {temperature} C setara dengan {konversi_suhu_farenheit(temperature)} Farenheit')
    elif input1 == 2:
        temperature = int(input('Masukan Skala Farenheit : '))
        print(f'Suhu {temperature} F setara dengan {konversi_suhu_celcius(temperature)} Celcius')
    else:
        print('Masukan input dengan benar')
   
   

if __name__=='__main__':
    main()