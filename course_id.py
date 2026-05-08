'''Write a function add_course(d, s, courseID) which adds in the dictionary d the
courseID to the list of courses passed by student s. Implement an in-place modification.
• Write a function add_courses(d, s, course_list) which adds in the dictionary d
each course in the list course_list to the list of courses passed by student s.
Implement an in-place modification.
• Write a function that returns the list of courses of a given student in a given dictionary.
• Write a function that returns the list of students who have passed a given course in a given
dictionary.
• Write a function that returns the list of students in a given dictionary. The list must be
ordered by the last name of the students.
• Write a function that creates a new dictionary containing the statistics about the courses
present in a given dictionary. In particular, the new dictionary has the course identifier as
key and the number of students who passed the course as value for that key.
 --Write a program that prints the histogram of given courses. In particular, it prints as many
* as the number of students who have passed a given course. The histogram should be
printed in descending order.
• Write a function remove_course(d, studentID, courseID), which removes
from the dictionary d the course courseID from the student studentID. If this was
their only course, the student is removed from the dictionary.
d = {('Alice', 'Bianchi', 1234567): [1, 2, 3],
 ('Mario', 'Rossi', 7654321): [3, 4, 5],
 ('Chiara', 'Ferri', 3217654): [2, 3, 4, 5]}'''

def add_course(d,s,courseID):
    if s in d:
        d[s].append(courseID)
    else:
        d[s]= [courseID]
def add_courses(d,s,course_list):
    if s in d:
        d[s].extend(course_list)
    else:
        d[s]= course_list
def get_coursesl(d,s):
    if s in d:
        return d.get(s,[])
def course_student(d,courseID):
    course_students=[]
    for s in d:
        if courseID in d[s]:
            course_students.append(s)
    return course_students

def all_students(d):
    l=list()
    for s in d:
        l.append(s)
    l=sorted(l, key= lambda x:x[1])
    return l
def all_students_2(d):
    def lastname(s):
        return s[1]
    return sorted(d, key= lastname)


def stats_about_course(d):
    stats_d={}
    for s in d:
        for course in d[s]:
            if course not in stats_d:
                stats_d[course]=1
            else:
               stats_d[course]+=1
    return stats_d
def graphic_stats(d):
    ordered= sorted(stats_about_course(d).items(),key= lambda x: x[1], reverse= True)
    print(ordered)
    for k,v in ordered:
        print(f'{k}:'+'*'*v)
def delete_course(d,studentid, courseid):
    l= d.keys()
    for s in l:
        if s[2]== studentid:
            d[s].remove(courseid)
            if d[s]==0:
                del d[s]
        break
        
   
        
    
    
    

d = {('Alice', 'Zianchi', 1234567): [1, 2, 3],
 ('Mario', 'Rossi', 7654321): [3, 4, 5],
 ('Chiara', 'Ferri', 3217654): [2, 3, 4, 5],('Chiara', 'Fer', 321767): []}

print(stats_about_course(d))
graphic_stats(d)
print(all_students(d))
delete_course(1234567
    

