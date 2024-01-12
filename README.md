# telegram-scraper-v2.0-ENG. Scraper and inviter telegram groups. (Telethon) 

![Watermark](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/bb1e06e4-83a5-4302-83b6-3d530fcaa14f)

# Updates
## v2.0
* __now .session files can be use for authorization. Place them to directorty!__
* __Added scraping user-ids.__
* __option on/off user-names and user-ids scraping. (in options)__
* __Converter phone numbers to .session__
  


## 1. Preparation to launch.
First thing, find out your API_ID and API_HASH tokens. Go to: https://my.telegram.org/apps and authorize. Choice __API Development Tools__

![12591615102022_5c20dcbcfbab07ab6c2df7e27444d5ac2afca569](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/75080769-1aa6-4cbc-ab75-cd0a1e04ec09)

In the next window, fill in App title and Short name. Choice desktop.

![gfbauf](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/963ca90a-b9f7-4f94-bc95-a87742742239)

Press Create Application, copy API_ID и API_HASH. 

__API_ID and API_HASH are suitable for any accounts. You can use API_ID and API_HASH a third party account__
## 2. Build project.
__Windows__
* Download python 3.12 https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
* __When installing, be sure to check the Add to PATH box__
  ![hgai](https://github.com/Keqy/telegram-parser-v1.0/assets/96333229/046ed050-5a00-4c94-8758-6de165e81ca3)
* Open cmd. ```cd``` to scraper directory. For example: ```cd C:Users/Keqy/programs/repos/telegram-parser-v2.0```
* Create virtual environment ```py -m venv venv```, activate it ```.\venv\Scripts\Activate```
* Install telethon ```pip install telethon```

__Linux/MacOS__
* Open cmd, update packages. ```sudo apt update```
* Install python and git. ```sudo apt install python3 python3-pip git -y```
* Download repository. ```git clone https://github.com/Keqy/telegram-parser-v2.0/```
* ```cd``` to scraper directory.
* Create virtual environment ```py -m venv venv```, activate it ```.\venv\bin\Activate```


## 3. Usage.
![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/5c31cb79-87c5-4419-bcac-09da9142aea6)


In options enter your API_ID __(only numbers)__ and API_HASH __(numbers and letters)__ without spaces.

Here in points 3 and 4 you can on/off usernames and userids scraping option. By default, both will be scraped



### Converter
Converter place in options in point ```Add user-bot account```. Give the converter a phone number and enter the redeem code. In directory creates .session file for user-bot quick authorization. You also can place your .session files in program directory and use them.
![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/daabecfc-2d69-4fef-8c53-6f5333220e1a)


__Converter does not work if API_ID and API_HASH incorrect__
__for any new account __DOES NOT__ required API_ID and API_HASH__


Options are stored in ```options.txt``` in project directory.
For escape, press ```e```.
The main menu will open.

![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/328d848b-b6f9-4cb4-a8e6-f2168b5622a5)


### Scraping
In scraping window, select account that is in groups for scraping.

![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/109c23a4-e551-487b-9b3b-bef1666ff600)
![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/56eaf32d-97e4-4bce-adbb-990a6a19723b)


__Sometimes telethon-library errors may appear here. In this case, you need to restart the program__

Scraped usernames and user-ids will be located in project directory in ```usernames.txt``` and ```userids.txt```.

### Inviting
In inviting window, select account that is in groups for inviting. Then program ask you to enter the group name.
![image](https://github.com/Keqy/telegram-scraper-v2.0-ENG/assets/96333229/bf99d383-5ba1-447f-8297-75856d1c57fa)


__Write to me in telegram ```@DonMinionAmerimaChesburger```___
