import pandas as pd
data = {'Poets':['Blok', 'Shakespeare', 'Dante', 'Akhmatova'],
        'Birth':[1880, 1564, 1265, 1889],
        'Nationality':['russian', 'british', 'italian', 'russian']
        }
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
df.head(3)