class NumberProcessor:
    def process_number(self):
        file = open("numbers.txt", "r")
        
        even_numbers = []
        odd_numbers = []
        
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
        
        file.close()
        
        even_file = open("even.txt", "w")
        
        for num in even_numbers:
            even_file.write(str(num) + "\n")
            
        even_file.close()