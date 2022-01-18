from bs4 import BeautifulSoup
import requests
import datetime
dt_now = datetime.datetime.now()

headers = {'Authorization': 'Bearer '} 
# <Request method> Authorization 에서 Bearer 쓰고 한칸 띄고 access token(발급받은 키) 입력

page_num = 1


four_price = []
five = []
print("4 ~ 5000원대 제품 크롤링 중")
print()

while True:
    code = requests.get(
        "https://www.coupang.com/np/search?q=%EC%98%A4%EA%B7%B8%EB%9E%98%EB%86%80%EB%9D%BC%ED%8C%9D&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}".format(
            page_num), headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(code.text, "html.parser")
    product = soup.select("div.descriptions-inner > div.name")
    price = soup.select("em.sale > .price-value")
    full = soup.select("li.search-product")

    
    if len(product) == 0:  # 끝 페이지까지 크롤링 모두 완료했다면?
        break

        
    for i in range(len(full)):
        link = full[i].select_one("a").attrs["href"]

        if len(price[i].text) == 5:
            if (price[i].text)[0:1] == "4":
                four_price.append(product[i].string + " " + price[i].text + "원")
                four_price.append("https://www.coupang.com/" + link)

            if (price[i].text)[0:1] == "5":
                five.append(product[i].string +  " " + price[i].text + "원")

    page_num += 1

    

print("4 ~ 5000원대 제품 크롤링 완료")



num=0
content = ""
for i in four_price :
    num+=1
    if num % 2 == 0:
        content+=(i+"\n" + "\n") # url을 기준으로 한칸 더 띄우기
    else :
        content += (i + "\n")

        

five_content = ""
for a in five :
    five_content += ( a + "\n" + "\n")

    
    
#four = "" # 4000원대의 가격이 없을 경우 5000원대 가격이 어떻게 나오는지 test 용도

if four_price : # 5000원대 test 할 경우 four이라고 수정해야함
    data = {"message": "\n"
                "{}월 {}일 현재 오그래놀라팝 가격입니다.".format(dt_now.month, dt_now.day) +
        "\n \n"
        
        "현재 <4️⃣000원>대 상품입니다."
        "\n"
        "\n" +
        "🔽 \n \n {} \n".format(content)

            }
else :
    data = {"message": "\n"
                       "{}월 {}일 현재 오그래놀라팝 가격입니다.".format(dt_now.month, dt_now.day) +
                       "\n \n"

                       "현재 <4️⃣000원>대 상품이 존재 하지 않습니다."
        
                       "\n \n = = = = = = = = = = = = = = = = = = \n \n"

                       "현재 <5️⃣000원>대 상품입니다."
                       "\n"
                       "\n" +

                       "🔽 \n \n {}".format(five_content)
            }

# Request parameters에서 Parameter name의 message 라는 곳에 내가 보내고 싶은 메세지를 넣으면 된다.

requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
# url 주소로 post를 요청


