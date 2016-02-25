import re

_author__ = "Saloni Silvia"
__copyright__ = "Copyright (c) 2015"
__credits__ = ["Saloni Silvia"]
__license__ = "All Rights Reserved"
__version__ = "1.0.0"
__maintainer__ = "Saloni Silvia"
__email__ = "silvia.saloni@ucdconnect.ie"
__status__ = "Development"

# its a good idea to make a class to hold the various bits of data 
# and functions we need to solve this problem
class Seater:
    
    # this regular expression will give us the command and the rectangular bounding box
    # https://docs.python.org/2/library/re.html#re.MatchObject.group
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    def __init__(self, size=1000):
        self.nrows, self.ncols = size, size 
        self.room = [ [False]*self.ncols for row in range(self.nrows)]
    
    def get_cmd(self, line):
        #take the user input and converted to code
        cmd, x1, y1, x2, y2 = Seater.pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        
        
        return cmd, x1, y1, x2, y2
    
    def seat(self, line):
        #there are 3 command and what we do with that
        cmd, x1, y1, x2, y2 = self.get_cmd(line)
        print (cmd, x1, y1, x2, y2)
        if cmd == 'toggle':
            self.toggle(x1, y1, x2, y2)
        elif cmd == "occupy":
            self.occupy(x1, y1, x2, y2)
        elif cmd == 'empty':
            self.empty(x1, y1, x2, y2)
        # if someone misstype
        else:
            # YIKES!
            pass
        return
    
    def occupy(self, x1, y1, x2, y2):
        for row in range(x1,x2+1): 
            for col in range(y1,y2+1): 
                self.room[row][col] = True
        

    
    def empty(self, x1, y1, x2, y2):
        for row in range(x1,x2+1): 
            for col in range(y1,y2+1): 
                self.room[row][col] = False
        
        
    
    def toggle(self, x1, y1, x2, y2):
        for row in range(x1,x2+1): 
            for col in range(y1,y2+1): 
                if self.room[row][col] == True:
                    self.empty(row, col, row, col)
                else:
                    self.occupy(row, col, row, col)
        
    
    def number_occupied(self):
        count_full =0 
        for row in range(self.nrows): 
            for col in range(self.ncols): 
                if self.room[row][col] == True:
                    count_full +=1
        return count_full
    
if __name__ == '__main__':
    pass