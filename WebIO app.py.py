#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from PyPDF2 import PdfFileMerger
# use dict to sort by filepath or filename
file_dict = {}
for subdir, dirs, files in os.walk("C:/Users/Owner/Desktop/scrapy/test"):
    for file in files:
        filepath = subdir + os.sep + file
        # you can have multiple endswith
        if filepath.endswith((".pdf", ".PDF")):
            file_dict[file] = filepath
            print(file)
# use strict = False to ignore PdfReadError: Illegal character error
merger = PdfFileMerger(strict=False)

for k, v in file_dict.items():
    print(k, v)
    merger.append(v)

merger.write("C:/Users/Owner/Desktop/scrapy/test/final/single_file.pdf")


# In[3]:


import tabula as tb
import pandas as pd
df = tb.read_pdf("C:/Users/Owner/Desktop/scrapy/test/final/single_file.pdf",pages="all")
print(len(df))


# In[4]:


for i in range(len(df)):
    df[i].to_csv('C:/Users/Owner/Desktop/scrapy/test/final/test'+str(i)+'.csv')


# In[9]:


import os, glob
import pandas as pd



path = "C:/Users/Owner/Desktop/scrapy/test/final"



#Collecting all the files to be combined
all_files = glob.glob(os.path.join(path, "test*.csv"))



#Combining all the csv files and export the final csv file
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("C:/Users/Owner/Desktop/scrapy/test/final.csv")
