class ReadBlast:
    '''A class to read the output from BLAST'''

    def __init__(self, file, evalue=0.001):
        self.file = file
        self.evalue = evalue

    def read7(self):
        reference = "Sequences producing significant alignments:                          (Bits)     Value\n"
        with open(self.file) as fn:
            lines = fn.readlines()
        if reference in lines:
            index = lines.index(reference)
            result = lines[index + 2].split(' ')
            e = result[-1].strip('\n')
            if float(e) < self.evalue:
                organism = result[1] + ' ' + result[2]
                return organism
            else:
                return 'no significant matches'
        else:
            return 'No Results'
