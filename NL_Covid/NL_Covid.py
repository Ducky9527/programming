#data source
#covid confirmed cases: https://coronadashboard.government.nl/verantwoording#confirmed-cases
#covid virus particles in waste water: https://coronadashboard.government.nl/verantwoording#virus-particles-in-wastewater
# 

import pandas as pd


#匯入好棒棒數據兩組
covid = pd.read_csv('NL_Covid/COVID-19_aantallen_gemeente_per_dag.csv', sep=";")
virus = pd.read_csv('NL_Covid/COVID-19_rioolwaterdata.csv', sep=";")



#清除不必要的欄位
covid = covid[['Date_of_publication', 'Province', 'Total_reported', 'Deceased']]
virus = virus[['Date_measurement', 'RWZI_AWZI_name', 'RNA_flow_per_100000']]

#改一下名字
virus = virus.rename(columns={"RWZI_AWZI_name" : "Site", 'RNA_flow_per_100000' : "Virus_Particles"})


print(" ")
print(" ")

print("confirmed covid cases")
print(" ")

print(covid.tail(10))

print("===========")
print("virus particles in water sewage ")
print(" ")

print(virus.tail(10))