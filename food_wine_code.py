import io
import pandas as pd
df = pd.read_csv(io.BytesIO(uploaded['food-categories.csv']))

def conv(txt):
    test_list = [0,0,0,0,0,0,0,0,0]
    for i in range(0,len(txt)-1,2): 
        test_list[int(i/2)] = int(txt[i+1])
    return(test_list) 

df['wine'] = df['turkey']
for i in range(len(df)):
    df['wine'][i] = [0,0,0,0,0,0,0,0,0]

for i in range(len(df)):
    row_list = [0,0,0,0,0,0,0,0,0]

    for column in df.columns[6:74]:
        l = conv (df[column][i])
        row_list = [row_list[i] + l[i] for i in range(len(l))]
    df['wine'][i] = row_list
