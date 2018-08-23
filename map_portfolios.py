import re
import json
import io
import csv
import sys
from pprint import pprint
from collections import defaultdict
import time
import datetime
import numpy as np
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
import pprint

  
class Mapper:

  def __init__(self, password):

    self.password = password
    self.get_buildings_by_officer()



  def get_buildings_by_officer(self):

    d_ref = defaultdict(list)
    d_cnt = defaultdict(int)
    path = "data/multi_story_head_officers.csv"
    reader = csv.reader(open(path, encoding="utf8", errors='ignore'))
    for row in reader:
      d_ref[row[6] + "_" + row[8]].append(row[1])
      d_cnt[row[6] + "_" + row[8]] += 1

    # for k in d_ref.keys():
    #   if(len(d_ref[k]) > 10):
    #     print(d_ref[k])
    sorted_d = sorted(d_cnt.items(), key=lambda x: x[1], reverse=True)
    for i in range(0,101):
      print(sorted_d[i])







      # d[row["FirstName"] + "_" + row["LastName"]].append(row["RegistrationID"])

      # cnx = mysql.connector.connect(user='root', password=self.password,
      #                               host='127.0.0.1',
      #                               database='multi_story_nyc')

      # cursor = cnx.cursor()

      # print("Beginning processing... ")

      # # Grab all rows with Type = "HeadOfficer"
      # query = 'SELECT * FROM `registered_contacts` as contacts JOIN `registered_buildings` as buildings ON contacts.`RegistrationID` = buildings.`RegistrationID` where contacts.`Type` = "HeadOfficer";'  
      # cursor.execute(query)
      # result_set = cursor.fetchall()

      # for result in result_set:
      #   print(result)



  def test(self):

    d = defaultdict(int)
    csv_read = "output_data/inwood_evictions_cleaned.csv"
    reader = csv.reader(open(csv_read, 'rU'), delimiter=",", dialect=csv.excel_tab)

    for row in reader:
      d[row[14]] += 1

    s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

    csv_write = "output_data/evictions_by_bin.csv"
    with open(csv_write,'w') as out:
      writer=csv.writer(out)
      for k,v in s:
        row = [k,v]
        writer.writerow(row)




if __name__ == '__main__':
  password = "lylla318"
  p = Mapper(password)






