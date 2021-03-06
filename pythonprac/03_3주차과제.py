import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 순위 / 곡 제목 / 가수를 스크래핑
'''
공통부문 찾기
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > 
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
'''
# print(soup.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)'))

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    rank = tr.select_one('td.number')
    title = tr.select_one('td.info > a.title.ellipsis')
    artist = tr.select_one('td.info > a.artist.ellipsis')
    print(rank.text.split()[0], title.text.split()[0], artist.text.split()[0])
