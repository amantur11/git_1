
# import requests
# from bs4 import BeautifulSoup as BS
# import csv


# url = 'https://www.kivano.kg/mobilnye-telefony.'

# def get_html(url):
#     reponse = requests.get(url)
#     return reponse.text
    
    
# def get_soup(html):
#     soup = BS(html, 'lxml')
#     return soup

# def get_laptops(soup):
#         phones = soup.find_all('div',class_='item product_listbox oh')
#         # print(phones)

#         for laptop in phones:
#             try:
#                 title = laptop.find('div', class_='listbox_title oh').text.strip()
#                 print(title)
#             except AttributeError:
#                 title = 'Телефон'
            
#             try:
#                 price = laptop.find('div',class_='listbox_price text-center').text.strip()
#                 # price = laptop.find('strong')
#                 print(price)
#             except AttributeError:
#                 price ='0'
#             try:
#                 image = laptop.find_all('div', class_='listbox_img pull-left').text.strip()
#                 print(image)
#             except AttributeError:
#                 print('Только под заказ')


#             write_csv({
#                 'title':title,
#                 'price':price,
#                 'image':image,
#                 })
        

# def write_csv(data):
#     with open('phones.csv','a') as file:
#         names = ['title','price','image']
#         write = csv.DictWriter(file, delimiter=',',fieldnames=names)
#         write.writerow(data)


# url = 'https://www.kivano.kg/mobilnye-telefony'
# html =get_html(url)
# soup = get_soup(html)
# get_laptops(soup)
# main()


# import requests
# from bs4 import BeautifulSoup as BS
# import csv


# def get_html(url):
#     response =requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BS(html,'lxlm')
#     return soup

# def get_data(soup):
#     names = soup.find('div',class_='header-submenu').text.split()
#     print(names)




# url = 'https://www.mashina.kg/'
# html =get_html(url)
# soup = get_soup(html)
# get_data(soup)


import csv
import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
    response = requests.get(url)
    return response.text

def to_csv(data):
    with open('sredniy_pars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='*')
        writer.writerow((data['name'],data['photo'],data['price']))



def get_total_pages(html):
    soup = BS(html, 'lxml')
    pages_ul= soup.find('div',class_="pager-wrap").find('ul', class_="pagination pagination-sm")
    pages_last = pages_ul.find_all('li')[-1]
    total_p = pages_last.find('a').get('href').split('=')[-1]
    return int(total_p)
    

def get_page_data(html):
    soup = BS(html, 'lxml')
    product_list = soup.find('div',class_="list-view")
    products = product_list.find_all('div', class_="item product_listbox oh")
    for product in products:
        try:
            name = product.find('div',class_="listbox_title oh").find('a').text
        except:
            name = ''
        try:
            photo = 'https://www.kivano.kg'+product.find('div',class_="listbox_img pull-left").find('img').get('src')
        except:
            photo = ''
        try:
            price = product.find('div',class_="listbox_price text-center").find('strong').text
        except:
            price = ''

        
        data = {'name':name,'photo':photo,'price':price}
        to_csv(data)
    



def main():
    cars_url = 'https://www.kivano.kg/mobilnye-telefony'
    pages = '?page='
    total_pages = get_total_pages(get_html(cars_url))
    for page in range(1,total_pages+1):
        url_page = cars_url + pages + str(page)
        html = get_html(url_page)
        get_page_data(html)


main()