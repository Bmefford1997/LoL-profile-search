import pandas as pd
import requests
from bs4 import BeautifulSoup

#submit summoner name
x = input('What summoner are you looking for? ' )



#request the url and convert it into a beautifulsoup object
#if this url cannot find the attribute 'GameItemWrap' for a summoner, it will fail.
#because all usernames technically exist on this website, it only fails through attributes
try:
    page = requests.get('https://na.op.gg/summoner/userName='+x)
    soup = BeautifulSoup(page.content, 'html.parser')
    layout = soup.find(id='SummonerLayoutContent')
    recent_game = layout.find_all(class_ = 'GameItemWrap')



#let the user know a summoner was not found
except:
    print('Summoner was not found')


#for each item in recent_game with the tag 'GameItemWrap' that we scraped earlier
#find each attribute from the html classes listed below and scrape it
#parse out the text from the html tags and excess ('\n\r\t":) using the get_text() method and strip() method for clear output
#output the clean text into a list 
else: 
    champions = [item.find(class_= 'ChampionName').get_text().strip('\n\r\t": ') for item in recent_game]
    kda = [item.find(class_= 'Kill').get_text()+'/'+item.find(class_= 'Death').get_text()+'/'
    +item.find(class_= 'Assist').get_text() for item in recent_game]
    cs_per_minute = [item.find(class_= 'CS').get_text().strip('\n\r\t": ') for item in recent_game]
    outcome = [item.find(class_= 'GameResult').get_text().strip('\n\r\t": ') for item in recent_game]
    game_time = [item.find(class_= 'GameLength').get_text().strip('\n\r\t": ') for item in recent_game]



#pandas module pd for creating a table for data anaytics
#the first parameter is the column heading
#the second parameter is the the data from the lists  
    recent_stats = pd.DataFrame(
        {
            'Champion': champions,
            'Outcome': outcome,
            'CS (cs/m)': cs_per_minute,
            'KDA': kda,
            'Time': game_time
        })

    print (recent_stats)
    recent_stats.to_csv(x+ '_stats.csv')
    input('Press [ENTER] key to continue' )
#tests
#def test1()
    #print (recent_game[0].find(class_ = 'ChampionName').get_text())
    # print (recent_game[0].find(class_ = 'Kill').get_text() + 
    # '/' + recent_game[0].find(class_ = 'Death').get_text() 
    # + '/' + recent_game[0].find(class_ = 'Assist').get_text() + '  '
    # + recent_game[0].find(class_ = 'CKRate').get_text().strip())
    #print (recent_game[0].find(class_ = 'CS').get_text())
    #print(recent_game[0].find(class_ = 'GameResult').get_text().strip())
    #print (recent_game[0].find(class_ = 'GameLength').get_text())


#tests
#def test2()
    # print(champions)
    # print(kda)
    # print(cs_per_minute)
    # print(outcome)
    # print(game_time)