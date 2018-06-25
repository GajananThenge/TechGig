import pandas as pd
import re
import numpy as np

with open(r'D:\Personal\Techgig\Predicting Housing Prices\Housing Prices data\bob.txt') as f:
    data = f.read()
house_data = data.split("\n\n\n")[:-1]
for h_data in house_data:
#    house_ids=re.findall(r'House ID :.*',h_data)[0].split(':')[1].strip()
    house_ids= re.match(r'House ID :.*',h_data).group(0).split(':')[1].strip()
    #built_date= re.findall(r'Date Built : .*AM|PM$',h_data)[0].split(':',1)[1].strip()
    #date_priced = re.findall(r'Date Priced cal: .*AM|PM$',h_data)[0].split(':',1)[1].strip()
    built_date = [cap_dis.split("and",1)[1].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Date Built : .*AM|PM$',h_data)]
    date_priced = [cap_dis.split(":",1)[1].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Date Priced : .*AM|PM$',h_data)]
    dock_dist = [cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Dock is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    #re.findall(r'Dock is .[0-9]{0,5}\.[0-9]{1,6}',h_data)[0].split('is')[1].strip()
    cap_dist=[cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Capital is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    royal_market_dist=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Royal Market is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    guarding_tower = royal_market_dist=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Guarding Tower is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    river=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'River is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    knights_house=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Knight\'s house is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
    
    print("{},{},{},{},{},{},{},{}".format(house_ids,built_date,
          date_priced,dock_dist,cap_dist,
          royal_market_dist,guarding_tower,river,knights_house))
    break



from ast import literal_eval
def main():
    value = input()
    print("This is a type of ",type(literal_eval(value) ))
 
main() 
