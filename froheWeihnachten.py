import shutil


def christbaum():
    def input_pruefen():
        eingabe = input("Gib eine Zahl ein: ")

        try:
            eingabe = int(eingabe)

        except:
            print(
                "Heyy, du sollst eine ZAHL eingeben ;P\nIst " + eingabe + " eine Zahl? - Nein, ich glaube nicht ;)\n\n")
            christbaum()

        if eingabe < 4:
            print("Die Zahl sollte nicht kleiner als 4 sein.\n\n")
            christbaum()

        elif eingabe > 40:
            print("Die Zahl sollte nicht größer als 40 sein.\n\n")
            christbaum()

        else:
            baum_bauen(eingabe)

    def baum_bauen(eingabe):
        columns = shutil.get_terminal_size().columns
        i = 1
        while i in range(2 * eingabe):
            print((i * "+").center(columns))
            i = i + 2

        if eingabe < 10:
            print("#".center(columns))

        elif 10 <= eingabe < 20:
            print("##".center(columns))

        elif 20 <= eingabe < 30:
            print("###".center(columns))
            print("###".center(columns))

        elif 30 <= eingabe <= 40:
            print("###".center(columns))
            print("###".center(columns))
            print("###".center(columns))
        else:
            print("Fataler Fehler: Zahl " + eingabe + "ist größer als 40 oder keine Zahl.\nDes dürfte eigentlich nicht passieren!")


    input_pruefen()


christbaum()
