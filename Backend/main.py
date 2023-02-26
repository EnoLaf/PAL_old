import json
import random
from utiles import Sortbooks

SB = Sortbooks()

print("Menu : \n"   "\t1-Lire un livre\n"
                    "\t2-Ajouter un livre\n"
                    "\t3-Supprimer un livre\n")
menu=int(input("Choix : "))

if menu == 1:

    list_nb_pages      = []
    list_style         = []
    list_splited_style = []

    SB.excel_to_json()

    f=open("pal.json")
    data=json.load(f)

    for i in range(len(data)):
        book_nb_pages = data[i]["nb_pages"]
        book_style    = data[i]["style"]
        list_nb_pages.append(book_nb_pages)
        list_style.append(book_style)

    for i in range(len(list_style)):
        tmp=list_style[i].split(",")
        list_splited_style.append(tmp)

    size, style=SB.user_input()

    if  size == 1:
        SB.min = 0
        SB.max = 400
        filtered_books= SB.size_filtering(list_nb_pages, data)
        list_style_filtered_books = SB.style_filtering(style, filtered_books)
        SB.random_filtered_book(list_style_filtered_books)

    elif size == 2:
        SB.min = 400
        SB.max = 600
        filtered_books= SB.size_filtering(list_nb_pages, data)
        list_style_filtered_books = SB.style_filtering(style, filtered_books)
        SB.random_filtered_book(list_style_filtered_books)

    elif size == 3:
        SB.min = 600
        SB.max = 800
        filtered_books= SB.size_filtering(list_nb_pages, data)
        list_style_filtered_books = SB.style_filtering(style, filtered_books)
        SB.random_filtered_book(list_style_filtered_books)

    elif size == 4:
        SB.min = 800
        SB.max = None
        filtered_books= SB.size_filtering(list_nb_pages, data)
        list_style_filtered_books = SB.style_filtering(style, filtered_books)
        SB.random_filtered_book(list_style_filtered_books)

elif menu == 2:
    SB.excel_to_json()

    new_book = {
        "title"     :"",
        "writer"    :"",
        "nb_pages"  :0,
        "style"     :""
    }

    f=open("pal.json")
    data=json.load(f)

    new_book["title"]    = input("Quel est son titre?")
    new_book["writer"]   = input("Quel est son auteur?")
    new_book["nb_pages"] = int(input("Combien de pages fait le livre?"))
    new_book["style"]    = input("Quels genres?")

    data.append(new_book)
    open("pal.json","w").close()
    with open("pal.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    SB.json_to_excel()
    print("Livre ajouté")

elif menu == 3:
    SB.excel_to_json()

    f=open("pal.json")
    data=json.load(f)

    title=print("Quel livre veux-tu supprimer?\n")
    for i in range(len(data)-1):
        if data[i]["title"] == title:
            del data[i]
            open("pal.json","w").close()
            with open("pal.json", "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            SB.json_to_excel()
            print("Livre supprimé")
