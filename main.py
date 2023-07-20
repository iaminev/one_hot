import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print('initial list: ')
print(lst)
print('\n')

data = pd.DataFrame({'whoAmI':lst})
print('initial dataframe: ')
print(data)
print('\n')

df_humans_robots_get_dummies = pd.get_dummies(data['whoAmI'])
print('one-hot dataframe when using get_dummies: ')
print(df_humans_robots_get_dummies)
print('\n')

my_dict = {}
my_dict['human'] = []
my_dict['robot'] = []

for val in lst:
    my_dict['human'].append(True if val == 'human' else False)
    my_dict['robot'].append(True if val == 'robot' else False)

df_humans_robots = pd.DataFrame({'human': my_dict['human'], 'robot': my_dict['robot']}, columns = ['human','robot'])
print('one-hot dataframe when no get_dummies used: ')
print(df_humans_robots)
print('\n')

print(f'dataframes are equal: {df_humans_robots_get_dummies.equals(df_humans_robots)}')
