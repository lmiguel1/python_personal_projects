import random

def run():

    watches = {
        'Instinct': '1',
        'G-Shock Black': '2',
        'G-Shock Green': '3',
        'Protrek': '4',
        'Riseman': '5',
        'G-Shock G-7900': '6',
        'G-Shock DW-5600E': '7'}

    print("\n             ***** Welcome. This program will help to choose a wristwatch for today *****\n")
    cond = True

    while cond:
        for watch, value in watches.items():  # Con esto se imprime en pantalla cada uno de los elementos del iterable.
            print(value, '-',  watch)

        yesterday_watch = input("\nEnter the number corresponding to the watch used yesterday and press enter: \n")

        aleas = random.choice(list(watches.values()))  # Elige aleatoriamente un valor del diccionario.

        today_watch = (list(watches.keys())[list(watches.values()).index(aleas)])  # Si estamos buscando la clave
        # correspondiente al valor 'v' en el diccionario 'd', el código será: list(d.keys())[list(d.values()).index(v)]

        if yesterday_watch not in watches.values():
            print("Invalid input. Please try again.\n")

        elif yesterday_watch == aleas:
            print(f"\nThe watch for today is: {today_watch}, the same one used yesterday. Please try again.\n")
            print(input('Press enter to continue...'))

        else:
            print(f"\nThe watch for today is: '{today_watch.upper()}'. Have a nice day!")
            cond = False


if __name__ == '__main__':
    run()
