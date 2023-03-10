def konversi_suhu_farenheit(celcius):
    konversi_suhu_farenheit = 9 * celcius / 5 + 32
    return konversi_suhu_farenheit

def konversi_suhu_celcius(farenheit):
    konversi_suhu_celcius = (5/9 * (farenheit - 32))
    return konversi_suhu_celcius

  
print('         \tProgram Konversi Suhu   ')
option= """
            h. To show the available options 
            1. Convertion from Farenheit to Celcius
            2. Convertion from Celcius to Farenheit
            k. Exit
""" 
print (option)

def main():
    while True:

        input1 = str(input('Your Option \t: '))
        if input1 == "1":
            print("Your Option: 1")
            temperature = int(input('Enter Number for Conversion \t: '))
            print(f'Suhu {temperature} Farenheit = {konversi_suhu_celcius(temperature)} Celcius')
        elif input1 == "2":
            print("Your Option: 2")
            temperature = int(input('Enter Number for Conversion \t: '))
            print(f'Suhu {temperature} Celcius = {konversi_suhu_farenheit(temperature)} Farenheit')
        elif input1 == "h":
            print (option)
        elif input1 == "k":
            break
        else:
            print('Masukan input dengan benar')
   
   

if __name__=='__main__':
    main()

