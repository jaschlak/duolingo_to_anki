# Duolingo To Anki

    This project is meant to login to your Duolingo site, grab the words
    you have learned and push them to an anki deck. 
    
    It does require you install
    AnkiConnect Add-on in Anki which listens on a port for the api
    
    If you wish to sync to your phone you will have to get a AnkiWeb account
    in order to synchronize with your app. I think it is like 20 bucks on apple
    and free on android (See Documentation Below)
    
## Setup

1) `pip3 install -r requirements.txt`
2) copy the `input/example_conf.json` -> `input/conf.json`
3) fill in your duolingo login information in `input/conf.json`
4) Check Anki info in `input/conf.json`  
    a) Fill your deckname  
    b) Change desired tags  
    c) Check port number  
5) Install AnkiConnect Add-on:
    a) Open Anki.
    b) Go to Tools > Add-ons > Get Add-ons.
    c) Enter the code for AnkiConnect (2055492159) and install it.
    

Documentation:

[anki-connect repo/readme](https://git.foosoft.net/alex/anki-connect)  
[anki web](https://ankiweb.net/)  