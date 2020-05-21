import urllib.request


class Kegg:
    '''A class for getting KEGG information'''

    def __init__(self, query, genes):
        self.query = query
        self.genes = genes

    def search(self, max_hit=1000):
        '''Searches the Kegg database and returns list of related genes'''
        organism = self.query.split(' ')
        x = urllib.request.urlopen('https://www.genome.jp/dbget-bin/www_bfind_sub?mode=bfind&max_hit='+ str(max_hit) + '&dbkey='
                                    + organism[0] + '+' + organism[1]+'&keywords='+ self.genes)

        page_list = str(x.read()).split('>')
        genes = [element.strip('</div ') for element in page_list if '(GenBank)' in element]

        return genes

    def output_file(self, genes, file_name):
        '''Creates a file that contains the genes'''
        fn = open(file_name, 'w')
        for gene in genes:
            fn.write(gene + '\n')
        fn.close()
