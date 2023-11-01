import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text,'html.parser')

#威力彩
data = sp.find('div',{'class':'contents_box02'})

#開獎期數
title = data.find('span','font_black15').text #取出期數<span>
print("最新一期大樂透開獎時間：",title)

#開獎號碼
nums = data.find_all('div',{"class":"ball_tx ball_green"}) #取出<div>
#print(nums)

#開獎順序
print("開出順序：", end=" ")
for i in range(0,6):
    print(nums[i].text, end=' ')#取出<div>的文字，取出前六個，指開出順序

print("\n小大順序：", end=" ")
#小大順序
for i in range(6,12):
    print(nums[i].text, end=' ')#取出<div>後六個，取出後六個，指小大順序

#特別號
spnum = data.find('div',{'class':'ball_red'}).text  #直接將<div>文字提出
print("\n  特別號：",spnum)