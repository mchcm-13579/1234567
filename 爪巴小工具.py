import requests
import os
from tkinter import *
from bs4 import BeautifulSoup

def save_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def scrape_url():
    url = url_entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    html_content = str(soup.prettify())
    file_name = file_name_entry.get()+".html"
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    file_path = os.path.join("downloads", file_name)
    save_file(html_content, file_path)

root = Tk()
root.title('爬虫爬的好 牢饭吃到饱')
root.geometry('450x250')



url_label = Label(root, text='网页URL:')
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

file_name_label = Label(root, text='文件命名为:')
file_name_label.grid(row=1, column=0, padx=10, pady=5)

file_name_entry = Entry(root, width=20)
file_name_entry.grid(row=1, column=1, padx=10, pady=5)

download_button = Button(root, text='点我爬取并下载.html文件', command=scrape_url)
download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
