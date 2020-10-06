# rasa_vaderbot
  Målet med detta projekt är att bygga en grundläggande Rasa-chatbot med Telegram-integration.
  Där användaren kan begära ett specifikt stadsväder och hämta platstemperaturen från ett specifikt API.

# Förutsättningar:
Skapa Weather API: https://home.openweathermap.org/
       .🤷‍  python
       .  Installera vid behov: https://visualstudio.microsoft.com/downloads/

TODO: projekt design todo here 🛺

## 1- Installera  RASA  https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide
      ✔  Skapa en ny miljö:
            conda create -m "din skappad miljö name" python==3.6.9
      ✔ Aktivera den skapade miljö:
            conda activate "miljö name"
      ✔ 
      
## 2- Skapa din bot och HTTP API med Telegram
            ✔   I din Telegram App/webplats, sök efter "BotFather"
            ✔   "/start"     (Att starta BotFather)  och sen välj: "/newbot"  som alternativ
            ✔   Skapa din "new bot"   - Recommendera att det måste vara unik name
            ✔   Efter kan man skapa användaren name till den ny bot. (exempelvis: TetrisBot eller tetris_bot)
            ✔   Om godkänt kan HTTP API token generas - 
            ✔

## 3- Implementera RASA
        ✔ skapa en ny mapp för ditt chatbotprojekt.
        ✔  Skapa en ny miljö from Vs-kod, Pycharm or Anaconda prompt:
            conda create -m "din skappad miljö name" python==3.6.9
        ✔ Aktivera den skapade miljö:
            conda activate "miljö name"
        ✔ kör kommandot   "pip install spacy" för installation av spacy-biblioteket
        ✔  Rasa init 

## 4- Nu kan man träna modellen med kommanden : 
             ✔ rasa train    (träna din model)
             ✔  rasa x  (Öppna http://localhost:5002/interactive)
             ✔ rasa run  (Kör endast rasa servern)
             ✔ rasa run actions   (action endpoint server)


## 5- Rekommendera att installera "ngrock" för localhost testning.  V.g see: "https://ngrok.com/docs"
     Syftet med ngdrock är att konvertera min lokala till offentliga webbadress.
     Användare kommandsline: For linux ( ./rgrock http 5005) , Windows (ngrodck http 5005) 
     Exampelvis port 5005 som är  Rasa servern kan naturligtvis variera. Standarden portaddress:80.🤷‍


🎭👂🧠
