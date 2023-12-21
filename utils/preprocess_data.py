import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


filename = "box2_DEFAULT_T46.csv"
filepath = fr"C:\Users\vedan\Desktop\project\data\raw\initial data\{filename}"

df = pd.read_csv(filepath, header=None)
#df.drop('Timestamp',axis=1, inplace=True)
print("Contents in csv file:", df)
#print(df.columns)
