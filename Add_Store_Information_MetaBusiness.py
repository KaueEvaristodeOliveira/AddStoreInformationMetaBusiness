#!/usr/bin/env python
# coding: utf-8

# In[89]:


#PREENCHER FORMULÁRIO DE LOJAS
import pyautogui 
import time
time.sleep(1)


#Add Store
pyautogui.click(x=440, y=251)

#Next
pyautogui.click(x=1213, y=845)

#ADD Manually
pyautogui.click(x=834, y=341)

#Next
pyautogui.click(x=1240, y=836)

#ID
pyautogui.press('tab', 3)
pyautogui.write('163')

#Location description
pyautogui.press('tab', 2)
pyautogui.write('Jao Bettega')

#Street Adress
pyautogui.press('tab')
pyautogui.write('Jão Bettega, 89')

#City/Town
pyautogui.press('tab')
pyautogui.write('Curitiba')
time.sleep(1)
pyautogui.press('enter', 2)

#Zip Code
pyautogui.press('tab', 2)
pyautogui.write('8888888')

#Phone Number
pyautogui.press('tab')
pyautogui.write('+5541991446209')

#Wi-Fi
pyautogui.press('tab', 2)
pyautogui.write('The Office')

#Opening Hours
pyautogui.press('tab', 12)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('tab')

#Monday
pyautogui.click(x=701, y=594)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
    
#Tuesday
pyautogui.click(x=701, y=655)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
    
#Wednesday
pyautogui.click(x=700, y=692)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
        
#Thurday
pyautogui.click(x=693, y=741)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
    
#Friday
pyautogui.click(x=698, y=786)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
    
#Saturday 
pyautogui.click(x=698, y=843)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
    
#Sunday
pyautogui.click(x=703, y=881)
pyautogui.press('tab') #Opening time
pyautogui.write('7') 
pyautogui.press('tab')
pyautogui.write('30')

pyautogui.press('tab') #Closing time
pyautogui.write('19') 
pyautogui.press('tab')
pyautogui.write('30')
        
#Pickup Options
pyautogui.press('tab', 2)
pyautogui.click(x=707, y=618)

#Price Range
pyautogui.click(x=737, y=711)
time.sleep(1)
pyautogui.press('down', 3)
time.sleep(1)
pyautogui.press('enter')

#Temporary Service Changes
pyautogui.press('tab')#Operating as Usual
pyautogui.click(x=773, y=858)


# In[ ]:


#BOT INSERINDO AS INFORMAÇÕES PARA PREENCHER O FORMULÁRIO
import pyautogui 
pyautogui.pause (1)


# In[86]:


import pyautogui 
pyautogui.position()

