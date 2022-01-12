"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!

    # each course is 6 units
    units = len(courses_list) * 6
    course_set = set()
    for course in courses_list:
        course_set.add(course)
        
    
    if target_course == "COMP1511":
        return True
    
    # 12 units in (COMP6843, COMP6445, COMP6845, COMP6447)"
    elif target_course == "COMP9301":
        unit = 0
        for course in course_set:
            if course == "COMP6443" or course == "COMP6445" or course == "COMP6845" or course == "COMP6447":
                unit += 6
            if unit == 12:
                return True
            
        
    
    elif target_course == "COMP3153":
        if "MATH1081" in course_set:
            return True
        
    
    elif target_course == "COMP3211":
        if "COMP3222" in course_set or "ELEC2141" in course_set:
            return True
       
    # "MATH1081 AND    (COMP1511 OR DPST1091 OR COMP1917 OR COMP1921)", 
    elif target_course == "COMP2111":
        if "MATH1081" in course_set and ("COMP1511" in course_set or "DPST1091" in course_set or "COMP1917" in course_set or "COMP1921" in course_set):
            return True
    
    return False




    