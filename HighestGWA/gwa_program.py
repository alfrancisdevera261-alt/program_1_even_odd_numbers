import os

class StudentGWA:
    def get_highest_gwa(self): 
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file = open(os.path.join(script_dir, "students.txt"), "r")
        
        highest_name = ""
        highest_gwa = 0
        
        for line in file:
            name, gwa = line.strip().split(",")
            gwa = float(gwa)
            
            if gwa < highest_gwa:
                highest_gwa = gwa
                highest_name = name
                
        file.close()
        
        print("Highest GWA:")
        print(highest_name, "-", highest_gwa)
        
student = StudentGWA()
student.get_highest_gwa()