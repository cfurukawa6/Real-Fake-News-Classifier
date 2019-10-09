import pandas as pd 
import os
import numpy as np 





def read_file():

    cwd = os.getcwd()
    dfile = pd.read_csv((os.path.join(cwd, 'resized_v2.csv')), delimiter = ',')
    
    drop_list = ['Unnamed: 0','domain','id','scraped_at','inserted_at','updated_at','authors','keywords','meta_keywords','meta_description','tags','summary','source']

    dfile=dfile.drop(columns=drop_list)

    #indeces = set(dfile['type'].values)
    #print(indeces)

    dfile = dfile[dfile.type != 'rumor']
    dfile = dfile[dfile.type != np.nan]
    dfile = dfile[dfile.type != 'unknown']
    dfile = dfile[dfile.type != 'bias']
    dfile = dfile[dfile.type != 'satire']
    dfile = dfile[dfile.type != 'clickbait']
    dfile = dfile[dfile.type != 'junksci']
    dfile = dfile[dfile.type != 'political']
    dfile = dfile[dfile.type != '2018-02-10 13:43:39.521661']

    dfile.to_csv('new_data.csv',index=False)
    print('success')

def redefine_label():

    cwd = os.getcwd()
    dfile = pd.read_csv((os.path.join(cwd, 'new_data.csv')), delimiter = ',')

    #dfile['type'] = dfile['type'].replace('reliable', 1)
    #dfile['type'] = dfile['type'].replace('unr')

    dfile = dfile.replace('reliable', 1)
    dfile = dfile.replace('unreliable', 0)
    dfile = dfile.replace('fake', 0)
    dfile = dfile.replace('hate', 0)
    dfile = dfile.replace('conspiracy', 0)


    dfile.to_csv('new_data_labeled.csv', index=False)
    print('success')



if __name__ == '__main__':

    #drops rows 
    #read_file()

    redefine_label()



