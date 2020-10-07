---


---

<h1 id="välkommen-till-rasa-väderbot">Välkommen till Rasa Väderbot</h1>
<p>Målet med detta projekt är att bygga en grundläggande Rasa-chatbot med <a href="https://www.google.com/url?sa=i&amp;url=https://core.telegram.org/bots&amp;psig=AOvVaw3JPxvhfMshvjbt2PM5Kylx&amp;ust=1602112973247000&amp;source=images&amp;cd=vfe&amp;ved=0CAIQjRxqFwoTCPDd-IqOoewCFQAAAAAdAAAAABAD">Telegram-integration</a>.  Där användaren kan begära ett specifikt stadsväder och hämta platstemperaturen från ett specifikt API.</p>
<h1 id="förutsättningar">Förutsättningar</h1>
<p>Skapa <a href="https://home.openweathermap.org/">Weather API</a>:<br>
.🤷‍  <a href="https://www.python.org/downloads/">python</a> är ett krav<br>
.  Installera  <a href="https://visualstudio.microsoft.com/downloads/">Microsoft Builds tools visual C++14.0</a>:</p>
<h2 id="installera--rasa">1- Installera  <a href="https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide">RASA</a></h2>
<pre><code>  ✔  Skapa en ny miljö:
        conda create -m "din skappad miljö name" python==3.6.9
  ✔ Aktivera den skapade miljö:
        conda activate "miljö name"
  ✔ 
</code></pre>
<h2 id="skapa-din-bot-och-http-api-med-telegram">2- Skapa din bot och HTTP API med Telegram</h2>
<pre><code>        ✔   I din Telegram App/webplats, sök efter "BotFather"
        ✔   "/start"     (Att starta BotFather)  och sen välj: "/newbot"  som alternativ
        ✔   Skapa din "new bot"   - Recommendera att det måste vara unik name
        ✔   Efter kan man skapa användaren name till den ny bot. (exempelvis: TetrisBot eller tetris_bot)
        ✔   Om godkänt kan HTTP API token generas - 
        ✔
</code></pre>
<h2 id="implementera-rasa">3- Implementera RASA</h2>
<pre><code>    ✔ skapa en ny mapp för ditt chatbotprojekt.
    ✔  Skapa en ny miljö from Vs-kod, Pycharm or Anaconda prompt:
        conda create -m "din skappad miljö name" python==3.6.9
    ✔ Aktivera den skapade miljö:
        conda activate "miljö name"
    ✔ kör kommandot   "pip install spacy" för installation av spacy-biblioteket
    ✔  Rasa init 
</code></pre>
<h2 id="nu-kan-man-träna-modellen-med-kommanden-">4- Nu kan man träna modellen med kommanden :</h2>
<pre><code>         ✔ rasa train    (träna din model)
         ✔  rasa x  (Öppna http://localhost:5002/interactive)
         ✔ rasa run  (Kör endast rasa servern)
         ✔ rasa run actions   (action endpoint server)
</code></pre>
<h2 id="rekommendera-att-installera-ngrock-för-localhost-testning.">5- Rekommendera att installera <a href="https://ngrok.com/docs">ngrock</a> för localhost testning.</h2>
<pre><code> Syftet med ngdrock är att konvertera min lokala till offentliga webbadress.
 Användare kommandsline: For linux ( ./rgrock http 5005) , Windows (ngrodck http 5005) 
 Exampelvis port 5005 som är  Rasa servern kan naturligtvis variera. Standarden portaddress:80.🤷‍
</code></pre>
<p><img alt="enter image description here"></p>

