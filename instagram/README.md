### 2021.01 인스타그램 자동 좋아요 코드
<img src = https://user-images.githubusercontent.com/74857364/103893132-1b1b8300-5130-11eb-959a-56685e0661e2.gif width = "70%">

<br>

```python
# 좋아요 누르기
while True:

    like = browser.find_element_by_css_selector("button.wpO6b span > svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")

    if value == "좋아요" :
        like.click()  # 좋아요 클릭
        time.sleep(random.randint(2, 5) + random.random())

        next.click()
        time.sleep(random.randint(2, 5) + random.random())

    elif value == "좋아요 취소" :
        next.click()
        time.sleep(random.randint(2, 5) + random.random())
```

* 컴퓨터 환경에 따라 기다리는 시간을 줄이거나 길게 조절한다.   

* a 노트북에서는 2 ~ 5초 사이로 해도 화면 로딩에 문제가 없었는데           
b 노트북에서는 가끔 로딩이 느려서 5초를 잡아먹는 경우가 있었다.      

* 짧은 시간 동안 계속 좋아요를 반복하니 인스타가 봇으로 인식하기 때문에 5초 이상을 권장한다. 
<br>
</br>

---

### 2021.01 자동 좋아요 + 팔로우 코드 작업
![instagram 팔로우](https://user-images.githubusercontent.com/74857364/160289688-d7c553d5-87a3-4faf-8ca3-e6a862f9d083.png)

<br>

사진 및 여행과 관련된 컨셉으로 프로필을 꾸몄기 때문에           
해당 코드를 실행했던 대상은 주로 사진 및 여행과 관련된 사람들 위주로 진행이 되었다.       
(ex. #사진계정, #사진스타그램)                   
                               
`hash_tag = input("해시태그 입력 >> ")` 해당 코드를 사용해 해시 태그를 입력하면             
해당 해시태그를 입력한 사람들을 대상으로 코드를 실행했다.   

더 자세한 내용 > [log 보기](https://github.com/haedal-project/python/blob/main/instagram/README.md#log)


<br>

#### 1차 수정 : 좋아요 코드에서 추가
***if***문과 ***elif***을 추가해서 text가 팔로우면 팔로우 버튼 클릭 아니면 pass

처음에는 좋아요/팔로우 속도를 4 ~ 8초로 잡고 실행하였으나 인스타그램에서 이를 봇으로 확인하는 경우가 많아
10 ~ 15초 사이로 수정했다.

```python
 if value == "좋아요":
        like.click()
        time.sleep(random.randint(10, 15) + random.random())

    elif value == "좋아요 취소":
        time.sleep(random.randint(10, 15) + random.random())

    if follow.text == "팔로우":
        follow.click()
        time.sleep(random.randint(10, 15) + random.random())
        
    elif follow.text == "팔로잉":
        pass
        
    next.click()
    time.sleep(random.randint(10, 15) + random.random())
```

<br><br>
</br>

#### 2차 수정 : css 선택자 오류
특정 사진에서 follow 버튼 css 선택자 뒷부분이 다르게 떠서 부모 css 선택자를 넣고 끝 부분 선택자를 지웠다.

`follow = browser.find_element_by_css_selector("button.sqdOP.yWX7d.y3zKF")`   
                        
→ `follow = browser.find_element_by_css_selector("div.bY2yH > button.sqdOP.yWX7d")`   


<br><br>
</br>

---

### 2021.02 예외 처리
#### 3차 수정 : 사진로드가 되지 않아서 아예 안뜨는 문제
<img src = https://user-images.githubusercontent.com/74857364/150069545-a6ba45d2-b936-4338-808a-56cdfb78c272.png width="50%">


사진이 안뜨는 경우 다음 사진으로 넘어가는 ***try~except*** 구문 사용

<br><br>
</br>


#### 4차 수정 : 경고 메세지가 뜨는 문제
<img src = https://user-images.githubusercontent.com/74857364/150069616-09454168-7f14-4eb5-b0a5-dccc9219a85b.png width="30%">

3차 수정 코드에서 작성한 ***try~except*** 구문의 ***except***에 ***try~except*** 구문을 추가

```python
try:
except:
    try: # 사진로드가 되지 않아서 에러가 생기는 경우 다음 사진 클릭
    except: #instagran에서 보내는 메세지가 뜨는 경우
```

<br><br>
</br>


#### 5차 수정 : 제자리에서 맴도는 문제

자동 좋아요 + 팔로우 반복을 `while True`로 계속 해왔으나 잦은 좋아요와 팔로우는 인스타에서 막는다.

정확한 수치는 모르겠으나 대략 100번 이상 좋아요 및 팔로우를 진행할 경우 제재를 받는 것 같아 

`for d in range(80):` 으로 변경해서 사용했다.

```python
for d in range(80):
    # 생략
    
    if value == "좋아요":
        like.click()
        time.sleep(random.randint(10, 15) + random.random())

    elif value == "좋아요 취소":
        time.sleep(random.randint(10, 15) + random.random())

    # 생략
```

<br>

경고메세지가 뜨고 취소를 누른 후 다시 팔로우를 시도하는데 다시 경고메세지가 뜨는 경우 제자리에서 계속 맴돌게 된다.

<img src = https://user-images.githubusercontent.com/74857364/104103799-6e840180-52e7-11eb-9bae-8931c70e44f1.gif width="50%">

<br>

→ 마지막으로 팔로우와 좋아요를 했던 부분부터 시작하기 위해 경고 창이 뜨는 사진의 링크를 메모장에 저장한 후,            
`link = browser.current_url`                       

                          
저장했던 링크를 통해 마지막으로 좋아요 & 팔로우 한 부분부터 시작하게 하는 코드 작성       
```python
if browser.current_url == 메모장에 저장한 파일 변수:  
    time.sleep(4)
    break
```    

<br>
</br>

---

### 2021.03 언팔관리 프로그램 작업 및 예외 처리
#### 1차 수정
크롤링 한 db를 엑셀에 저장 

```python
# 엑셀 파일 생성
if not os.path.exists("./인스타_크롤링.xlsx"):
    openpyxl.Workbook().save("./인스타_크롤링.xlsx")

book = openpyxl.load_workbook("./인스타_크롤링.xlsx")

if "Sheet" in book.sheetnames:
    book.remove(book["Sheet"])
sheet = book.create_sheet()
now = datetime.datetime.now()
sheet.title = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
sheet.column_dimensions["B"].width = 40
sheet.column_dimensions["c"].width = 40
```

<br>

단점 : 엑셀에 저장 후 직접 중복 아닌 것 들을 찾아서 언팔을 관리

<br><br>
</br>

#### 2차 수정 (메모장 저장)
```python
f = open("file.txt", "w") # 팔로워 아이디 저장
ff = open("file1.txt", "w") # 팔로잉 아이디 저장
```
<br>

+) 저장된 메모장을 불러와서 언팔하는 코드를 따로 작성

```python
if __name__ == '__main__':
    # file 불러오기
    NewList = fileopen('file.txt')

    # file1 불러오기
    NewList1 = fileopen('file1.txt')

    # file1(팔로잉)에는 포함되고 file(팔로워)에는 포함되지 않은 아이디 출력  
    note = list(set(NewList1) - set(NewList))
    print(note)
    
    
    # 개수
    c=len(note)
    print(c , "개")
```

<br>

❓ 굳이 메모장에 저장해서 사용을 해야할까? 에 관한 고민

<br><br>
</br>

#### 3차 수정 (메모장 활용 x)
- 메모장을 활용하지 않고 프로그램 자체 내에서 저장, 중복을 제거하고 남은 아이디를 바로 언팔하는 하나의 프로그램으로 만듦
```python
a = []
b = []
```
<br>

##### +) 예외처리
- 로봇이 아니다 라는 타일을 클릭하는 메세지가 뜨는 경우가 발생 → 브라우저 창 그대로 띄움
- 크롤링이 잘 되지 못했을 경우 방지 → 팔로워와 팔로잉 수 출력 후 진행 여부 묻기       
           
+) 기존에 팔로우 및 팔로잉 취소 10 ~ 15초로 진행하였으나 15초까지 기다리지 않아도 실행이 잘 되어서 천천히 시간을 줄여가고 있다.            
```python
print("팔로워 수 :", len(b))
print("팔로잉 수 :", len(a))

aset = set(a) # 3번째
bset = set(b) # 2번째
note = aset-bset # 중복제거
print(note)

print()
print("팔로잉을 취소할 아이디의 개수는 " + str(len(note)) + "개 입니다.")
print()
time.sleep(random.randint(10, 12) + random.random())

ask= input("프로그램을 실행시키겠습니까? : ").lower()

if ask == 'y':
    for i in note:
    # 이하 생략
```

<br><br>
</br>

#### 4차 수정 (title css 변경)
변경 전
```python
title = browser.find_elements_by_css_selector("a.FPmhX.notranslate._0imsa")
```
<br>

변경 후
```python
title = browser.find_elements_by_css_selector("span.Jv7Aj.mArmR.MqpiF")
```

<br>

---

## 특징
- 인스타 자동 좋아요 및 팔로우                  
다른 사람의 게시글에 직접 반응(좋아요+팔로우) 해주지 않아도 내 게시글에 대한 반응을 얻을 수 있습니다.


- 언팔 관리             
나를 언팔로 한 사람들을 계속 팔로우를 해주기 싫을 때, 그 아이디를 일일히 찾으면서 비교하는 것이 시간을 꽤 쏟아야 하고               
팔로워와 팔로잉 수가 많으면 찾기 어려운데 프로그램만 실행시켜주면 알아서 취소해주므로 관리가 편리합니다.              

<br>
<br>

## log
인스타 자동화 강의를 배움으로써 이 기능을 활용하여 실제로 제가 사용하고 싶은 욕구가 생겼습니다.          
그래서 좋아요와 팔로우 기능을 만들게 되었고 계정을 새로 생성하면서                     
0부터 시작하여 목표치인 팔로워 수 1,000명 넘기기 달성도 해보게 되었습니다.                   
                    
그리고 팔로워 수와 팔로잉 수의 차이가 생김에 따라 언팔 관리 로직 작성의 필요성이 느껴져 이러한 기능을 추가하게 되었습니다.          

<br>

초반에 `좋아요` / `좋아요+팔로우` / `팔로우` 3개로 나눠서 테스트를 진행 하였습니다.          
`좋아요+팔로우` > `팔로우` > `좋아요` 순으로 반응이 좋았으나            
`좋아요+팔로우`와 `팔로우` 코드에는 큰 차이가 없었습니다.                         

다만 `좋아요+팔로우` 코드로 진행할 경우 제 계정의 사진에 좋아요를 받을 확률만 높아지는 것이고            
저는 좋아요보다는 팔로워 수에 더 집중을 하고 있었기에         
최근에는 더 많은 팔로워 수를 늘리기 위해서 `좋아요+팔로우` 대신 `팔로우`만 하는 코드로 진행을 하게 되었습니다.           

또 제 추측으로 이 전에 인스타에서 제재를 많이 받아왔는데 좋아요와 팔로우를 하나의 계정에 같이 하게 된다면        
2가지의 활동을 하는 것이고 팔로우만 진행하였을 때는 2개의 계정에 팔로우를 진행해야         
2가지의 활동을 하는 것이기 때문에 팔로우만 실행하는 코드로 진행을 하게 되었습니다. 


