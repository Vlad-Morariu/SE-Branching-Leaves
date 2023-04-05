f = open("b2.json", "r")
b1 = f.read()
f.close()
import json

books2 = json.loads(b1)


def search_item_author(a, books):
    dir = {}
    for i in books:
        if a.upper() in books[i]['Author'].upper():
            dir.update({i: books[i]})

    return dir

def search_item_genre(a, books):
    dir = {}
    for i in books:
        if a.upper() in books[i]['Genre'].upper():
            dir.update({i: books[i]})

    return dir

def search_item_Length(a, books):
    dir = {}
    for i in books:
        if a == ("AnyLength"):
            dir.update({i: books[i]})
        if a == ("200-300"):
            if int(books[i]['Pages']) >= 200:
                if int(books[i]['Pages']) < 300:
                    dir.update({i: books[i]})
        if a == ("300-400"):
            if int(books[i]['Pages']) >= 300:
                if int(books[i]['Pages']) < 400:
                    dir.update({i: books[i]})
        if a == ("+400"):
            if int(books[i]['Pages']) >= 400:
                dir.update({i: books[i]})
        #if a.upper() in books[i]['Genre'].upper():

    return dir

def search_item_Period(a, books):
    dir = {}
    for i in books:
        if a == ("AnyPeriod"):
            dir.update({i: books[i]})
        if a == ("1980-1990"):
            if int(books[i]['Published Date']) >= 1980:
                if int(books[i]['Published Date']) < 1990:
                    dir.update({i: books[i]})
        if a == ("1990-2000"):
            if int(books[i]['Published Date']) >= 1990:
                if int(books[i]['Published Date']) < 2000:
                    dir.update({i: books[i]})
        if a == ("2000-2010"):

            if int(books[i]['Published Date']) >= 2000:
                if int(books[i]['Published Date']) < 2010:
                    dir.update({i: books[i]})
        if a == ("2010-2020"):
            #print(int(books[i]['Published Date']))
            if int(books[i]['Published Date']) >= 2010:
                if int(books[i]['Published Date']) < 2020:
                    dir.update({i: books[i]})
        if a == ("2020+"):
            if int(books[i]['Published Date']) >= 2020:
                dir.update({i: books[i]})
        if a == ("1980-"):
            if int(books[i]['Published Date']) < 1980:
                dir.update({i: books[i]})
    return dir

def search_item_Price(a, books):
    dir = {}
    for i in books:
        if a == ("None"):
            dir.update({i: books[i]})
        if a == ("<10"):
            if int(books[i]['Price']) <10:
                dir.update({i: books[i]})
        if a == ("10-20"):
            if int(books[i]['Price']) >= 10:
                if int(books[i]['Price']) < 20:
                    dir.update({i: books[i]})
        if a == ("20-30"):
            if int(books[i]['Price']) >= 20:
                if int(books[i]['Price']) < 30:
                    dir.update({i: books[i]})
        if a == ("30-40"):
            if int(books[i]['Price']) >= 30:
                if int(books[i]['Price']) < 40:
                    dir.update({i: books[i]})
        if a == ("40-50"):
            if int(books[i]['Price']) >=40:
                if int(books[i]['Price']) < 50:
                    dir.update({i: books[i]})
        if a == (">50"):
            if int(books[i]['Price']) >50:
                dir.update({i: books[i]})
    return dir

def search_item_Format(a, books):
    dir = {}
    for i in books:
        if a.upper() in books[i]['Type'].upper():
            dir.update({i: books[i]})

    return dir

def search_item_Language(a, books):
    dir = {}
    for i in books:
        if a.upper() in books[i]['Language'].upper():
            dir.update({i: books[i]})

    return dir

