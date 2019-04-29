#*****CLASSES*************************************************************************#
#*****USER****************************************************************************#
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name

    def change_email(self, address):
        self.email = address
        print("Email for %s has been updated to %s!" % (self.name, self.email))

    def __repr__(self):
        return "%s, %s, has recorded %i books!" % (self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.name:
            return True
        else: return False

    def read_book(self, book, rating = None):
        self.book = {book:rating}

    def get_average_rating(self):
        rating_total = 0
        count = 0
        for e in self.books.values():
            if e:
                rating_total+= e
                count += 1
        try: return rating_total/count
        except ZeroDivisionError:
            return 0
     
        

#*****BOOK****************************************************************************#
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        return "The ISBN for %s has been set to %i!" % (self.title, self.isbn)

    def add_rating(self, rating):
        if rating:
            if rating >=0 and rating <=4:
                self.rating.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, other_Book):
        if self.title == other_Book.title and self.isbn == other_Book.isbn:
            return True
        else:
            return False
    def get_average_rating(self):
        rating_total = 0
        for e in self.rating:
            rating_total += e
            
        if len(self.rating) > 0:
            return rating_total / len(self.rating)
        else:
            return 0
        
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        return "%s by Unknown" % (self.title)

#*****FICTION*************************************************************************#
class Fiction(Book):
    def __init__(self, title, author, isbn):
         super().__init__(title, isbn)
         self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "%s by %s" % (self.title, self.author)
            
#*****NON_FICTION*********************************************************************#
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
         super().__init__(title, isbn)
         self.subject = subject
         self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "%s, a %s manual on %s" % (self.title, self.level, self.subject)
    
#*****TOMERATER***********************************************************************#
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}


    def __repr__(self):
        string = "TomeRater has following users: \n"
        for e in self.users:
            string += self.users[e].get_name() + "\n"
        string += "They have read the following books: \n"
        for e in self.books:
            string += e.get_title() + "\n"
        return string
   
    def __eq__(self, other_rater):
        if self.users == other_rater.users and self.books == other_rater.books:
            return True
        else:
            return False

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with the email %s!" % (email))
                  
        user = self.users.get(email, None)
        
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for e in user_books:
                self.add_book_to_user(e, email)
    
    def print_catalog(self):
        print("Catalog list: ")
        for e in self.books.keys():
            print(e)

    def print_users(self):
        print("User list: ")
        for e in self.users.keys():
            print(e)

    def most_read_book(self):
        most_read_count = 0
        most_read_book = None
        for e in self.books:
            reads = self.books[e]
            if reads > most_read_count:
                most_read_count = reads
                most_read_book = e
        return "%s is the most read book being read by %i users" % (most_read_book, most_read_count)

    def highest_rated_book(self):
        highest_rated_book = None
        highest_rating = 0
        for e in self.books:
            rating = e.get_average_rating()
            
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_book = e
        return highest_rated_book

    def most_positive_user(self):
        most_positive_user = None
        highest_average_user_rating = 0
        for e in self.users.values():
            if e.get_average_rating() > highest_average_user_rating:
                most_positive_user = e
                highest_average_user_rating = e.get_average_rating()
        return most_positive_user







#*****__MAIN__************************************************************************#

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

print(Tome_Rater)

Tome_Rater_2 = TomeRater()
print(Tome_Rater == Tome_Rater_2)

Tome_Rater_3 = TomeRater()
Tome_Rater_3 = Tome_Rater
print(Tome_Rater == Tome_Rater_3)

