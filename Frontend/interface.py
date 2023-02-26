import tkinter
import tkinter.font as tkFont
from PIL            import Image, ImageTk
from tkinter        import ttk
from utiles         import Functions
import sys, pyglet, os

sys.path.append("D:\Code\PAL")
from Backend.mainv2 import read_a_book, books, add_book, read_book, add_read_book, tbr_book

F = Functions()

# Declaration of the different colors
color1 = '#F6E5D4'
color2 = '#DCCCB5'
color3 = '#A66254'

# Creation of the window + settings
app = tkinter.Tk()                                  # Tkinter initialization
app.geometry("1000x600")                            # Window sizing
app.resizable(0, 0)                                 # Non-resizable window
app.title("PAL")                                    # Set window title
app.iconbitmap('D:/Code/PAL/Images/icon_book.ico')  # Set window icon
app['bg'] = color1                                  # Set window background

# Declaration of the different fonts
font1 = tkFont.Font(family='Bahnschrift', size=30, weight='bold')
font2 = tkFont.Font(family='Bahnschrift', size=26, weight='bold')
font3 = tkFont.Font(family='Bahnschrift', size=22, weight='normal')
font4 = tkFont.Font(family='Bahnschrift', size=16, weight='normal')
font5 = tkFont.Font(family='Bahnschrift', size=14, weight='normal')

# Declaration of the different images
icon_return = F.creer_image("menu_close.png")
img_pal     = F.creer_image("pal.png")
img_book    = F.creer_image("book.png")

# Declaration of different functions
def clicked_button1(size, style):
    title, subtitle, writer, image, styles = read_a_book(size, style)
    frame_chosen_book            = F.create_frame(app, color1, 0, 0, 1000, 600)
    frame_chosen_book_left       = F.create_frame(frame_chosen_book, color3, 0, 0, 250, 600)
    frame_chosen_book_right      = F.create_frame(frame_chosen_book, color3, 975, 0, 25, 600)
    label_title                  = F.create_label(frame_chosen_book, title, font1, color1, 'black', 400, 100)
    label_subtitle               = F.create_label(frame_chosen_book, subtitle, font2, color1, 'black', 400, 150)
    label_writer                 = F.create_label(frame_chosen_book, writer, font3, color1, 'black', 400, 225)
    label_styles                 = F.create_label(frame_chosen_book, styles, font4, color1, 'black', 400, 275)
    return_button5               = F.create_button_image(frame_chosen_book, icon_return, color3, frame_menu, 25, 25)
    cover                        = F.create_image_cover(image)
    canva_chosen_book_cover      = F.create_canvas(frame_chosen_book, F.photo_image_cover, color1, 100, 100)

