#!/usr/bin/env python3
import pandas as pd

def suicide_fractions():
    data = pd.read_csv('src/who_suicide_statistics.csv')
    data['mean'] = data['suicides_no'] / data['population']
    result = data.groupby('country')['mean'].mean()

    return result
    
def suicide_weather():
    # [0] since read_html returns a list of DFs
    avg_temp = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col='Country')[0]
    suicide = suicide_fractions()
    avg_temp = avg_temp.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    merge_df = pd.merge(avg_temp, suicide, left_on='Country', right_on='country')
    result = avg_temp.corr(suicide, method='spearman')

    return (len(suicide), len(avg_temp), len(merge_df), result)

def main():
    suicide_rows, temperature_rows, common_rows, spearman_correlation = suicide_weather()
    print(f'Suicide DataFrame has {suicide_rows} rows')
    print(f'Temperature DataFrame has {temperature_rows} rows')
    print(f'Common DataFrame has {common_rows} rows')
    print(f'Spearman correlation: {spearman_correlation}')

if __name__ == "__main__":
    main()