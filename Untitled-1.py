from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver=webdriver.Chrome("C:\Program Files (x86)\SeleniumFile\chromedriver.exe")
driver.get("https://politrip.com/account/sign-up")



class PythonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\SeleniumFile\chromedriver.exe")
        self.driver.get("https://politrip.com/account/sign-up")
    
    def test_1(self):
        camp=driver.find_element_by_id("first-name")
        camp.send_keys("robert")    #//valoarea acmpului Fisrt_name
        valoare_camp=camp.get_attribute("value")
        x=0
        if (len(valoare_camp)>0):
            for character in valoare_camp:  #verificare daca esxista un numar in camp
                if character.isdigit():
                    x=1
                    break
            if (x==1):
                assert False
            else:
                assert True
        else:   
            assert False

    
    def test_2(self):
        camp_last=driver.find_element_by_id("last-name")
        camp_last.send_keys("doroftea")    #//valoarea acmpului Last_Name
        valoare_camp_last=camp_last.get_attribute("value")
        x=0
        if (len(valoare_camp_last)>0):
            for character in valoare_camp_last:  #verificare daca esxista un numar in camp
                if character.isdigit():
                    x=1
                    break
            if (x==1):
                assert False
            else:
                assert True
        else:   
            assert False
    
    def test_3(self):
        email=driver.find_element_by_id("email")
        email.send_keys("rober@doroftea")    #//valoarea acmpului Email
        valoare=email.get_attribute("value")
        if (len(valoare)>0):
            if("@"in valoare and valoare[0] != "@"):  #//Verificarea cerintelor campului Email
                assert True     
            else:
                assert False    

        else:
            assert False
        
    def test_4(self):
        camp=driver.find_element_by_id("sign-up-password-input")
        camp.send_keys("RobertD1")    #//valoarea acmpului PAssword
        valoare_camp=camp.get_attribute("value")
        x=0  #Presupunem ca nu esxista numere, iar in eventualitatea in care acestea exista x isi va schimba valoarea
        y=0  #Presupunem ca nu esxista L=litere mari, iar in eventualitatea in care acestea exista x isi va schimba valoarea
        z=0  #Presupunem ca nu esxista litere mici, iar in eventualitatea in care acestea exista x isi va schimba valoarea
        if (len(valoare_camp)>7):
            for character in valoare_camp:  #verificare daca esxista un numar in camp
                if character.isdigit():
                    x=1
                    break
            if (x==0):
                assert False
            else:
                for mare in valoare_camp:  #varificarea de litera mare in camp
                    if mare.isupper():
                        y=1
                        break
            if (y==0):
                assert False        
            else:
                for mic in valoare_camp:
                    if mic.islower():
                        z=1
                        break
            if(z==0):
                assert False
            else: 
                assert True           
        else:   
            assert False
    
    def test_5(self):
        camp_parola=driver.find_element_by_id("sign-up-password-input")   #//valoarea acmpului PAssword
        valoare_camp=camp_parola.get_attribute("value")
        camp_re_parola=driver.find_element_by_id("sign-up-confirm-password-input")
        camp_re_parola.send_keys("RobertD1")    #//valoarea acmpului Password_re
        valoare_re_camp=camp_re_parola.get_attribute("value")
        if(valoare_camp==valoare_re_camp):
            assert True
        else:
            assert False


    def inchidere(self):
        self.driver.close()  
    

unittest.main()