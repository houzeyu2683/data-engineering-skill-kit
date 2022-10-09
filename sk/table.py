
import pandas
import os

class engine:

    def __init__(self, folder):

        self.folder = folder
        return

    def scan(self, style='csv'):

        path = []
        name = []
        loop = os.listdir(self.folder)
        for i in loop:

            if(style=='csv'):

                condition = style in i.split('.')[-1]
                if(condition):

                    p = os.path.join(self.folder, i)
                    n = i.replace(".{}".format(style), "")
                    path += [p]
                    name += [n]
                    pass

                pass

            continue
        
        self.path = path
        self.name = name
        return

    def get(self, name):

        i = self.name.index(name)
        p = self.path[i]
        table = pandas.read_csv(p)
        return(table)

    pass
