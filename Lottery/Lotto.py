import requests
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


minDrwNo = 1        #Start
maxDrwNo = 919      #End
drwtNo1 = []        
drwtNo2 = []        
drwtNo3 = []        
drwtNo4 = []        
drwtNo5 = []        
drwtNo6 = []        
bnusNo = []         
drwNoDate = []      

# Get winning number from first to last
for i in tqdm(range(minDrwNo, maxDrwNo + 1, 1)):

    # get the winnig numbers
    req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)

    req_lotto = requests.get(req_url)

    lottoNo = req_lotto.json()

    drwNoDate.append(lottoNo['drwNoDate'])  
    drwtNo1.append(lottoNo['drwtNo1'])      
    drwtNo2.append(lottoNo['drwtNo2'])      
    drwtNo3.append(lottoNo['drwtNo3'])      
    drwtNo4.append(lottoNo['drwtNo4'])      
    drwtNo5.append(lottoNo['drwtNo5'])      
    drwtNo6.append(lottoNo['drwtNo6'])      
    bnusNo.append(lottoNo['bnusNo'])   


h = np.hstack((drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6))

cnt = Counter(h)
#print Output
print(sorted(cnt.items(),key=lambda x:x[1], reverse=False))