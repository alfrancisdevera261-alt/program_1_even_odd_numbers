class StudentGWA:
    def get_highest_gwa(self): 
        
        file = open("students.txt", "r")
        
        highest_name = ""
        highest_gwa = 0
        
        for line in file:
            name, gwa = line.strip().split(",")
            gwa = float(gwa)