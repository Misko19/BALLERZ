import pandas as pd
import json

# sheet_id = '1uj_RkwcraJZc0cJitcf9lvBJjnz-vveWdfiV8lgljC8'
sheet_id = '17o_Aic0fk-QoUmDTfngbouwefpIUs5HrMNFVWAqMpPA'
sheet_name = 'Ballerz%20Database'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

data = pd.read_csv(url)

l = [
    'ID',
    'Body',
    'Team',
    'Gender',
    'Accessory Group',
    'Accessory 1',
    'Accessory 2',
    'Accessory 3',
    'Jersey',
    'Hair',
    'Role',
    'Number',
    'Dunks',
    'Shooting',
    'Playmaking',
    'Defense',
    'Overall',
    'Image',
    'Pts',
    'Reb',
    'Ast',
    'Stl',
    'MVP?',
    'JSA Rarity Score',
    'JSA Rarity Rank'
]

data_clean = data[l].fillna('')
data_clean.head(3)
data_clean.to_json('ballerz_jsa_info.json', orient="records", indent=1)
