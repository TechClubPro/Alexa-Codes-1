
"""
Dictionaries
"""

import speech_recognition as speech
import pyttsx3
import pygame

import time

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',200)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('Sportexa')

#Display the Background Image
bg=pygame.image.load("images/bg1.jpg")
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()


#Dictionaries for Books Alexa
harry={"cricket":["Spch","Cricket is the most popular game in the world"],
       "football":["Img","football"],
       "badminton":["ImgSpch","It is one of the games in olympics","badminton"],
       "tennis":["consoleText","Tennis can be played on different types of grounds"]}

geronimo={"basketball":["Spch","Each team of basketball has 5 players"],
       "hockey":["ImgSpch","Hockey is a national sport of India","hockey"],
       "swimming":["ImgSpch","Swimming is a fun sport","swimming"]}       
       
nancy={"squash":["Spch","It's an interesting game"],
       "athletics":["Spch","It's a game of agility and flexibility"],
       "stop":["stop"],
       "exit":["exit","Thanks for Interaction"]}       

#Use this as a default dictionary       
blank={"exit":["exit","Thanks for Interaction"]}


activate="none"
exitstatus="no"
state=blank

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 'c' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("C pressed")
                    
                    
        #If 'c' key is pressed
        if activate=='c':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg2.jpg").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            
            if "harry potter" in command:
                state=harry
                
            elif "geronimo stilton" in command:
                state=geronimo
            elif "nancy" in command:
                state=nancy
                
            elif "geronimo stilton" in command:
                state=geronimo
                
            if state != blank:    
                #Change the background image to Listening Image
                listenImg=pygame.image.load("images/bg2.jpg").convert_alpha()
                image1=pygame.transform.scale(listenImg, (900,600))
                screen.blit(image1,(0,0))
                pygame.display.update()
                
                #Start Listening the User Voice Input
                r=speech.Recognizer()
                
                with speech.Microphone() as source:
                        r.adjust_for_ambient_noise(source)
                        print("Speak:")
                        audio=r.listen(source)
                    #Convert Voice Commands to Text
                command=r.recognize_google(audio).lower()
                    
                print("You said: "+command)
            
            
            #Search each keyword in the dictionary one-by-one
            for keyword in state:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword
                    
                    #Speech Response Type
                    if state[keyword][0]=="Spch":
                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        state=blank
                        
                    #Console Text Response Type
                    elif state[keyword][0]=="consoleText":
                        print(state[keyword][1])
                        state=blank
                    
                    #Image Response type
                    elif state[keyword][0]=="Img":
                        image=pygame.image.load("images/"+state[keyword][1]+".jpg").convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                        
                        pygame.display.update()
                        time.sleep(15)
                        state=blank
                        
                    #Image & Speech Response type
                    elif state[keyword][0]=="ImgSpch":
                        #Showing Image
                        image=pygame.image.load("images/"+state[keyword][2]+".jpg").convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                      
                        pygame.display.update()
                        
                        #Saying Text
                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        state=blank
                                         
                     
                    elif state[keyword][0]=="exit":
                        engine.say(state[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/bg1.jpg").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                


