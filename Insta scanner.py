from selenium import webdriver
from time import sleep

class insta:
    def __init__(self,name,ps):
        self.name=name 
        self.ps=ps
        self.driver='C:\\chromedriver'            #update Chrome driver path
        self.bro=webdriver.Chrome(self.driver)
        self.bro.get("https://instagram.com")
        sleep(2)
        seluser="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
        selpass="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
        sellogin="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button/div"
        try:
            self.bro.find_element_by_xpath(seluser).send_keys(name)
            self.bro.find_element_by_xpath(selpass).send_keys(ps)
            sleep(1)
            self.bro.find_element_by_xpath(sellogin).click()
            sleep(4)
            #uncomment if 2 factor is used
            #input("press enter after code")
            self.bro.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            self.bro.get("https://www.instagram.com/"+name+"/")
        except Exception as e:
            print(e)
            exit(0)
        
    def username(self):
        sleep(1)
        scroll_box = self.bro.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(3)
            ht = self.bro.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.bro.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg").click()
        return names 

    def followers(self):
        sleep(2)
        self.bro.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        foll=self.username()
        return foll
    def following(self):
        sleep(3)
        self.bro.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        f=self.username()
        return f
    def dnfoll(self):
        followe=self.followers()
        foling=self.following()
        notf=[u for u in foling if u not in followe]
        return notf

if __name__ == "__main__":
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    bot=insta(username,password)          

    followers=bot.followers()
    following=bot.following()
    notfollowing=[u for u in following if u not in followers]

    print("\n\tpeople not following: " + str(len(notfollowing)))
    print(notfollowing)

    print ("\n\tfollowing: " + str(len(following)))
    print (following)

    print("\n\tfollowers: " + str(len(followers)))
    print(followers)

#code by udit19281










