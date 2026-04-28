class IntegerProcessor:

    def process(self):
        
        file = open("integers.txt", "r")
        
        even_results = []
        odd_results = []
        
        for line in file:
            number = int(line.strip())