def clicked_button2(add_entry_title, add_entry_writer, add_entry_nb_pages, add_entry_style, add_entry_cover):
    frame_add               = F.create_frame(app, color1, 0, 0, 1000, 600)
    frame_add_left          = F.create_frame(frame_add, color3, 0, 0, 250, 600)
    frame_add_right         = F.create_frame(frame_add, color3, 975, 0, 25, 600)
    add_label_title         = F.create_label(frame_add, add_entry_title, font4, color1, 'black', 450, 100)
    add_label_title         = F.create_label(frame_add, add_entry_title, font4, color1, 'black', 450, 150)
    add_label_writer        = F.create_label(frame_add, add_entry_writer, font4, color1, 'black', 450, 200)
    add_label_nb_pages      = F.create_label(frame_add, add_entry_nb_pages, font4, color1, 'black', 450, 250)
    add_label_style         = F.create_label(frame_add, add_entry_style, font4, color1, 'black', 450, 300)
    cover                   = F.create_image_cover(add_entry_cover)
    canva_chosen_book_cover = F.create_canvas(frame_add, F.photo_image_cover, color1, 100, 100)
    return_button1          = F.create_button_image(frame_add, icon_return, color3, frame_menu, 25, 25)

    def create_button3(frame, texte, couleur, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
        button= tkinter.Button(frame, text=texte, bg=couleur, font=police, command=lambda:add_book(add_entry_title, add_entry_subtitle, add_entry_writer, add_entry_nb_pages, add_entry_style, add_entry_cover), relief=relief)
        button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
        return button

    button_confirm = create_button3(frame_add, "Valider", color3, font5, 700, 500, 200, 50)


#==================================Menu=====================================================================================================================================================
frame_menu      = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_central   = F.create_frame(frame_menu, color3, 200, 0, 600, 600)


#==============================Add a book===================================================================================================================================================
add_entry_title     = tkinter.StringVar()
add_entry_writer    = tkinter.StringVar()
add_entry_nb_pages  = tkinter.IntVar()
add_entry_style     = tkinter.StringVar()
add_entry_cover     = tkinter.StringVar()

frame_add           = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_add_top       = F.create_frame(frame_add, color3, 0, 0, 1000, 100)
frame_add_bottom    = F.create_frame(frame_add, color3, 0, 500, 1000, 100)
canva_pal           = F.create_canvas(frame_add, img_pal, color1, 700, 230)
add_label_big_title = F.create_label(frame_add_top, "Ajouter un livre", font1, color3, 'white', 300, 15)
add_label_title     = F.create_label(frame_add, "Titre :", font5, color1, 'black', 100, 150)
add_label_subtitle  = F.create_label(frame_add, "Sous-titre :", font5, color1, 'black', 100, 200)
add_label_writer    = F.create_label(frame_add, "Auteur :", font5, color1, 'black', 100, 250)
add_label_nb_pages  = F.create_label(frame_add, "Nombre de pages :", font5, color1, 'black', 100, 300)
add_label_style     = F.create_label(frame_add, "Genres :", font5, color1, 'black', 100, 350)
add_label_cover     = F.create_label(frame_add, "Couverture :", font5, color1, 'black', 100, 400)
add_entry_title     = F.create_entry(frame_add, 300, 155)
add_entry_subtitle  = F.create_entry(frame_add, 300, 205)
add_entry_writer    = F.create_entry(frame_add, 300, 255)
add_entry_nb_pages  = F.create_entry(frame_add, 300, 305)
add_entry_style     = F.create_entry(frame_add, 300, 355)
add_entry_cover     = F.create_entry(frame_add, 300, 405)
return_button1      = F.create_button_image(frame_add, icon_return, color3, frame_menu, 25, 25)

def create_button2(frame, texte, couleur, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur, font=police, command=lambda:clicked_button2(add_entry_title.get(), add_entry_writer.get(), add_entry_nb_pages.get(), add_entry_style.get(), add_entry_cover.get()), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button

button_confirm      = create_button2(frame_add_bottom, "Valider", color2, font5, 725, 25, 200, 50)


#================================Livres lus==================================================================================================================================================
def read_books():
    frame_read_books             = F.create_frame(app, color1, 0, 0, 1000, 600)
    frame_read_books_top         = F.create_frame(frame_read_books, color3, 0, 0, 1000, 100)
    frame_read_books_bottom      = F.create_frame(frame_read_books, color3, 0, 550, 1000, 50)
    read_books_label_big_title   = F.create_label(frame_read_books_top, "Livres lus", font1, color3, 'white', 350, 15)
    return_button6               = F.create_button_image(frame_read_books, icon_return, color3, frame_menu, 25, 25)
    listbox_read_books           = F.create_listbox(frame_read_books, color1, color3, font5, 50, 100, 900, 450)

    list_read_books, lenght = read_book()
    for item in list_read_books:
        listbox_read_books.insert("end", item)

    label_read_books             = F.create_label(frame_read_books_bottom, ("Nombre de livres lus : "+str(lenght)), font4, color3, 'white', 50, 10)

def create_button_read_books(frame, texte, couleur1, couleur2, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur1, fg=couleur2, font=police, command=lambda:read_books(), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button


#================================Livres à lire==================================================================================================================================================
def tbr_books():
    frame_tbr_books             = F.create_frame(app, color1, 0, 0, 1000, 600)
    frame_tbr_books_top         = F.create_frame(frame_tbr_books, color3, 0, 0, 1000, 100)
    frame_tbr_books_bottom      = F.create_frame(frame_tbr_books, color3, 0, 550, 1000, 50)
    tbr_books_label_big_title   = F.create_label(frame_tbr_books_top, "Livres à lire", font1, color3, 'white', 350, 15)
    return_button7              = F.create_button_image(frame_tbr_books, icon_return, color3, frame_menu, 25, 25)
    listbox_tbr_books           = F.create_listbox(frame_tbr_books, color1, color3, font5, 50, 100, 900, 450)

    list_tbr_books, lenght = tbr_book()
    for item in list_tbr_books:
        listbox_tbr_books.insert("end", item)

    label_tbr                   = F.create_label(frame_tbr_books_bottom, ("Nombre de livres à lire : "+str(lenght)), font4, color3, 'white', 50, 10)

def create_button_tbr_books(frame, texte, couleur1, couleur2, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur1, fg=couleur2, font=police, command=lambda:tbr_books(), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button


#==============================Read a book==================================================================================================================================================
frame_read          = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_read_top      = F.create_frame(frame_read, color3, 0, 0, 1000, 175)
frame_read_bottom   = F.create_frame(frame_read, color3, 0, 575, 1000, 25)
return_button4      = F.create_button_image(frame_read, icon_return, color3, frame_menu, 25, 25)

size  = tkinter.IntVar()
style = tkinter.StringVar()

check_400           = F.create_radiobutton(frame_read, "moins de 400 pages", color1, size, 1, 'Bahnschrift', 105, 225)
check_400_600       = F.create_radiobutton(frame_read, "400 à 600 pages", color1, size, 2, 'Bahnschrift', 315, 225)
check_600_800       = F.create_radiobutton(frame_read, "600 à 800 pages", color1, size, 3, 'Bahnschrift', 525, 225)
check_800           = F.create_radiobutton(frame_read, "plus de 800 pages", color1, size, 4, 'Bahnschrift', 735, 225)
fantasy             = F.create_checkbutton(frame_read, "Fantasy", color1, style, "fantasy", 'Bahnschrift', 105, 315)
science_fiction     = F.create_checkbutton(frame_read, "Science Fiction", color1, style, "science_fiction", 'Bahnschrift', 105, 355)
romance             = F.create_checkbutton(frame_read, "Romance", color1, style, "romance", 'Bahnschrift', 105, 395)
aventure            = F.create_checkbutton(frame_read, "Aventure", color1, style, "aventure", 'Bahnschrift', 105, 435)
amitie              = F.create_checkbutton(frame_read, "Amitié", color1, style, "amitie", 'Bahnschrift', 315, 315)
famille             = F.create_checkbutton(frame_read, "Famille", color1, style, "famille", 'Bahnschrift', 315, 355)
royaute             = F.create_checkbutton(frame_read, "Royauté", color1, style, "royaute", 'Bahnschrift', 315, 395)
pouvoir             = F.create_checkbutton(frame_read, "Pouvoir", color1, style, "pouvoir", 'Bahnschrift', 315, 435)
magie               = F.create_checkbutton(frame_read, "Magie", color1, style, "magie", 'Bahnschrift', 525, 315)
sorciere            = F.create_checkbutton(frame_read, "Sorcière", color1, style, "sorciere", 'Bahnschrift', 525, 355)
vampire             = F.create_checkbutton(frame_read, "Vampire", color1, style, "vampire", 'Bahnschrift', 525, 395)
loup_garou          = F.create_checkbutton(frame_read, "Loup Garou", color1, style, "loup_garou", 'Bahnschrift', 525, 435)
ado                 = F.create_checkbutton(frame_read, "Ado", color1, style, "ado", 'Bahnschrift', 735, 315)
young_adult         = F.create_checkbutton(frame_read, "Young Adult", color1, style, "young_adult", 'Bahnschrift', 735, 355)
smut                = F.create_checkbutton(frame_read, "Smut", color1, style, "smut", 'Bahnschrift', 735, 395)
horreur             = F.create_checkbutton(frame_read, "Horreur", color1, style, "horreur", 'Bahnschrift', 735, 435)

def create_button1(frame, texte, couleur, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur, font=police, command=lambda:clicked_button1(size.get(), style.get()), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button

button_confirm      = create_button1(frame_read, "Valider", color3, font5, 750, 500, 200, 50)


#============================All books======================================================================================================================================================
frame_all_books             = F.create_frame(app, color1, 0, 0, 1000, 600)
frame_all_books_top         = F.create_frame(frame_all_books, color3, 0, 0, 1000, 100)
frame_all_books_bottom      = F.create_frame(frame_all_books, color3, 0, 500, 1000, 100)
all_books_label_big_title   = F.create_label(frame_all_books_top, "Tous les livres", font1, color3, 'white', 350, 15)
return_button5              = F.create_button_image(frame_all_books, icon_return, color3, frame_menu, 25, 25)
listbox_all_books           = F.create_listbox(frame_all_books, color1, color3, font5, 50, 100, 900, 400)

list_books = books()
for item in list_books:
    listbox_all_books.insert("end", item)

def read():
    selected_book = listbox_all_books.selection_get()
    tmp=selected_book.split(" - ")
    selected_book_title     = tmp[0]
    selected_book_subtitle  = tmp[1]
    selected_book_writer    = tmp[2]
    add_read_book(selected_book_title, selected_book_subtitle)


def create_button_read(frame, texte, couleur, police, posX, posY, largeur, hauteur, relief="flat", ancre="nw"):
    button= tkinter.Button(frame, text=texte, bg=couleur, font=police, command=lambda:read(), relief=relief)
    button.place(x=posX, y=posY, anchor=ancre, width=largeur, height=hauteur)
    return button

button_all_books_read = create_button_read(frame_all_books_bottom, "Livre lu", color2, font5, 700, 25, 200, 50)



#=============================Menu's buttons================================================================================================================================================
button_read_a_book  = F.create_button(frame_central, "Lire un livre", color2, color3, font5, frame_read, 200, 75, 200, 50)
button_add_book     = F.create_button(frame_central, "Ajouter un livre", color2, color3, font5, frame_add, 200, 175, 200, 50)
button_books_read   = create_button_read_books(frame_central, "Livres lus", color2, color3, font5, 200, 275, 200, 50)
button_tbr_books    = create_button_tbr_books(frame_central, "Livres à lire", color2, color3, font5, 200, 375, 200, 50)
button_all_books    = F.create_button(frame_central, "Tous les livres", color2, color3, font5, frame_all_books, 200, 475, 200, 50)

F.show_frame(frame_menu)

app.mainloop()
