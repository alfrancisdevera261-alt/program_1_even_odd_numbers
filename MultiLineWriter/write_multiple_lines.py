class MyLifeWriter:

    def write_lines(self):
        
        file = open("mylife.txt", "w")
        
        while True:
            
            line = input("Enter line: ")
            file.write(line + "\n")
            
            choice = input("Are there more lines y/n? ")
            
            if choice.lower() != 'y':
                break