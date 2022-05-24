from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import os

print ("This bot was made and written by @eric.nyc_ via Instagram")
print ("GitHub Link: https://github.com/EricProgrammerBLM")
print ('')
sleep(2)
#Important Information

#RefreshRate = int(input('How many seconds before the bot refresh its Instagram Timeline: '))

CalmDown = [1, 3, 2, 5, 3, 2] #Slowing Down the Refresh Rate
LongPause = [35, 45, 60, 25, 32, 47, 15, 10, 73, 30, 22, 27, 12, 49, 37]
xpath_of_comment_section = "//div/form[*[local-name()='textarea']]" #section[2] is used for new post
CaptionXpath = "//div[3]/div[1]/div/div[1]/div/span[2][*[local-name()='span']]"
Post = "//div/form/button[contains(text(),'Post')]"

#What the bot looks for on the first post on its timeline so it knows if to comment or not
RecentPost = ['1 SECONDS AGO', '2 SECONDS AGO', '3 SECONDS AGO', '4 SECONDS AGO', '5 SECONDS AGO', '6 SECONDS AGO', '7 SECONDS AGO', '8 SECONDS AGO', '9 SECONDS AGO']

#---------------------- Below Connects to a Spread Sheet that Has a List of Comments---------
Login = ['its empty'] #Login credentials go here. Username Should go first then Password
RandomComments = []

#Cleaning the list from any None values.
RandomComments = list(filter(None, RandomComments))
Login = list(filter(None, Login))





#------------------------------------------Browser Opens and Starts Below

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)

driver.find_element_by_name('username').send_keys(Login[0])
driver.find_element_by_name('password').send_keys(Login[1])
Login = "//button[@type='submit']" 
sleep(2)
driver.find_element_by_xpath(Login).submit() #Logs In
sleep(1)
#Logs into Instagram
print ('Logged In')

#------------------------ATTENTION

NotNow = "//button[contains(text(),'Not Now')]"
driver.find_element_by_xpath(NotNow).click()
#Clicks Pop Up
print ('Close Pop Up')

#Its weird but the pop up opens once, only after this page.
#If ever a problem delete one, or have the first click be
#directed to your Instagram Profiles timeline

NotNow = "//button[contains(text(),'Not Now')]"
try:
    driver.find_element_by_xpath(NotNow).click()
    #Clicks Pop Up
    print ('Close Pop Up')
except NoSuchElementException:
    print ('No Pop Up was Found.')

#-----------------------------------

def LeavingComments(comment, time): #a different try error must add, try except and default i think im not sure
    try:
        LeaveComment = driver.find_element_by_xpath(xpath_of_comment_section)
        LeaveComment.click()
        LeaveComment2 = driver.find_element_by_tag_name('textarea')
        LeaveComment2.send_keys(comment)
        Post2 = driver.find_element_by_xpath(Post).click()
        print ('Comment Left: ', comment)
        print ('Pausing for: ', time)
        sleep(CalmDown[0])
    except NoSuchElementException:
        print ('Comments Were Turned Off; Search for a better Post')
        driver.refresh()
        #Temporary solution, it will ignore the error and leave a comment on another post

#------------------------------------------------------------


#NewPost = []




while True:
    print ('Refreshing Timeline')
    driver.refresh()

    #This randomizes the list of comments extracted from the spread shit, from up above
    random.shuffle(CalmDown)
    random.shuffle(RandomComments)
    random.shuffle(LongPause)

    #Driver can sense the time of the first 4 post on the timeline, but cant comment on the first 3; can possibly fix later

    
    try: #Incase connection is ever lost while running the bot
        PostCaption = driver.find_element_by_xpath(CaptionXpath) #Xpath of the caption of a post
    except NoSuchElementException:
        print ('Error Webpage; Refreshing')
        driver.refresh()
        #Xpath of the caption of a post
        
    Time = driver.find_element_by_xpath("//div[3]/div[2]/a[*[local-name()='time']]") #Xpath to the time the Instagram Post was made
    #May need to add a try statement here for NoSuchElementException, if (New Post) becomes an issue
    print ('Last Post Was: ', Time.text)

    if (Time.text) in RecentPost:
        LeavingComments(RandomComments[0], LongPause[0])
        sleep(LongPause[0])
    else:
        sleep(CalmDown[0])

        #add multiple if statements with postcaption.text have rapper name
        #                         do LeaveComment(rappername[random number])









