# 쿠팡 최저가 상품 알림 봇(python) 
**4,000원대 상품이 있을 때**          

<img src = https://user-images.githubusercontent.com/74857364/160288775-4669e5e1-6aef-4124-aaf1-b4e2708c28af.png width="30%">

<br>

**4,000원대 상품이 없을 때**            

<img src = https://user-images.githubusercontent.com/74857364/160288777-32d5bbdc-df72-4570-8892-6f12360ba07b.png width="30%">

<br>

## 실행 과정
### 1. 복잡한 css 코드 정리        
`product = soup.select("div.name")` → `product = soup.select("div.descriptions-inner > div.name")`

[코드 보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L22)

<br> 
           
### 2. 특정 상품 크롤링 반복문 설정               
[코드 보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L17)

<br> 

### 3. 원하는 가격대 설정       
[코드 보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L34)

<br> 

### 4. Line API 사용으로 알림 봇 설정
```python
import requests
headers = {'Authorization': 'Bearer 발급 받은 키'} 
data = {"message": "Hi!"}
requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
```
[코드 보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L6)

<br> 

### 5. 자동화 설정 (작업 스케줄러)

<br> 

### 6. 출력 결과 형식 수정

#### 1차 수정 
- **변경 전** : 4,000원대와 5,000원대 함께 출력    
- **변경 후**              
4,000원대 상품이 있는 경우, 5,000원대 상품 출력X  → [코드 보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L69)        
**&** 4,000원대 상품이 없는 경우, 상품이 없다는 메세지 + 5,000원대 상품 출력 → [코드보기](https://github.com/haedal-project/python/blob/b282b3c66a8e3b9a59dd206eed5a015d7e83a484/bot/coupang.py#L67)   



<br> 

#### 2차 수정
- 메모장 활용하지 않고 가독성있게 출력 시키기    
[코드 보기](https://github.com/haedal-project/python/blob/6499f3c477d6c7d8b9cc963bfc77783ec2bb458f/bot/coupang.py#L50)

<br>

---

## 배경
특정 상품의 가격이 낮춰질 때가 일주일에 한 두번 정도로 나타남

사이트에 들어가서 매번 확인하기 번거로움 → 알림 봇을 만들자

<br>

## 특징 
- 상품을 사고 싶은데 현재 가격을 모르면 사이트에 검색해서 찾아야하는데 알아서 알려주므로 편리하게 사용 가능

- 작업 스케줄러를 이용해서 지정한 시간에 컴퓨터에서 자동으로 수행되게 할 수 있어 원하는 시간에 편리하게 확인 가능

<br>

### Tistory 구현 과정 링크 첨부
[https://lu-delight.tistory.com/171](https://lu-delight.tistory.com/171)

[https://lu-delight.tistory.com/172](https://lu-delight.tistory.com/172)

[https://lu-delight.tistory.com/173](https://lu-delight.tistory.com/173)

[https://lu-delight.tistory.com/174](https://lu-delight.tistory.com/174)

[https://lu-delight.tistory.com/184](https://lu-delight.tistory.com/184)

