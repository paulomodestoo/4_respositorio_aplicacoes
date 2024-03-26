#%%
import requests
import bs4

url = 'https://www.google.com/search?q=%22%C3%A1guas+de+niter%C3%B3i%22&sca_esv=d34a127615f5f538&biw=2124&bih=1026&tbm=nws&sxsrf=ACQVn0-zR77gZpIV1wxdisvoR5hzNlqA5g%3A1711293166266&ei=7kIAZpDZD4LW1sQPlIaImAw&udm=&ved=0ahUKEwiQiKDql42FAxUCq5UCHRQDAsMQ4dUDCA0&uact=5&oq=%22%C3%A1guas+de+niter%C3%B3i%22&gs_lp=Egxnd3Mtd2l6LW5ld3MiFCLDoWd1YXMgZGUgbml0ZXLDs2kiMgUQABiABDIFEAAYgAQyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYigUYQ0iSHFCEC1irGXAAeACQAQCYAaIBoAGGA6oBAzAuM7gBA8gBAPgBAZgCA6ACkwOYAwCIBgGSBwMwLjOgB-8T&sclient=gws-wiz-news'

requisicao = requests.get(url)

pagina = bs4.BeautifulSoup(requisicao.text, "html.parser" )

# elemento "a" e a classe ""  -   class_='OSrXXb rbYSKb LfVVr'

lista_noticias = pagina.find_all("a")
for noticia in lista_noticias:
    if "BNeawe vvjwJb AP7Wnd" in str(noticia):
        print("============")
        print(str(noticia.find("h3")).split(">")[2].split("<")[0])
        print(str(noticia.get("href")).split("/url?q=")[1])
        print("")