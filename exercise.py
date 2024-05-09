from gfn import get_formatted_name

print("Wpisz 'q', aby zakończyć działanie programu.")
while True:
    first = input("\nPodaj imię: ")
    if first == "q":
        break
    middle = input("Podaj drugie imię, jeśli je posiadasz: ")
    if middle == "q":
        break
    last = input("Podaj nazwisko: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tEstetycznie sformatowane pełne imię i nazwisko: {formatted_name}.")