Books.objects.get
 all_books = Book.objects.all()
   for b in all_books:
       print(b.title, b.author, b.publication_year)  # Expected output: "1984 George Orwell 1949"
