### 2021.01 인스타그램 자동 좋아요 코드
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

<br>
</br>
<br>
</br>

### 2021.01 자동 좋아요 + 팔로우 코드 작업

#### 1차 수정 : 좋아요 코드에서 추가
if문과 elif을 추가해서 text가 팔로우면 팔로우 버튼 클릭
아니면 pass

<br>

#### 2차 수정 : css 선택자 오류
특정 사진에서 follow 버튼 css 선택자 뒷부분이 다르게 떠서 부모 css 선택자를 넣고 끝 부분 선택자를 지웠다.

`follow = browser.find_element_by_css_selector("button.sqdOP.yWX7d.y3zKF")`   
                        
→ `follow = browser.find_element_by_css_selector("div.bY2yH > button.sqdOP.yWX7d")`   


<br>
</br>
<br>
</br>

### 2021.02 예외 처리
#### 3차 수정 : 사진로드가 되지 않아서 아예 안뜨는 문제
사진이 안뜨는 경우 다음 사진으로 넘어가는 ***try~except*** 구문 사용

<br>

#### 4차 수정 : 경고 메세지가 뜨는 문제
3차 수정 코드에서 작성한 try~except 구문의 except에 try~except 구문을 추가

```python
try:
except:
    try: # 사진로드가 되지 않아서 에러가 생기는 경우 다음 사진 클릭
    except: #instagran에서 보내는 메세지가 뜨는 경우
```

<br>

#### 5차 수정 : 제자리에서 맴도는 문제
자동 좋아요 + 팔로우 반복을 `while True`로 계속 해오다가 `for d in range(80):` 으로 변경해서 사용

경고메세지가 뜨고 취소를 누른 후 다시 팔로우를 시도하는데 다시 경고메세지가 뜨는 경우 제자리에서 계속 맴돌게 된다.

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
<br>
</br>

### 2021.03 언팔관리 프로그램 작업 및 예외 처리
#### 1차 수정
팔로워 아이디 크롤링 후 팔로잉 아이디 크롤링 하여 엑셀 각각의 시트에 저장
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

<br>
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

<br>
</br>

#### 3차 수정 (메모장 활용 x)
메모장을 활용하지 않고 프로그램 자체 내에서 저장해 중복을 제거하고 남은 아이디를 바로 언팔하는 하나의 프로그램으로 만듦
     
```python
a = []
b = []
```
<br>

##### +) 예외처리
이 전에 작성한 코드를 실행하면서 확인하던 도중에 "로봇이 아니다" 라는 타일을 클릭하는 메세지가 떠서                        
계정이 차단당하는 것을 막을 수 있었는데 이러한 부분을 확인하지 못하고 꺼버리면         
차단 당할 수 있어서 브라우저 창은 그대로 띄우고 진행
                  
또한 크롤링이 잘 되지 못했을 경우를 방지하기 위해서 팔로워와 팔로잉 크롤링 수를 출력했고,     
팔로우 취소를 해야하는 횟수를 출력시킨 다음 이대로 진행할 것인지 여부를 묻는 코드를 작성         
           
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

