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