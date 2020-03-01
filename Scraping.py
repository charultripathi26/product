from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from flask import Flask
from flask import request, jsonify
import json

app=Flask(__name__)
@app.route('/', methods=['POST'])

# def index():
# 	if request.method == 'GET':
# 		URL= 'https://www.amazon.in/Yardley-London-Morning-Perfume-50ml/dp/B07YLY3W7L/ref=asc_df_B07YLY3W7L/?tag=googleshopdes-21&linkCode=df0&hvadid=397081552310&hvpos=1o1&hvnetw=g&hvrand=5606536759617604886&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062136&hvtargid=pla-844148630094&psc=1&ext_vrnc=hi'
# 		uClient= uReq(URL)
# 		page_html= uClient.read()
# 		uClient.close()
# 		page_soup=soup(page_html, "html.parser")
# 		price=page_soup.find(id="priceblock_ourprice").get_text()
# 		return(price)
	
def index():
	task = {
		"id" : request.json['id']
	}
	#task.append(task)

	data = jsonify({'task': task}), 201
	print(task["id"])
	ID=task["id"]
	print(ID)
	URL= 'https://www.amazon.in/s?k='+ID
	print(URL)
	uClient= uReq(URL)
	page_html= uClient.read()
	uClient.close()
	page_soup=soup(page_html, "html.parser")
	price=page_soup.find("span",{"class":"a-price-whole"}).get_text()
	print(price)
	return jsonify(price), 200
	# return data


if __name__ =='__main__':
	app.run(host='192.168.42.189')

    
    
    
    
    


#filename="price.csv"
#f=open(filename,"w")
#headers="price"

#f.write(headers)


#html parsing




