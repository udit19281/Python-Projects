from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



class insta:
    def __init__(self,name,ps):
        self.name=name 
        self.ps=ps
        self.driver='C:\\chromedriver'    
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])      #update Chrome driver path
        self.bro=webdriver.Chrome(self.driver, options=options)
        self.bro.get("https://instagram.com")
        sleep(5)
        seluser="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
        selpass="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
        sellogin="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"
        try:
            self.bro.find_element("xpath",seluser).send_keys(name)
            self.bro.find_element("xpath",selpass).send_keys(ps)
            sleep(1)
            self.bro.find_element("xpath",sellogin).click()
            sleep(5)
            #uncomment if 2 factor is used
            input("Press enter after code")
            # self.bro.find_element("xpath","/html/body/div[1]/section/main/div/div/div/div/button").click()
            
        except Exception as e:
            exit(0)
        
    def username(self, scroll_box):
        sleep(1)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            ht = self.bro.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""",scroll_box)
            sleep(3)
        links = scroll_box.find_elements(By.TAG_NAME,"a")
        names = [name.text for name in links if name.text != '']
        # self.bro.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()
        
        return names 

    def followers(self):
        
        # self.bro.get("https://www.instagram.com/"+self.name+"/")
        self.bro.get(f"https://www.instagram.com/{self.name}/followers/")
        sleep(7)
        # self.bro.find_element("xpath","/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        foll=[]
        while True:
            try:
                scroll_box = self.bro.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
                foll=self.username(scroll_box)
                break
            except Exception as e:
                print(e)
                break
                sleep(2)
                pass    
        
        return foll

    def following(self):
        self.bro.get(f"https://www.instagram.com/{self.name}/following/")
        sleep(7)
        # self.bro.find_element("xpath","/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        f=[]
        while True:
            try:
                scroll_box = self.bro.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
                f=self.username(scroll_box)
                break
            except Exception as e:
                print(e)
                break
                sleep(2)
                pass
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
    following=bot.following()
    print(following)
    followers=bot.followers()
    print(followers)
    
    notfollowing=[u for u in following if u not in followers]

    print("\n\tpeople not following: " + str(len(notfollowing)))
    print(notfollowing)

    print ("\n\tfollowing: " + str(len(following)))
    print (following)

    print("\n\tfollowers: " + str(len(followers)))
    print(followers)

#code by udit19281










