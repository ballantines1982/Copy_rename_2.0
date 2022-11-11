import pandas as pd
import numpy as np


df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df2 = df.set_index(["A", "B"])

grouped = df2.groupby(level=df2.index.names.difference(["B"]))

def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'


grouped = df.groupby(get_letter_type, axis=1)


print(df)
print('Grouped by A')
print(grouped.sum())
