# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:39:05 2018

@author: hp-pc
"""

import pandas as pd
import re
import numpy as np
import os

source_path = r'I:\TechGig\Horse Price Prediction\Housing Prices'

full_path_list = [os.path.join(root,f_name) for root, dir_names, file_names in os.walk(source_path) for f_name in file_names  if f_name.split('.',1)[1]=='txt']
dest_file = r"I:\TechGig\result.csv"


for file in full_path_list:
    with open(file) as f:
        data = f.read()
        house_data = data.split("\n\n\n")[:-1]
        with open(dest_file, 'a+') as f:
            for h_data in house_data:
                builder = file.rsplit(os.path.sep, 1)[1].split('.',1)[0]
                house_ids= re.match(r'House ID :.*',h_data).group(0).split(':')[1].strip()
                built_date,date_priced= re.findall(r'Date Built.*(?:AM|PM|am|pm)',h_data)[0].split(':',1)[1].strip().split(" and Date Priced :  ")
                dock_dist = [cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else None for cap_dis in re.findall(r'Dock is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                cap_dist=[cap_dis.split("is")[1].strip() if len(cap_dis)!=0 else None for cap_dis in re.findall(r'Capital is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                royal_market_dist=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Royal Market is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                guarding_tower = [str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Guarding Tower is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                river=[str(cap_dis.split("is")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'River is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                house_location=[str(cap_dis.split(":")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Location of the house is : .*',h_data)]
                num_bedrooms = [str(cap_dis.split(" ")[0].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'\d.* bedrooms',h_data)]
                num_dining_room =[str(cap_dis.split(" ")[0].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'\d.* dining rooms',h_data)]
                
                #Distance from Knight's house is 
                knights_house_dist=[cap_dis.split("is")[2].strip() if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Distance from Knight\'s house is .[0-9]{0,5}\.[0-9]{1,6}',h_data)]
                
                sorcerer =[cap_dis for cap_dis in re.findall(r'sorcerer.*',h_data)]
                
                in_front = [str(cap_dis.split(" in the front")[0].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'.* in the front',h_data)]
                kings_blessings =  [str(cap_dis.split("with ")[1].strip()) if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'King blessed the house with \d+',h_data)]
                holy_tree = [cap_dis if len(cap_dis)!=0 else '' for cap_dis in re.findall(r'Holy tree .*',h_data)]
        
                house_id = house_ids if len(house_ids)>0 else str(np.NaN)
                built_date=  built_date if len(built_date)>0 else str(np.NaN)
                date_priced  =  date_priced[0] if len(date_priced)>0 else str(np.NaN)
                dock_dist = dock_dist[0] if len(dock_dist)>0 else str(np.NaN)
                cap_dist=  cap_dist[0] if len(cap_dist)>0 else str(np.NaN)
                royal_market_dist=  royal_market_dist[0] if len(royal_market_dist)>0 else str(np.NaN)        
                guarding_tower = guarding_tower[0] if len(guarding_tower)>0 else str(np.NaN)
                river= river[0] if len(river)>0 else str(np.NaN)
                house_location =house_location[0]  if len(house_location)>0 else str(np.NaN)
                num_bedrooms= num_bedrooms[0] if len(num_bedrooms)>0 else str(np.NaN)
                num_dining_room = num_dining_room[0] if len(num_dining_room)>0 else str(np.NaN)
                knights_house_dist= knights_house_dist[0]  if len(knights_house_dist)>0 else str(np.NaN)
                in_front = in_front[0] if len(in_front)>0 else str(np.NaN)
                kings_blessings = kings_blessings[0]  if len(kings_blessings)>0 else str(np.NaN)
                holy_tree = holy_tree[0] if len(holy_tree)>0 else str(np.NaN)
                
                results = ','.join((house_ids,built_date,date_priced,dock_dist,cap_dist,royal_market_dist,guarding_tower,
                                    river,house_location,num_bedrooms,knights_house_dist,in_front,kings_blessings,holy_tree,builder))
                f.write(results+'\n')
