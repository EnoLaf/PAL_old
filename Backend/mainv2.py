import json
import random
from Backend.utiles import Sortbooks

SB = Sortbooks()


def add_book(new_book_title, new_book_subtitle, new_book_writer, new_book_pages, new_book_styles, new_book_cover):
    SB.excel_to_json()

    new_book = {
        "title"     :"",
        "subtitle"  :"",
        "writer"    :"",
        "nb_pages"  :0,
        "style"     :"",
        "cover"     :"",
        "read"      :0
    }

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)

    new_book_pages.lstrip()
    new_book_pages_int = int(new_book_pages)

    new_book["title"]    = new_book_title
    new_book["subtitle"] = new_book_subtitle
    new_book["writer"]   = new_book_writer
    new_book["nb_pages"] = new_book_pages_int
    new_book["style"]    = new_book_styles
    new_book["cover"]    = new_book_cover
    new_book["read"]     = 0

    data.append(new_book)
    open("D:/Code/PAL/Backend/pal.json","w").close()
    with open("D:/Code/PAL/Backend/pal.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    SB.json_to_excel()
    print("Livre ajouté")


def add_read_book(title, subtitle):

    SB.excel_to_json()

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)
    for i in range(len(data)-1):
        if data[i]["title"] == title and data[i]["subtitle"] == subtitle:
            data[i]["read"]=1
            open("D:/Code/PAL/Backend/pal.json","w").close()
            with open("D:/Code/PAL/Backend/pal.json", "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            SB.json_to_excel()
            print("Livre ajouté comme lu")


def books():
    SB.excel_to_json()

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)

    list_title  = []
    list_writer = []
    list_books  = []

    for i in range(len(data)):
        book_title      = data[i]["title"]
        book_subtitle   = data[i]["subtitle"]
        book_writer     = data[i]["writer"]
        list_books.append(book_title+" - "+book_subtitle+" - "+book_writer)
    return list_books


def read_book():
    SB.excel_to_json()

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)

    list_title      = []
    list_writer     = []
    list_read_books = []

    for i in range(len(data)):
        if data[i]["read"] == 1:
            book_title  = data[i]["title"]
            book_subtitle   = data[i]["subtitle"]
            book_writer     = data[i]["writer"]
            list_read_books.append(book_title+" - "+book_subtitle+"   -   "+book_writer)
            lenght=len(list_read_books)
    return list_read_books, lenght

def tbr_book():
    SB.excel_to_json()

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)

    list_title      = []
    list_writer     = []
    list_tbr_books = []

    for i in range(len(data)):
        if data[i]["read"] == 0:
            book_title  = data[i]["title"]
            book_subtitle   = data[i]["subtitle"]
            book_writer     = data[i]["writer"]
            list_tbr_books.append(book_title+" - "+book_subtitle+"   -   "+book_writer)
            lenght=len(list_tbr_books)
    return list_tbr_books, lenght


def read_a_book(size, style):
    list_nb_pages      = []
    list_style         = []
    list_splited_style = []

    SB.excel_to_json()

    f=open("D:/Code/PAL/Backend/pal.json")
    data=json.load(f)

    for i in range(len(data)):
        if data[i]["read"] == 0:
            book_nb_pages = data[i]["nb_pages"]
            book_style    = data[i]["style"]
            list_nb_pages.append(book_nb_pages)
            list_style.append(book_style)

    for i in range(len(list_style)):
        tmp=list_style[i].split(",")
        list_splited_style.append(tmp)

    if  size == 1:
        SB.min = 0
        SB.max = 400

    elif size == 2:
        SB.min = 400
        SB.max = 600

    elif size == 3:
        SB.min = 600
        SB.max = 800

    elif size == 4:
        SB.min = 800
        SB.max = None

    filtered_books= SB.size_filtering(list_nb_pages, data)
    list_style_filtered_books = SB.style_filtering(style, filtered_books)
    return SB.random_filtered_book(list_style_filtered_books)
