import pandas as pd
import os 

# remove outliers
def remove_outliers(data, outlier_margin = 7.5):
    Q1 = data.quantile(0.25)
    Q3  = data.quantile(0.75)
    IQR = Q3 - Q1
    return data[(data > (Q1 - outlier_margin * IQR)) & (data < (Q3 + outlier_margin * IQR))]
#     return data[~((data > (Q1 - outlier_margin * IQR)) |(data < (Q3 + outlier_margin * IQR))).any(axis=1)]

if __name__ == "__main__":
   # read in electrical datas into a single CSV
   data = pd.DataFrame()
   path = "Data/Raw Data/"
   for file in os.listdir(path):
      data = data.append(pd.read_csv(path+file, skiprows=3), ignore_index=True)

   data["Timestamp"] = pd.to_datetime(data['Timestamp'])
   data.sort_values("Timestamp", ignore_index=True, inplace=True)
   data.to_csv("Data/Electrical_All.csv", index=False)   #save datas to csv

   # re-format
   data.set_index('Timestamp', inplace=True)
   data = data.groupby(data.index.floor('d')).mean()    # average electrical usage by days
   data = data[data.columns[[0,6,11,1,2,5,8,9,3,4,7,10,12]]]  # re-arrange to building types
   data = remove_outliers(data, 50)   # remove huge outliers
   data.to_csv("Data/Electrical_Averaged.csv")   # save processed data
