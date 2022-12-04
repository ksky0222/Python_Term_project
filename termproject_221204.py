import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

class excel:
    def __init__(self, address):
        self.address = address
    
    def get_data(self):
        if(self.address[-3:] == 'csv'):
            return pd.read_csv(self.address)
        else:
            return pd.read_excel(self.address)


def convert_data_populationratio(address, str1, str2, new_name):
    excel1 = excel(address)
    data1 = excel1.get_data()
    data2 = data1.columns[1:].to_list() # 연도추출
    data3 = (data1.loc[1])[1:].to_list() # 데이터 추출
    new_data = {
        str1 : data2,
        str2 : data3
    }
    columns = [str1,str2]
    new_df = pd.DataFrame(new_data, columns= columns)
    base_address = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/'
    new_df.to_csv(base_address+new_name)

def convert_data_fertilityrate(address, str1, str2, new_name):
    excel1 = excel(address)
    data1 = excel1.get_data()
    data2 = data1.columns[1:].to_list() # 연도추출
    data3 = (data1.loc[0])[1:].to_list() # 데이터 추출
    new_data = {
        str1 : data2,
        str2 : data3
    }
    columns = [str1,str2]
    new_df = pd.DataFrame(new_data, columns= columns)
    base_address = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/'
    new_df.to_csv(base_address+new_name)




# 원본데이터 불러오기

address_rawdata_fertilityrate = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/시도_합계출산율__모의_연령별_출산율_(1993-2021).csv'
excel_rawdata_fertilityrate = excel(address_rawdata_fertilityrate)
raw_data_fertilityrate = excel_rawdata_fertilityrate.get_data()
raw_data_fertilityrate

address_rawdata_under14 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/0-14세 인구비율.csv'
excel_rawdata_under14 = excel(address_rawdata_under14)
raw_data_under14 = excel_rawdata_under14.get_data()

address_rawdata_15_64 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/15-64세 인구비율.csv'
excel_rawdata_15_64 = excel(address_rawdata_15_64)
raw_data_15_64 = excel_rawdata_15_64.get_data()

address_rawdata_over65 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/65세이상 인구비율.csv'
excel_rawdata_over65 = excel(address_rawdata_over65)
raw_data_over65 = excel_rawdata_over65.get_data()

# 원본데이터 가공하기
convert_data_fertilityrate(address_rawdata_fertilityrate,"연도","합계출산율","합계출산율 가공.csv")
convert_data_populationratio(address_rawdata_under14,"연도","인구비율","0-14세 인구비율 가공.csv")
convert_data_populationratio(address_rawdata_15_64,"연도","인구비율","15-64세 인구비율 가공.csv")
convert_data_populationratio(address_rawdata_over65, "연도", "인구비율","65세이상 인구비율 가공.csv")

# 가공데이터 가져오기

address_processeddata_fertilityrate = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/합계출산율 가공.csv'
excel_processeddata_fertilityrate = excel(address_processeddata_fertilityrate)
processed_data_fertilityrate = excel_processeddata_fertilityrate.get_data()

address_processeddata_under14 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/0-14세 인구비율 가공.csv'
excel_processeddata_under14 = excel(address_processeddata_under14)
processed_data_under14 = excel_processeddata_under14.get_data()

address_processeddata_15_64 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/15-64세 인구비율 가공.csv'
excel_processeddata_15_64 = excel(address_processeddata_15_64)
processed_data_15_64 = excel_processeddata_15_64.get_data()

address_processeddata_over65 = 'C:/Users/yshar/Desktop/Term_project/시군구 데이터/65세이상 인구비율 가공.csv'
excel_processeddata_over65 = excel(address_processeddata_over65)
processed_data_over65 = excel_processeddata_over65.get_data()



#출산율 그래프그리기

list_year_fertility = processed_data_fertilityrate["연도"].to_list()
list_fertility_rate = processed_data_fertilityrate["합계출산율"].to_list()
plt.plot(list_year_fertility,list_fertility_rate)
plt.ylim((0,2))
plt.xlabel('year')
plt.ylabel('Tatal fertility rate')
plt.title('Changes of Total fertility rate(1993-2021)')
plt.show()


# 연령별 인구비율 그래프 그리기


list_year = processed_data_under14["연도"].to_list()
list_under_14 = processed_data_under14["인구비율"].to_list()
list_15_64 = processed_data_15_64["인구비율"].to_list()
list_over_65 = processed_data_over65["인구비율"].to_list()

plt.plot(list_year,list_under_14,'r',label = 'under 14')
plt.plot(list_year, list_15_64, 'g',label = '15-64')
plt.plot(list_year, list_over_65, 'b',label = 'over 65')
plt.legend(loc = 'upper right')
plt.xlabel('year')
plt.ylabel('population ratio(%)')
plt.title('changes of population ratio(2000-2021) ')
plt.ylim((0,100))
plt.show()

# 노령화 지수 그래프
# 노령화 지수  = 고령인구(65세이상)/유소년인구(0-14세)*100

list_Aging_index = []
for i in range(0,22):
    num = list_over_65[i]/list_under_14[i]*100
    list_Aging_index.append(num)
plt.plot(list_year, list_Aging_index)
plt.xlabel('year')
plt.ylabel('Aging index')
plt.title('Changes of Aging index(2000-2021)')
plt.ylim(0,150)
plt.show()