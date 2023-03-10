import re


rules = '<url>https:\/\/([a-zA-Z0-9_\.]+)<\/url>'

stats_access_links = ["<url>https://xcd32112.smart_meter.com</url>",
                      "<url>https://tXh67.dia_meter.com</url>",
                      "<url>https://yT5495.smart_meter.com</url>",
                      "<url>https://ret323_TRu.crown.com</url>",
                      "<url>https://luwr3243.celcius.com</url>"]


for c in range(4):
    
   match = re.search(rules, stats_access_links[c])
  
   print(match)
   
   if match:
       
     print(match.group())
     
   else:
       
     print("Not found")
