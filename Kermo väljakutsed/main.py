def find_average():
    
    grades = [['english', 5, 4, 3, 4, 4, 3, 4, 4],
                 ['math', 4, 4, 5, 5, 4, 5, 5, 4, 5],
                 ['chemistry', 4, 3, 3, 2, 3, 4],
                 ['literature', 5, 5, 5, 4, 5, 5, 4],
                 ['biology', 4, 5, 4, 4, 3, 5, 5, 5]]
                 
    for _ in grades:
        sum_of_grades = 0
        grade_count = 0
        for grade in _:
            
            if(isinstance(grade, int)):
                sum_of_grades += grade
                grade_count += 1
            else:
                subject = grade
                
        average_grade = sum_of_grades / grade_count
        print('Your ' + subject + '\'s average grade is ' + repr(round(average_grade, 2)))
        
find_average()