from dataclasses import dataclass

# I don't think I totally understand this @ part.
@dataclass
# creating the class, Student, similar to the Author one
class Student:
    # Only the object data is all set at once.
    # which means that when you make a Student object,
    # you have to have all of the data ready at that time. or allow for nulls maybe?
    name: str
    college_id: int
    gpa: float

def main():

    # using the dataclass to create Students, have to input all necessary data
    alice = Student('Alice', 12345, 4.0)
    bob = Student('Bob', 98765, 3.5)
    test = Student('Test', 13579, 2.5)
    # So something like this doesn't work because it's missing an argument:
    # test2 = Student('Test2', 00000)

    print(alice)
    print(bob)
    print(test)
    print(test.college_id)

main()

# I think dataclasses are if you have all the info at the time and 
# can create a full object at the start. Though I'm sure it's all editable
# traditional classes are a bit longer to write, and can use separate methods
# as a means for tying data to the object, and they don't worry about datatypes
# I'm not sure I really have a good idea of this yet.