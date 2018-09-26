"""Functions to parse a file containing student data."""


def unique_houses(filename):
    """Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> sorted(unique_houses("cohort_data.txt"))
    ["Dumbledore's Army", 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    """

    houses = set()

    # Code goes here
    my_file = open(filename).readlines()

    for line in my_file:
        my_line_split = line.strip().split("|")
        my_house = my_line_split[2]
        if my_house != "":
            houses.add(my_house)

    return houses


def sort_by_cohort(filename):
    """Return a list of all cohort lists, including ghosts but not instructors.

    Sort students by cohort, skipping instructors.

    Iterate over the data to create a list for each cohort. Puts ghosts into a
    separate list called "ghosts".

    For example:

    >>> sort_by_cohort("cohort_data.txt")
    [['Harry Potter', 'Mandy Brocklehurst', 'Ron Weasley', 'Oliver Wood', 'Colin Creevey', 'Cho Chang', 'Michael Corner', 'Draco Malfoy', 'Seamus Finnigan', 'Eddie Carmichael', 'Theodore Nott', 'Terence Higgs', 'Hermione Granger', 'Penelope Clearwater', 'Angelina Johnson', 'Dennis Creevey'], ['Neville Longbottom', 'Cedric Diggory', 'Pansy Parkinson', 'Anthony Goldstein', 'Padma Patil', 'Luna Lovegood', 'Eleanor Branstone', 'Lee Jordan', 'Marietta Edgecombe', 'Andrew Kirke', 'Ginny Weasley', 'Mary Macdonald', 'Blaise Zabini', 'Natalie McDonald', 'Adrian Pucey', 'Hannah Abbott', 'Graham Pritchard', 'Susan Bones', 'Roger Davies', 'Owen Cauldwell'], ['Laura Madley', 'Orla Quirke', 'Parvati Patil', 'Eloise Midgeon', 'Zacharias Smith', 'Cormac McLaggen', 'Lisa Turpin', 'Demelza Robins', 'Ernie Macmillan', 'Millicent Bullstrode', 'Percy Weasley', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Miles Bletchley', 'Malcolm Baddock'], ['Marcus Belby', 'Euan Abercrombie', 'Vincent Crabbe', 'Ritchie Coote', 'Katie Bell', 'Terry Boot', 'Lavender Brown', 'Gregory Goyle', 'Marcus Flint', 'Dean Thomas', 'Jack Sloper', 'Rose Zeller', 'Stewart Ackerley', 'Fred Weasley', 'George Weasley', 'Romilda Vane', 'Alicia Spinnet', 'Kevin Whitby'], ['Friendly Friar', 'Grey Lady', 'Nearly Headless Nick', 'Bloody Baron']]
    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    # Code goes here
    my_file = open(filename).readlines()

    for line in my_file:
        my_line_split = line.strip().split("|")
        my_cohort = my_line_split[4]
        my_name = my_line_split[0] + " " + my_line_split[1]
        
        if my_cohort == "Winter 2016":
            winter_16.append(my_name)
        elif my_cohort == "Spring 2016":
            spring_16.append(my_name)
        elif my_cohort == "Summer 2016":
            summer_16.append(my_name)
        elif my_cohort == "Fall 2015":
            fall_15.append(my_name)
        elif my_cohort == "G":
            ghosts.append(my_name)
    
    # expects cohorts in a certain order...
    all_students.append(fall_15)
    all_students.append(winter_16)
    all_students.append(spring_16)
    all_students.append(summer_16)
    all_students.append(ghosts)

    return all_students


def hogwarts_by_house(filename):
    """Sort students into lists by house and return all lists in one list.

    Iterate over the data to create an alphabeticaly sorted list for each
    house, and sorts students into their appropriate houses by last name. Sorts
    ghosts into a list called "ghosts" and instructors into a list called
    "instructors". Add them, in that order, to your list of houses.

    For example:
    >>> hogwarts_by_house("cohort_data.txt")
    [['Abbott', 'Chang', 'Creevey', 'Creevey', 'Edgecombe', 'Nott', 'Spinnet'], ['Abercrombie', 'Bell', 'Brown', 'Coote', 'Finnigan', 'Granger', 'Johnson', 'Jordan', 'Kirke', 'Longbottom', 'Macdonald', 'McDonald', 'McLaggen', 'Patil', 'Peakes', 'Potter', 'Robins', 'Sloper', 'Thomas', 'Vane', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Wood'], ['Bones', 'Branstone', 'Cauldwell', 'Diggory', 'Finch-Fletchley', 'Macmillan', 'Madley', 'Midgeon', 'Smith', 'Whitby', 'Zeller'], ['Ackerley', 'Belby', 'Boot', 'Brocklehurst', 'Carmichael', 'Clearwater', 'Corner', 'Davies', 'Goldstein', 'Lovegood', 'Patil', 'Quirke', 'Turpin'], ['Baddock', 'Bletchley', 'Bullstrode', 'Crabbe', 'Flint', 'Goyle', 'Higgs', 'Malfoy', 'Parkinson', 'Pritchard', 'Pucey', 'Zabini'], ['Baron', 'Friar', 'Lady', 'Nick'], ['Flitwick', 'McGonagall', 'Snape', 'Sprout']]

    """

    all_hogwarts = []
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # Code goes here
    my_file = open(filename).readlines()

    for line in my_file:
        my_line_split = line.strip().split("|")
        my_house = my_line_split[2]
        my_cohort = my_line_split[4]
        last_name = my_line_split[1]
        
        if my_house == "Dumbledore's Army":
            dumbledores_army.append(last_name)
        elif my_house == "Gryffindor":
            gryffindor.append(last_name)
        elif my_house == "Hufflepuff":
            hufflepuff.append(last_name)
        elif my_house == "Ravenclaw":
            ravenclaw.append(last_name)
        elif my_house == "Slytherin":
            slytherin.append(last_name)
        else:
            if my_cohort == "G":
                ghosts.append(last_name)
            elif my_cohort == "I":
                instructors.append(last_name)
    
    all_hogwarts.append(sorted(dumbledores_army))
    all_hogwarts.append(sorted(gryffindor))
    all_hogwarts.append(sorted(hufflepuff))
    all_hogwarts.append(sorted(ravenclaw))
    all_hogwarts.append(sorted(slytherin))
    all_hogwarts.append(sorted(ghosts))
    all_hogwarts.append(sorted(instructors))

    return all_hogwarts


def all_students_tuple_list(filename):
    """Return a list of tuples of student data.

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:

    >>> all_students_data = all_students_tuple_list("cohort_data.txt")
    >>> print(all_students_data)
    [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Laura Madley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Orla Quirke', 'Ravenclaw', '', 'Spring 2016'), ('Marcus Belby', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Euan Abercrombie', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Neville Longbottom', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Vincent Crabbe', 'Slytherin', 'Snape', 'Summer 2016'), ('Parvati Patil', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Mandy Brocklehurst', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Ritchie Coote', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Eloise Midgeon', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Zacharias Smith', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Katie Bell', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Cedric Diggory', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Ron Weasley', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Cormac McLaggen', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Lisa Turpin', 'Ravenclaw', 'Flitwick', 'Spring 2016'), ('Oliver Wood', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Pansy Parkinson', 'Slytherin', 'Snape', 'Winter 2016'), ('Demelza Robins', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Terry Boot', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Lavender Brown', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Anthony Goldstein', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Ernie Macmillan', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Colin Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Padma Patil', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Cho Chang', "Dumbledore's Army", 'Flitwick', 'Fall 2015'), ('Gregory Goyle', 'Slytherin', 'Snape', 'Summer 2016'), ('Michael Corner', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Luna Lovegood', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Eleanor Branstone', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Draco Malfoy', 'Slytherin', 'Snape', 'Fall 2015'), ('Marcus Flint', 'Slytherin', 'Snape', 'Summer 2016'), ('Lee Jordan', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Marietta Edgecombe', "Dumbledore's Army", 'Flitwick', 'Winter 2016'), ('Andrew Kirke', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Ginny Weasley', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Mary Macdonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Blaise Zabini', 'Slytherin', 'Snape', 'Winter 2016'), ('Millicent Bullstrode', 'Slytherin', 'Snape', 'Spring 2016'), ('Seamus Finnigan', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Eddie Carmichael', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Dean Thomas', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Percy Weasley', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Jack Sloper', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Theodore Nott', "Dumbledore's Army", 'Snape', 'Fall 2015'), ('Terence Higgs', 'Slytherin', 'Snape', 'Fall 2015'), ('Jimmy Peakes', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Natalie McDonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Justin Finch-Fletchley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Rose Zeller', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Miles Bletchley', 'Slytherin', 'Snape', 'Spring 2016'), ('Stewart Ackerley', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Adrian Pucey', 'Slytherin', 'Snape', 'Winter 2016'), ('Fred Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hannah Abbott', "Dumbledore's Army", 'Sprout', 'Winter 2016'), ('Graham Pritchard', 'Slytherin', 'Snape', 'Winter 2016'), ('George Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hermione Granger', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Penelope Clearwater', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Malcolm Baddock', 'Slytherin', 'Snape', 'Spring 2016'), ('Angelina Johnson', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Susan Bones', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Dennis Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Roger Davies', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Romilda Vane', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Alicia Spinnet', "Dumbledore's Army", 'McGonagall', 'Summer 2016'), ('Kevin Whitby', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Owen Cauldwell', 'Hufflepuff', 'Sprout', 'Winter 2016')]
    """

    student_list = []

    # Code goes here
    my_file = open(filename).readlines()

    for line in my_file:
        my_line_split = line.strip().split("|")
        my_cohort = my_line_split[4]
        my_student_tuple = my_line_split[0] + " " + my_line_split[1], my_line_split[2], my_line_split[3], my_line_split[4]
        
        if my_cohort != "G" and my_cohort != "I":
            student_list.append(my_student_tuple)
            
    return student_list


def find_cohort_by_student_name(student_list):
    """Given full name, return student's cohort.

    Use list of tuples generated by all_students_tuple_list() to make a small
    function that, given a first and last name from the command line, return
    that student's cohort, or returns "Student not found." when appropriate.

    NOTE: This function isn't included in doctests. Test it by uncommenting the
    function call at the bottom of the file.

    For example:

    Who are you looking for? Harry Potter
    'Harry Potter was in the Fall 2015 cohort.'

    Who are you looking for? Tom Riddle
    'Student not found.'

    """

    # Code goes here
    all_students_data = all_students_tuple_list("cohort_data.txt")

    student_name = input("Who are you looking for? ")

    for student in all_students_data:
        # do something
        if student_name == student[0]:
            print(student_name + " was in the " + str(student[3]) + " cohort.")
            return
        
    print("Student not found.")

    return


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """Return a set of student last names that have duplicates.

    Iterate over the data to find any last names that exist across all cohorts.
    Use set operations (set math) to create and return a set of these names.

    For example:
    >>> find_name_duplicates("cohort_data.txt")
    {'Weasley'}

    """

    duplicate_names = set()

    # Code goes here
    winter_16 = set()
    spring_16 = set()
    summer_16 = set()
    fall_15 = set()

    my_file = open(filename).readlines()

    for line in my_file:
        my_line_split = line.strip().split("|")
        my_cohort = my_line_split[4]
        last_name = my_line_split[1]

        if my_cohort == "Winter 2016":
            winter_16.add(last_name)
        elif my_cohort == "Spring 2016":
            spring_16.add(last_name)
        elif my_cohort == "Summer 2016":
            summer_16.add(last_name)
        elif my_cohort == "Fall 2015":
            fall_15.add(last_name)

    duplicate_names = winter_16 & spring_16 & summer_16 & fall_15
        
    return duplicate_names


def find_house_members_by_student_name(student_list):
    """Prompt user for a student. Display everyone in their house and cohort.

     Prompt the user for the name via the command line and when given a name,
     print a statement of everyone in their house in their cohort.

     Use the list of tuples generated by all_students_tuple_list() to make a
     small function that, when given a student's first and last name, prints
     students that are in both that student's cohort and that student's house.

     NOTE: This function isn't included in doctests. Test it by uncommenting the
     function call at the bottom of the file.

     For example:

     Choose a student: Hermione Granger
     Hermione Granger was in house Gryffindor in the Fall 2015 cohort.
     The following students are also in their house:
     Seamus Finnigan
     Angelina Johnson
     Harry Potter
     Ron Weasley
     Oliver Wood

     """

    # Code goes here
    all_students_data = all_students_tuple_list("cohort_data.txt")

    student_name = input("Choose a student: ")

    for student in all_students_data:
        # do something
        if student_name == student[0]:
            print(student_name + " was in the house " + str(student[1]) + " in the " + str(student[3]) + " cohort.")
            
            print("The following students are also in their house and cohort:")
            for other_student in all_students_data:
                # do smething
                if student_name != other_student[0] and student[1] == other_student[1] and student[3] == other_student[3]:
                    print(other_student[0])
            
            return
        
    print("Student not found.")

    return


#############################################################################
# Here is some useful code to run these functions without doctests!
all_students_data = "Hermione Granger"
# find_cohort_by_student_name(all_students_data)
find_cohort_by_student_name(all_students_data)
find_house_members_by_student_name(all_students_data)


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#



if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
