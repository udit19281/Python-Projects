import os,re
import webbrowser as web,sys
try:
    import requests
    import bs4
except ImportError:
    os.system("pip install requests, bs4")
import requests
import bs4    

if __name__ == "__main__":
    if len(sys.argv)>1:
        query = sys.argv[1:]
        query=' '.join(query)
    else:
        query=input("Enter Query:")

    google="https://www.google.com/search?q="+query
    result=requests.get(google)
    result.raise_for_status()
    soup=bs4.BeautifulSoup(result.text,"html.parser")
    links=[]
    com=re.compile("&sa=.*&ved=.*")
    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        temp=(re.split(":(?=http)",link["href"].replace("/url?q=","")))[0]
        if com.search(temp)[0]!=None:
            final=re.sub(com.search(temp)[0],"",temp)
            links.append(final)
    mi=min(4,len(links))
    # print(links)
    web.open(google)
    for i in range(mi):
        print(links[i])
        web.open(links[i])
