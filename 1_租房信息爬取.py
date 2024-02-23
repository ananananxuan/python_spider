from lxml import html
import requests

cookies = {
    'lianjia_uuid': 'fcf4e7e7-34a5-4ce0-bac0-83adc03b7dfc',
    'select_city': '110000',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218dcf05c2f017a2-0c7fbcdcbc88d9-26001851-1296000-18dcf05c2f123b0%22%2C%22%24device_id%22%3A%2218dcf05c2f017a2-0c7fbcdcbc88d9-26001851-1296000-18dcf05c2f123b0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D',
    'GUARANTEE_POPUP_SHOW': 'true',
    'GUARANTEE_BANNER_SHOW': 'true',
    'lianjia_ssid': '8c9a8a86-96bd-4966-9ba1-8a645802a97d',
    'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiNDQxYjBiNmY3MWY0MGY5ZjQyNjA3NDU5ODVmZWIyZWQ1NWZiYWJiMzkzZDAzMjYwZmQzMGZiOGVkNTg0ZmU1MTk0MmQwMzhhMzA2NDc2MDE1N2RlODI1OGFkMjQwNTQ2ZmI4ZWEwZDg5MWI3NWQ2NzQ3NjQ5YzQwMDQzYzRhZTNiZjhhNmJiZmMzMmJlYmE2MDJhYjM0ODg2NGI2ZTczNzFlYmYxNzZlM2MyNTNhOTAzNmRkMjI5NjNhZTg4ODJlYzMzMTUxY2VjZDE5ZmJmMzI1MzZkNjA0Njg1YWRiNGU4MGNlZDM3YzE5ZjExYzIwMzVhYWRkNWU3NWYwMzQzMVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwMDA5ZjcyMlwifSIsInIiOiJodHRwczovL2JqLnp1LmtlLmNvbS96dWZhbmcvI2NvbnRlbnRMaXN0Iiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lianjia_uuid=fcf4e7e7-34a5-4ce0-bac0-83adc03b7dfc; select_city=110000; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218dcf05c2f017a2-0c7fbcdcbc88d9-26001851-1296000-18dcf05c2f123b0%22%2C%22%24device_id%22%3A%2218dcf05c2f017a2-0c7fbcdcbc88d9-26001851-1296000-18dcf05c2f123b0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; GUARANTEE_POPUP_SHOW=true; GUARANTEE_BANNER_SHOW=true; lianjia_ssid=8c9a8a86-96bd-4966-9ba1-8a645802a97d; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNDQxYjBiNmY3MWY0MGY5ZjQyNjA3NDU5ODVmZWIyZWQ1NWZiYWJiMzkzZDAzMjYwZmQzMGZiOGVkNTg0ZmU1MTk0MmQwMzhhMzA2NDc2MDE1N2RlODI1OGFkMjQwNTQ2ZmI4ZWEwZDg5MWI3NWQ2NzQ3NjQ5YzQwMDQzYzRhZTNiZjhhNmJiZmMzMmJlYmE2MDJhYjM0ODg2NGI2ZTczNzFlYmYxNzZlM2MyNTNhOTAzNmRkMjI5NjNhZTg4ODJlYzMzMTUxY2VjZDE5ZmJmMzI1MzZkNjA0Njg1YWRiNGU4MGNlZDM3YzE5ZjExYzIwMzVhYWRkNWU3NWYwMzQzMVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwMDA5ZjcyMlwifSIsInIiOiJodHRwczovL2JqLnp1LmtlLmNvbS96dWZhbmcvI2NvbnRlbnRMaXN0Iiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
    'Referer': 'https://bj.zu.ke.com/zufang/pg4/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

for page in range(1,5):
  if page == 1 :
    url = 'https://bj.zu.ke.com/zufang'
  else:
    url = f'https://bj.zu.ke.com/zufang/pg{page}/#contentList'
  
  response = requests.get(url, cookies=cookies, headers=headers)

  # 使用lxml解析HTML
  tree = html.fromstring(response.content)

  titles = tree.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div/div/p[2]/a[3]/text()')

  print(titles)
