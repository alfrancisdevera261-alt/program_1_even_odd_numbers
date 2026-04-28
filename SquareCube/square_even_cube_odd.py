class IntegerProcessor:

    def process(self):
        
        file = open("integers.txt", "r")
        
        even_results = []
        odd_results = []
        
        for line in file:
            number = int(line.strip())
            
            if number % 2 == 0:
                even_results.append(number ** 2)  # square
            else:
                odd_results.append(number ** 3)   # cube

        file.close()
        
        double_file = open("double.txt", "w")
        
        for num in even_results:
            double_file.write(str(num) + "\n")

        double_file.close()
        
        triple_file = open("triple.txt", "w")
        
        for num in odd_results:
            triple_file.write(str(num) + "\n")

        triple_file.close()
        
processor = IntegerProcessor()
processor.process()