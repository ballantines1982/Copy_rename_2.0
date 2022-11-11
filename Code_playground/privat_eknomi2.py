import pandas as pd
import numpy as np


budget = pd.read_excel(r'C:\Users\svard\OneDrive\Skrivbord\Privat_budget_210921.xlsx', sheet_name=11)

print(budget.info())