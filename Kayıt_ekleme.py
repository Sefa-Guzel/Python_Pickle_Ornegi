import pickle
def main():
    tekrar = 'e'   
    yazılacak_dosyam = open('veriler.dat', 'wb')
    while tekrar.lower() == "e":
        save_data(yazılacak_dosyam)
        tekrar = input('başka veri girilsin mi?(e/h:)')
    print('girilen veriler dosyaya yazıldı')
    print()
    print("dosyadan okunan veriler aşağıdadır:")
    yazılacak_dosyam.close()
    
    dosya_sonu = True
    okunacak_dosyam = open('veriler.dat','rb')
    while dosya_sonu:
        try:
            person=pickle.load(okunacak_dosyam)
            display_data(person)
        except EOFError:
            dosya_sonu=True
    okunacak_dosyam.close()
def save_data(file):
    person = {}
    person['ad'] = input("ad:")
    person['öğrenci no'] = int(input("öğrenci no:"))
    person['ortalama'] = float(input("ortalama:"))
    pickle.dump(person,file)
def display_data(person):
    print('ad:',person['ad'])
    print('öğrenci no:',person['öğrenci no'])
    print('not ortalaması:',person['ortalama'])
if __name__ == "__main__":
    main()