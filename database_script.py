import os
import pandas as pd 


def read_file():
    cwd = os.getcwd() #cwd right now is in Metriguard folder
    dfile = pd.read_csv((os.path.join(cwd, 'datasets/data.csv')), delimiter = ',')
    return dfile.values
def create_script(d):
    f = open("data_insert_statements.txt", 'w')

    f.write("INSERT INTO Articles (url, headline, body, label)\nVALUES\n")
    for row in d:
        f.write('(\'')
        temps = ''
        if (isinstance(row[0], str)):
            for i in range(0, len(row[0])):
                #if i == len(row[0])-2 and row[0][i] == '\n':
                    #temps += row[0][i]
                if (i != len(row[0])-1) or (i == len(row[0])-2 and row[0][i] != '\n'):
                    temps += row[0][i]

        else:
            print('wtf')
            h = input()

        f.write(temps)
        f.write('\', \'')
        temps = ''


        if isinstance(row[1], str):
            for i in range(0, len(row[1])):
                if (i != len(row[1])-1):
                    temps += row[1][i]

            #adding last character without checking if char results in encoding error
            if row[1][-1].isalpha():
                temps += row[1][-1]
        else:
            print('wtf')
            h = input()
        f.write(temps)
        f.write('\',\'')
        #h = input()

        #f.write('body\'')

        f.write('\', ')
        f.write('%d' % row[3])

        f.write('),\n')


        '''
        #f.write('%s' % row[0].encode("utf-8"))
        b = row[0].encode("utf-8")
        #f.write('{0}'.format(row[0].decode("utf-8")))
        f.write('%s' % b.decode("utf-8"))
        f.write('\', \'')
        s = row[1]
        f.write('%s' % s.encode("utf-8"))
        f.write('\',\'')
        g = row[2]
        if (isinstance(g,str)):
            f.write('%s' % g.encode("utf-8"))
        else:
            print(g)
            print(row[0])
            fuck = input()
        f.write('\', ')
        f.write('%d' % row[3])
        f.write('),\n')
        '''
        
    f.close()
if __name__ == '__main__':
    df1 = read_file()
    #print(df1[0][0])

    create_script(df1)

    #if isinstance(df1[0][2], str):
        #print('hey')

