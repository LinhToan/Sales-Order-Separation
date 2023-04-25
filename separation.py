import pandas as pd
import numpy as np
import os

excelDF = pd.read_excel(r'M:\Turkey\BOLs\IA000012808_AbbyyBOL\Output\11_04_2021\Final Output\FinalOutput_11_04_2021_44.xlsx')
excelDF2 = excelDF.fillna('')
excelDF2.groupby(by='Sales Order Number')

# Create empty list to concat with dataframe
SOlist = []
# Create dataframe with column headers
cols = ['Sales Order Number', 'Pallet Number', 'Box Number', 'Material Number', 'Plant', 'Batch#', 'Stock Type', 'Quantity' 'UOM', 'Weight', 'Unit of Weight', 'Hold Reasons']
df = pd.DataFrame(SOlist, columns=cols)

test = [e for i, e in excelDF2.groupby('Sales Order Number')]

# Loop through SOnums and compare SO numbers.
for e in test:
    if len(SOlist) == 0:
        # If SOlist is empty, start process
        SOlist.append(e) 
    else:
        # If SOlist is non-empty and SO is in SOlist, then we're still on same SO
        if e['Sales Order Number'].isin(SOlist[0]['Sales Order Number']).all(): 
            SOlist.append(e)
        # If SO not in SOlist and SOlist is non-empty, we've reached a new SO
        else: 
            # If we reach a new SO, then concat with dataframe
            df = pd.concat(SOlist, axis=0, ignore_index=True) 
            df.to_string(index=False)
            df.to_csv(r'M:\Turkey\BOLs\IA000012808_AbbyyBOL\Output\11_04_2021\Final Output\SO upload files\{}.csv'.format(SOlist[0]['Sales Order Number'].unique()), index=False)
            SOlist = []
            df = pd.DataFrame(SOlist, columns=cols)
