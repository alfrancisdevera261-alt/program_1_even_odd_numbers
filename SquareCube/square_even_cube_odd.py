import os

class IntegerProcessor:

    def process(self):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file = open(os.path.join(script_dir, "integers.txt"), "r")
        
        even_results = []
        odd_results = []
        
        for line in file:
            number = int(line.strip())
            
            if number % 2 == 0:
                even_results.append(number ** 2)  # square
            else:
                odd_results.append(number ** 3)   # cube

        file.close()
        
        double_file = open(os.path.join(script_dir, "double.txt"), "w")
        
        for num in even_results:
            double_file.write(str(num) + "\n")

        double_file.close()
        
        triple_file = open(os.path.join(script_dir, "triple.txt"), "w")
        
        for num in odd_results:
            triple_file.write(str(num) + "\n")

        triple_file.close()
        
processor = IntegerProcessor()
processor.process()