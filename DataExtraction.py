import pandas as pd
import re
import numpy as np
dest_file = r"D:\Personal\Techgig\result.csv"
with open(r'D:\Personal\Techgig\Predicting Housing Prices\Housing Prices data\bob.txt') as f:
    data = f.read()
house_data = data.split("\n\n\n")[:-1]
with open(dest_file, 'a+') as f:
    for h_data in house_data:
    #    house_ids=re.findall(r'House ID :.*',h_data)[0].split(':')[1].strip()
        house_ids= re.match(r'House ID :.*',h_data).group(0).split(':')[1].strip()
        built_date,date_priced= re.findall(r'Date Built.*(?:AM|PM|am|pm)',h_data)[0].split(':',1)[1].strip().split(" and Date Priced :  ")
        dock_dist = [cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else None for cap_dis in re.findall(r'Dock is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
        #re.findall(r'Dock is .[0-9]{0,5}\.[0-9]{1,6}',h_data)[0].split('is')[1].strip()
        cap_dist=[cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else None for cap_dis in re.findall(r'Capital is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        royal_market_dist=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Royal Market is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        guarding_tower = [str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Guarding Tower is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        river=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'River is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        #knights_house=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Knight\'s house is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        house_location=[str(cap_dis.split(":")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Location of the house is : .*',h_data)]
#        num_bedrooms = [str(cap_dis.split(" ")[0].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'\d.* bedrooms',h_data)]
#        num_dining_room =[str(cap_dis.split(" ")[0].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'\d.* dining rooms',h_data)]
#        #Distance from Knight's house is 
#        knights_house_dist=[cap_dis.split("is")[2].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Distance from Knight\'s house is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
#        
                
#       
#        results = ','.join((house_ids,built_date,date_priced,dock_dist[0],cap_dist[0],royal_market_dist[0],guarding_tower[0],
#                            river,house_location[0],num_bedrooms[0],knights_house_dist[0]))
        results = ','.join((house_ids,built_date,date_priced,dock_dist[0],cap_dist[0]))
#    
#    
        f.write(results)
