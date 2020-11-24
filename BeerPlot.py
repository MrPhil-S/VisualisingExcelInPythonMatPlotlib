import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Beers.xlsx"
df = pd.read_excel(excel_file_path)  #"read_excel" is a method
#print(df)

#time series
df_bar = df.groupby(['style']).mean()
df_bar['abv'].plot.bar()
plt.show()
