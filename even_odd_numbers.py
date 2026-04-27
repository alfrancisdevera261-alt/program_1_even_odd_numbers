class NumberProcessor:
    def process_number(self):
        file = open("numbers.txt", "r")
        
        even_numbers = []
        odd_numbers = []
        
        for line in file:
            number = int(line.strip())
            