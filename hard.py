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
import re

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
    
    elif target_course == "COMP3211":
        if "COMP3222" in course_set or "ELEC2141" in course_set:
            return True
       
    # "MATH1081 AND    (COMP1511 OR DPST1091 OR COMP1917 OR COMP1921)", 
    elif target_course == "COMP2111":
        if "MATH1081" in course_set and ("COMP1511" in course_set or "DPST1091" in course_set or "COMP1917" in course_set or "COMP1921" in course_set):
            return True
    
    
    #"COMP1511    or DPST1091 or COMP1911 or COMP1917",
    elif target_course == "COMP1521":
        if "COMP1511" in course_set or "DPST1091" in course_set or "COMP1911" in course_set or "ELEC1917" in course_set:
            return True
    
    #"COMP1511 or DPST1091 or COMP1917 or COMP1921",
    elif target_course == "COMP1531" or target_course == "COMP2041":
        if "COMP1511" in course_set or "DPST1091" in course_set or "COMP1917" in course_set or "COMP1921" in course_set:
            return True
    
    # "COMP2121": "COMP1917 OR COMP1921 OR COMP1511 OR DPST1091 OR COMP1521 OR DPST1092 OR (COMP1911 AND MTRN2500)",
    elif target_course == "COMP2121":
        if "COMP1511" in course_set or "DPST1091" in course_set or "COMP1917" in course_set or "COMP1921" in course_set or "COMP1521" in course_set or "DPST1092" in course_set or ("COMP1911" in course_set or "MTRN2500" in course_set()):
            return True
        
    #"COMP2511": "COMP1531 AND (COMP2521 OR COMP1927)",
    elif target_course == "COMP2511":
        if "COMP1531" in course_set and ("COMP2521" in course_set or "COMP1927" in course_set): 
            return True
    
    #"COMP2521": "COMP1511    OR DPST1091 OR COMP1917 OR COMP1921",
    elif target_course == "COMP2521":
        if "COMP1531" in course_set and ("COMP2521" in course_set or "COMP1927" in course_set): 
            return True
    
    #  "COMP3121": "COMP1927 or    COMP2521.",
    elif target_course == "COMP3121":
        if "COMP1927" in course_set or "COMP2521" in course_set: 
            return True
        
    # "COMP3131": "COMP2511 or COMP2911",
    elif target_course == "COMP3131":
        if "COMP2511" in course_set or "COMP2911" in course_set: 
            return True
    
    # "COMP3131": "COMP2511 or COMP2911",
    elif target_course == "COMP3131":
        if "COMP2511" in course_set or "COMP2911" in course_set: 
            return True
    
    #"COMP3141": "COMP1927 or COMP2521.",
    elif target_course == "COMP3141":
        if "COMP1927" in course_set or "COMP2521" in course_set: 
            return True
    
    #"COMP3151": "COMP1927 OR ((COMP1521 or DPST1092) AND COMP2521)",
    elif target_course == "COMP3151":
        if "COMP1927" in course_set or (("COMP1521" in course_set or "DPST1092" in course_set) and "COMP2521" in course_set): 
            return True
    
    #"COMP3153": "MATH1081",
    elif target_course == "COMP3153":
        if "MATH1081" in course_set:
            return True

    # "COMP3161": "COMP2521 or COMP1927",
    elif target_course == "COMP3161":
        if "COMP2521" in course_set or "COMP1927" in course_set:
            return True

    #"COMP3900": "COMP1531 and (COMP2521 or COMP1927) and 102 units of credit",
    elif target_course == "COMP3900":
        if "COMP1531" in course_set and ("COMP2521" in course_set or "COMP1927" in course_set) and units >= 102:
            return True
       
    #"COMP3901": "Prerequisite: 12 units of credit in  level 1 COMP courses and 18 units of credit in level 2 COMP courses",
    elif target_course == "COMP3901":
        unit1 = 0
        unit2 = 0
        for course in course_set:
            # regex match to find comp1 courses
            if bool(re.search("COMP1", course)) == True:
                unit1 += 6
            if bool(re.search("COMP2", course)) == True:
                unit2 += 6
            # if more than 12 in unit comp1 and 18 in comp2
            if unit1 >= 12 and unit2 >= 18:
                return True
     
    
    # "COMP3902": "Prerequisite: COMP3901 and 12 units of credit in level 3 COMP courses",
    elif target_course == "COMP3902":
        if "COMP3901" in course_set:
            unit = 0
            for course in course_set:
                # regex match to find comp3 courses
                if bool(re.search("COMP3", course)) == True:
                    unit += 6
                
                if unit == 12:
                    return True
            
    
    # "COMP4121": "COMP3121 or   COMP3821",
    elif target_course == "COMP4121":
        if "COMP3121" in course_set or "COMP3821" in course_set:
            return True
    
    #"COMP4128": "Prerequisite: COMP3821 or (COMP3121 and 12 units of credit in level 3 COMP courses)",
    elif target_course == "COMP4121":
        unit = 0
        for course in course_set:
            # regex match to find comp3 courses
            if bool(re.search("COMP3", course)) == True:
                unit += 6
        
        if ("COMP3121" in course_set and unit >= 12) or "COMP3821":
            return True
        
    #"COMP4141": "Pre-requisite: MATH1081 and (COMP1927 or COMP2521)",
    elif target_course == "COMP4141":
        if "MATH1081" in course_set and ("COMP1927" in course_set or "COMP2521" in course_set):
            return True
       
    # "COMP4161": "Completion  of 18 units of credit", 
    elif target_course == "COMP4161":
        if units >= 18:
            return True
    
    #"COMP4336": "Prerequisite: COMP3331.", 
    elif target_course == "COMP4336":
        if "COMP3331" in course_set:
            return True
    
    # "COMP4418": "Pre-req: COMP3411",  
    elif target_course == "COMP4418":
        if "COMP3411" in course_set:
            return True
    
    # "COMP4601": "(COMP2511 or COMP2911) and completion of 24 units of credit",
    elif target_course == "COMP4601":
        if "COMP2511" in course_set or "COMP2911" in course_set and units >= 24:
            return True
        
    #"COMP4951": "36 units of credit in COMP courses",
    elif target_course == "COMP4951":
        if units >= 36:
            return True
        
    #"COMP4952": "4951",
    elif target_course == "COMP4952":
        if "COMP4951" in course_set:
            return True
    
    #"COMP4953": "4952",
    elif target_course == "COMP4953":
        if "COMP4952" in course_set:
            return True
    
    # "COMP9301": "12 units of credit in (COMP6443,  COMP6843, COMP6445, COMP6845, COMP6447)",
    elif target_course == "COMP9301":
        unit = 0
        for course in course_set:
            if course == "COMP6443" or course == "COMP6843" or course == "COMP6445" or course == "COMP6845" or course == "6447":
                unit += 6
            
            if unit == 12:
                return True
                
    
    #"COMP9302": "(COMP6441 OR COMP6841) AND 12 units of credit in (COMP6443, COMP6843, COMP6445, COMP6845, COMP6447)",
    elif target_course == "COMP9302":
        if "COMP6441" in course_set or "COMP6841" in course_set:
            unit = 0
            for course in course_set:
                if course == "COMP6443" or course == "COMP6843" or course == "COMP6445" or course == "COMP6845" or course == "6447":
                    unit += 6
                
                
                if unit == 12:
                    return True
    
    # "COMP9417": "MATH1081 and ((COMP1531 or COMP2041) or (COMP1927 or COMP2521))",
    elif target_course == "COMP9417":
        if "MATH1081" in course_set and (("COMP1531" in course_set or "COMP2041" in course_set) or ("COMP1927" in course_set or "COMP2521" in course_set)):
            return True
    
    # "COMP9418": "Prerequisite:  MATH5836 or COMP9417",
    elif target_course == "COMP9418":
        if "MATH5836" in course_set or "COMP9417" in course_set:
            return True
    
    # "COMP9444": "Prequisite: COMP1927 or COMP2521 or MTRN3500",    
    elif target_course == "COMP9444" or target_course == "COMP9447":
        if "COMP1927" in course_set or "COMP2521" in course_set or "MTRN3500" in course_set:
            return True
    
    # "COMP9491": "18 units oc credit in (COMP9417, COMP9418, COMP9444, COMP9447)"
    elif target_course == "COMP9491":
        
        unit = 0
        for course in course_set:
            if course == "COMP9417" or course == "COMP9418" or course == "COMP9444" or course == "COMP9447":
                unit += 6
            
            if unit == 18:
                return True
    
    return False




    