# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

book1 = {
        "title": "Danka a Janka",
        "pirce": 14.50,
        "author": "Mária Ďuríčková",
        "publication_year": 2023,
     }

book2 = {
        "title": "Kubko a zúbková víla",
        "pirce": 6.8,
        "author": "Marta Galewska-Kustra",
        "publication_year": 2025,
    }
books.append(book1)
books.append(book2)

print(books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
book1["pirce"] = 30
print(books)

# 3. Odstraň nějakou knihu. Vypiš list.
books.remove(book2)
print(books)

# 4. Vypiš celkový počet knih v listu.
books_count = len(books)
print(books_count)

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
b = input("Zadaj nazov nejakej knihy:")
c = input("Zadaj kto je autor:")
d = input("Zadaj rok vydania:")
e = input("Zadaj aka je Cena:")
book3 = {
    "title": b,
    "pirce":e,
    "author": c,
    "publication_year": d
    }
books.append(book3)
print(books)
