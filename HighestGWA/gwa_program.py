class StudentGWA:
    def get_highest_gwa(self): 
        
        file = open("students.txt", "r")
        
        highest_name = ""
        highest_gwa = 0