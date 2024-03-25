#%%
import requests
import bs4

url = 'https://www.google.com/search?q=%22%C3%A1guas+de+niter%C3%B3i%22&sca_esv=d34a127615f5f538&biw=2124&bih=1026&tbm=nws&sxsrf=ACQVn0-zR77gZpIV1wxdisvoR5hzNlqA5g%3A1711293166266&ei=7kIAZpDZD4LW1sQPlIaImAw&udm=&ved=0ahUKEwiQiKDql42FAxUCq5UCHRQDAsMQ4dUDCA0&uact=5&oq=%22%C3%A1guas+de+niter%C3%B3i%22&gs_lp=Egxnd3Mtd2l6LW5ld3MiFCLDoWd1YXMgZGUgbml0ZXLDs2kiMgUQABiABDIFEAAYgAQyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIKEAAYgAQYigUYQ0iSHFCEC1irGXAAeACQAQCYAaIBoAGGA6oBAzAuM7gBA8gBAPgBAZgCA6ACkwOYAwCIBgGSBwMwLjOgB-8T&sclient=gws-wiz-news'

requisicao = requests.get(url)

pagina = bs4.BeautifulSoup(requisicao.text, "html.parser" )

# elemento "a" e a classe ""  -    n0jPhd ynAwRc MBeuO nDgy9d

lista_noticias = pagina.find_all("h3", class_="zBAuLc l97dzf")

print(lista_noticias)