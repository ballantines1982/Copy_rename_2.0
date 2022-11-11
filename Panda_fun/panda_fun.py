import pandas as pd
import datetime
#from dateutil import parser
import re
import locale

locale.setlocale(locale.LC_ALL, 'Swedish_Sweden.1252')

date_str = "25:e Maj 2022"

def char_search(string): 
    if re.search(':e', string):
        string = re.sub(':e', '', string)
        return string
    return string

try:
    date_obj = datetime.datetime.strptime(char_search(date_str), '%d %b %Y').date()
    print(date_obj)
except Exception as e:
    print(e)

#print(type(date_obj))

#date_pars = parser.parse(date_str).date()

#print(date_pars)
#print(type(date_pars))

   
def test(x):
    x['Percent'] = x['Antal (p)'] / x['Antal (p)'].sum() * 100
    return x


    
def EkoSum():
    
    
    
    bil_bills = ['Ingo', 'Avbet. Bilen', 'LF Motor (1:e)', 'Trängselskatt']
    hyra_bills = ['Hyra (30:e)', 'Hyra']
    sheets = 0
    
    peter_drop_list = ["Spara Bilen", "Inkomst", "Gem. Räk. TOT"]
    sara_drop_list = ["Spara Helgnöje", "Spara Familjen", "-", "Inkomst", "Gem. Räk. TOT"]

    col_names = ['Peter', 'Antal (p)', "Sara", "Antal (s)"]
    
    budget = pd.ExcelFile("Privat_budget_210921 - kopia.xlsx")
    
    Peterbudget_sheets = {}
    concatDf = {}

    try:         
        with pd.ExcelFile("Privat_budget_210921 - kopia.xlsx") as budget:
            for sheet in budget.sheet_names[1:-3]:
                if "25e" in sheet:
                    sheets+=1
                    Peterbudget_sheets[sheet] = pd.read_excel(budget, sheet, usecols="A:D", nrows=19)
                    Peterbudget_sheets[sheet].columns = col_names
                    #Peterbudget_sheets[sheet]['Per'] = Peterbudget_sheets[sheet]['Antal (p)'] / Peterbudget_sheets[sheet]['Antal (p)'].sum() * 100
                    concatDf = pd.concat(Peterbudget_sheets, ignore_index=True)
                    concatDf.insert(0, 'Date', budget.sheet_names)

                    peter = concatDf[[col_names[0], col_names[1]]].groupby(col_names[0]).agg(['count', 'sum', 'min', 'max', 'mean'])
                    peter[['Antal (p)']].transform(lambda x: (x - 1000))
                    sara = concatDf[[col_names[2], col_names[3]]].groupby(col_names[2]).agg(['count', 'sum', 'min', 'max', 'mean'])
                    income = concatDf[concatDf['Peter'] == 'Inkomst']
                    cost = concatDf[concatDf['Peter'] == 'Gem. Räk. TOT']
                    income1 = income[[col_names[0], col_names[1]]].groupby(col_names[0]).agg(['count', 'sum', 'min', 'max', 'mean'])
                    income2 = income[[col_names[2], col_names[3]]].groupby(col_names[2]).agg(['count', 'sum', 'min', 'max', 'mean'])
                    
                    
                    
                    # income['Sum'] = income.loc[:,'Antal (p)'] + income.loc[:,'Antal (s)']
                    # cost['Sum'] = cost.loc[:,'Antal (p)'] + cost.loc[:,'Antal (s)']
        print(concatDf)
        # peter1 = peter.drop(peter_drop_list)
        # print("\nÖversikt Peter")
        # print("-"*70)
        # print(peter1)
    
        # sara1 = sara.drop(sara_drop_list)
        # print("\nÖversikt Sara")
        # print("-"*70)
        # print(sara1)
        
        # peter1 = peter.drop(peter_drop_list)
        # print("\nSUM Räkningar Peter")
        # print("-"*35)
        # print(peter1.sum())
        # print("\nSUM Inkomst Peter")
        # print("-"*35)
        # print(income1.sum())
        
        # sara1 = sara.drop(sara_drop_list)
        # print("\nSUM Räkningar Sara")
        # print("-"*35)
        # print(sara1.sum())
        # print("\nSUM Inkomst Sara")
        # print("-"*35)
        # print(income2.sum())
    
            
            
        # with pd.ExcelWriter('Privat_budget_210921 - 3.xlsx') as writer:
        #     writer.book = openpyxl.load_workbook('Privat_budget_210921 - kopia.xlsx')
        #     df.to_excel(writer, sheet_name=person)
        #     print("New sheet created")
    except Exception as e:
        print(e)

    # df2 = concatDf.loc[concatDf['Bill_Peter'].isin(bil_bills)]
    # bilDf = df2[['Bill_Peter', 'Amount']].groupby('Bill_Peter').agg(['count', 'sum', 'min', 'max', 'mean'])
            

EkoSum()






#Kontrollera vilka sheets som finns och ersätt dem
#Summera inkomsterna
    #Addera en rad med skillnaden mellan Sara & Peter

#Kalkulera en jämnförelse med förra årets siffror.
#Jämnför r12 snittet med sista månaden 
#Kalkulera skillnaden på inkomstsnittet och utgiftsnittet totalt för båda
