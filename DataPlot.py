import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "AviationData.xlsx"
df = pd.read_excel(excel_file_path)  #"read_excel" is a method
#print(df)
###time series###
#filter
#df_aircraft_cat = df.loc[(df['Aircraft.Category'] == 'Airplane') & (df['Investigation.Type'] == 'Accident' )]
#sort
#df_aircraft_cat = df_aircraft_cat.sort_values(by=['Event.Date'])
#plot
#df_aircraft_cat.plot(x='Event.Date', y='Number.of.Engines')
#plt.show()

###bar or pie chart###
df_bar = df.groupby(['Broad.Phase.of.Flight']).sum()
#df_bar['Total.Serious.Injuries'].plot.bar()
df_bar['Total.Serious.Injuries'].plot.pie()
plt.show()
