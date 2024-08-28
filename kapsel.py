from kapsel.kapsel import Zeitkapsel

def main():
    print("Willkommen zur GitHub Zeitkapsel!")
    action = input("Möchten Sie eine [v]ersiegeln oder eine [ö]ffnen? (v/ö): ").strip().lower()
    
    if action == 'v':
        date_to_open = input("Geben Sie das Öffnungsdatum an (YYYY-MM-DD): ")
        kapsel_name = input("Geben Sie den Namen der Zeitkapsel an: ")
        data = input("Geben Sie die Daten an, die versiegelt werden sollen: ")
        
        kapsel = Zeitkapsel(date_to_open, kapsel_name)
        kapsel.versiegeln(data)
        
        print("Die Zeitkapsel wurde erfolgreich versiegelt!")
        print(f"Geheimschlüssel zum Öffnen: {kapsel.get_secret_key()}")

    elif action == 'ö':
        kapsel_name = input("Geben Sie den Namen der Zeitkapsel an: ")
        secret_key = input("Geben Sie den Geheimschlüssel ein: ").encode()
        
        kapsel = Zeitkapsel(date_to_open="2000-01-01", kapsel_name=kapsel_name, secret_key=secret_key)
        
        try:
            data = kapsel.oeffnen()
            print(f"Die Zeitkapsel enthält: {data}")
        except ValueError as e:
            print(e)
    
    else:
        print("Ungültige Option. Bitte wählen Sie [v]ersiegeln oder [ö]ffnen.")

if __name__ == "__main__":
    main()