def cauta_carte(author, genre, published, pages, language, price, types, books):
    dict = search_item_genre(genre, books)
    if len(dict) == 1:
        return dict
    if len(dict) == 0:
        print("Sorry, there is no book available for your selected criteria. Please try again!")
    else:
        dict2= search_item_author(author, dict)
        if len(dict2) == 1:
            return dict2
        if len(dict2) == 0:
            print("Sorry, there is no book available for your selected criteria. Please try again!")
        else:
            dict3= search_item_Length(pages, dict2)
            if len(dict3) == 1:
                return dict3
            if len(dict3) == 0:
                print("Sorry, there is no book available for your selected criteria. Please try again!")
            else:
                dict4 = search_item_Period(published, dict3)
                if len(dict4) == 1:
                    return dict4
                if len(dict4) == 0:
                    print("Sorry, there is no book available for your selected criteria. Please try again!")
                    return {}
                else:
                    dict5 = search_item_Format(types, dict4)
                    if len(dict5) == 1:
                        return dict5
                    if len(dict5) == 0:
                        print("Sorry, there is no book available for your selected criteria. Please try again!")
                        return {}
                    else:
                        dict6 = search_item_Language(language, dict5)
                        if len(dict6) == 1:
                            return dict6
                        if len(dict6) == 0:
                            print("Sorry, there is no book available for your selected criteria. Please try again!")
                            return {}
                        else:
                            dict7 = search_item_Price(price, dict6)
                            if len(dict7) == 1:
                                return dict7
                            if len(dict7) == 0:
                                print("Sorry, there is no book available for your selected criteria. Please try again!")
                                return {}
                            else:
                                io= 0
                                for i in dict7:
                                    if dict7[i]['ID']> io:
                                        book = i
                                return book

def adauga_carte():
    f = open("b2.json", "r")
    b1 = f.read()
    f.close()
    import json
    books = json.loads(b1)
    name = input("Title: ")
    a = 0
    for i in books:
        if int(books[i].get('ID')) > a:
            a = int(books[i].get('ID'))
    id = a+1
    autor = input("Author: ")
    gen = input("Genre: ")
#    publisher = input("Publisher: ")
    publishedDate = input("Published Date: ")
#    IBSN = input("International Standard Book Number: ")
    language = input("Language: ")
    pageCount = input("Number of pages :")
    price = input("Price of book :")
    booktype = input("Kidle or Hardcover version:  ")
    description = input("Description :")
    book = {}
    book[name] = {
        'ID': id,
        'Title': name,
        'Author': autor,
        'Genre': gen,
#       'Publisher': publisher,
        'Published Date': publishedDate,
#       'IBSN-13': IBSN,
        'Pages': pageCount,
        'Language': language,
        'Price': price,
        'Type': booktype,
        'Description': description.strip(),

    }

    books.update(book)

    s = json.dumps(books)
    f = open("b2.json", "w")
    f.write(s)
    f.close()

def add_item(a,b,c):
    f = open("b2.json", "r")
    b1 = f.read()
    f.close()
    import json
    books = json.loads(b1)
    books[a].update({b:c})
    s = json.dumps(books)
    f = open("b2.json", "w")
    f.write(s)
    f.close()

def delete_item(a):
    f = open("b2.json", "r")
    b1 = f.read()
    f.close()
    import json
    books = json.loads(b1)
    for i in books:
        books[i].pop(a)
    s = json.dumps(books)
    f = open("b2.json", "w")
    f.write(s)
    f.close()

def delete_book(a):
    f = open("b2.json", "r")
    b1 = f.read()
    f.close()
    import json
    books = json.loads(b1)
    for i in books:
        if i == a:
 #          print(i)
 #          del books[i]
            books.pop(a)
            break
    s = json.dumps(books)
    f = open("b2.json", "w")
    f.write(s)
    f.close()

def change_item(a,b,c):
    f = open("b2.json", "r")
    b1 = f.read()
    f.close()
    import json
    books = json.loads(b1)
    for i in books:
        if i == a:
            print(books[i][b])
            books[i].update({b: c})
    s = json.dumps(books)
    f = open("b2.json", "w")
    f.write(s)
    f.close()


############################################3
final= {}
final= cauta_carte('J. K. Rowling','Fantasy', '2010-2020', 'AnyLength', 'EN', '10-20', 'Hardcovered', books2 )
if final == {}:
   print('Please try again!')
else:
   for i in final:
        print(i)
        print(final[i]["Author"])
        print(final[i]["Description"])
