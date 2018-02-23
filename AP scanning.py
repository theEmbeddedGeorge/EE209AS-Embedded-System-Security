import os
import operator
import csv
import time
import sys

monitor_card = 'wlan1'
scan_s = '10'
file_name = 'ap_info'
chosen_bssid = ''
file_path = os.system('pwd')

# save 5-second scanning result to a csv file
print('scan for nearby AP...')
#os.system('rm ' + file_name + '*')
os.system('timeout ' + scan_s + ' airodump-ng -w ' + file_name +
                                ' --output-format csv -I 5 --ignore-negative-one '
                                + monitor_card)

reader = csv.reader(open(file_name + '-01.csv'))
list_reader = list(reader)

# only extract AP info, dont need device info
filtered_r = [line for line in list_reader if (len(line) == len(list_reader[2]))]

# sort according to the pwr rating of APs
sortedlist = sorted(filtered_r, key=operator.itemgetter(8))

# filter out ap with incorrect info, fix format
for line in sortedlist:
    strip_item = line[8].replace(" ", '')
    if int(strip_item) < -1:
        # record the bssid of the AP with the strongest signal
        chosen_bssid = line[0].replace(" ", '')
        print(strip_item)
        print(chosen_bssid)
        break

