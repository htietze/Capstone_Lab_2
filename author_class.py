
class Author:

    # setting up the author class, self ties it to the Author as a whole,
    # and then you use __init__ because it's the name is
    # the main label for the object
    def __init__(self, name):
        self.name = name
        self.books = []
    # while this is a separate method that isn't run at the start
    # but it's a method that can be called using the object name
    def publish(self, title):
        # if the title argument isn't found in the list, then it's added
        # could be made better by adding in checks for case
        if title not in self.books:
            self.books.append(title)
        else:
            print('This title is already added')
        # self.books.append(title)

    def __str__(self):
        # oh this is like. I know this kind of command from other languages
        # When you try to print the object, this is what gets returned
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():

    test = Author('Test Author')
    test.publish('A book 1')
    test.publish('B book 2')
    test.publish('B book 2')
    print(test)

    test2 = Author('Test Author2')
    print(test2)

main()