import optparse
import sys
from src.seater import Seater

_author__ = "Saloni Silvia"
__copyright__ = "Copyright (c) 2015"
__credits__ = ["Saloni Silvia"]
__license__ = "All Rights Reserved"
__version__ = "1.0.0"
__maintainer__ = "Saloni Silvia"
__email__ = "silvia.saloni@ucdconnect.ie"
__status__ = "Development"

def main(filename=None):
    # here we create the seater object
    seater = Seater(1000)
    
    # and we read the file line by line, feeding each line to the Seater
    with open(filename, 'r') as f:
        for line in f:
            seater.seat(line.strip())
            
    print ('number of occupied seats', seater.number_occupied())
    return

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-i', dest="filename", default='data/input_assign3.txt')
    options, remainder = parser.parse_args()
    
    sys.exit(main(filename=options.filename))
