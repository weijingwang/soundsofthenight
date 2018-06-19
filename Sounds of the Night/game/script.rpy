#start program
define w = Character('{image=私.png} (watashi or me if you didnt alreay kow smh)') #return is end seal ends
define k = Character('{image=愛子狐ちゃん.png}~ (aiko kitsune chan~learnyourjapanes!stupidbaka!)')#\(>w<)/
define m = Character('{image=桃子樣.png} (Momoko Sama)')
label splashscreen:
    show intro1
    with fade
    $ renpy.pause(2)
    show intro2
    with fade
    $ renpy.pause(2.5)
    return

label start:
    stop music
    play music "night_time.mp3"#http://soundbible.com/951-Nightime.html
    scene bg scene1
    w "it was a really really kawaii day and i became tired and then it became night and suprise i got lost in wildlife preserve du oiseax!!!!???"
    w "but what nani NANI!!??? I hear somethi"
    w "rustile in grass desu huh"
    w "what the heck yes i am a edgy teen so i can say big boy word"
    w "no joke man what the f word im getin the chils"
    w "wait i hear not BFF {image=愛子狐ちゃん.png}~ ????"

$ kp = 0#kokoro points

menu :#tree branch number 1 but no matter

    "go CONAN KAwai sugoi kakiu INVESITIgation Skill!!!! h":
        jump investigate

    "ignore you stupid little bee word!!! (0o0)":
        jump notinvestigate


label investigate:
    w "EH~~~???!!!"
    "???" "REEEEEEEEEEEE UUUNNN HAAA AAA~~~ UUUUUUUUU"
    w "??????????? ^-('W')/^?"
    "you aproch and you see it!"
    "+5 kokoro pointS!"
    $ kp += 5
    jump encounter

label notinvestigate:
    "???" "REEEEEEEEEEEE UUUNNN HAAA AAA~~~ UUUUUUUUU"
    w "uuuuuuhhhhhhhhh"
    "then sudenly somthing grab you!!!!  |(0o0)/ "
    jump encounter

label encounter:
    "it is so desu~~~!!! a KAWAI KITSUNE CHAN!!~~~"
    show k_spook
    with vpunch
    w "oh desu it is {image=愛子狐ちゃん.png} ohio gossamer! :)"
    k "bbbrrrr brrrrr vrrrrrrooooommmmmmmm ima desu so watashi kuruma desuka?"
    w "watashi wa dare deskua?? I A-M W-H-O-Q-U-E-S-T-I-O-N-M-A-R-K-"

    show k_confuse
    with dissolve
    hide k_spook
    k "ano th er war dare derk waaaaaa???? chuuuu~~"
    w "U-ARE-AI-KO-KI-TSU-NE-CHAN-NE??? YOU ARE EHHH???"
    k "ii aaamm uuuhhh"
    w "hey aiko chan you want pain?? huh? you want pain???"
    k "?????"
    w "un"
    "you start punishing aiko kitsune chan because of bad behorbvor"
    play music "hit.mp3"
    pause 7.0
    stop music
    play music "night_time.mp3"
    scene bg scene2
    with fade
    k "eeeeteeeeeee ooowwwwiieee im sorry sir im sorry sir ih"
#6/16/18
    scene bg scene1
    with fade
    show k_scare
    w "Oh hi! My name is watashi and I just got lost in this forest for some reason... Nice to meet you!"
    k  "ummm hi..... i ---iii---ii mmy name iss-sss Aiiikooo kitsu ---ne chaa---nn--n~~ uuummm nice to meet you too nnnnnn"
    w "uuummm you live here?? or you are lost?? 4444444444444444444444444444444444444444444444444444444444444444444444444444444444444"
    k "ummm noo ii am protecc animal national reservveee.... i dont knowww ii amm----------- ... loosstt  aaannn"
    show k_normal
    w "Ok then, I guess we are both lost yes? Oh! I have an marvilis idea!!!! Lets---"

menu:#1st story change choice
    "stick together and get out":
        jump sticktogether
    "bye":
        jump notsticktogether
    "use my new ibay item that starts fires to send signals to the above":
        jump disaster

label disaster:#end
    hide k_scare
    show k_normal
    k "ok whateve but tha sem like great idea send signal to airlplane you now wink chu~~~~ :)"
    show k_blush
    w "mmmmmmmmmmmm"
    "+100 Kokoro point!! {image=愛子狐ちゃん.png} think you are real smart"
    "you set up the signal machine and you leave it there and wait until it works"
    play music "fire.mp3"#http://soundbible.com/2178-Crackling-Fireplace.html
    #fire noise sequence
    image fire:
        "fire1.png" with Dissolve(0.5, alpha=True)
        1
        "fire2.png" with Dissolve(0.5,alpha=True)
        1
        repeat
    scene fire


    w "uh oh taihen"
    k "iiiieaaa kyyaaa eeeeiiiiiiii iiiiii!!!!!!!!! not cooolbakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabaka"
    "oh no! -1000000000000 Kokoro point {image=愛子狐ちゃん.png} think you are bakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabakabaka"
    w "..."
    "ummmm every thing burn and creamtation"
    "... :( so unkawaii desu"
    image bad_end:#BAD END ANIMATION
        "bad_end1.png"
        0.1
        "bad_end2.png"
        0.1
        repeat
    scene bad_end
    with dissolve
    "anata wa go into heaven ja nai because you kill aiko kitsune chan and self NOT NICE IS MURDUER!!! smh smh w(>_<)w"
    return

label sticktogether:
    k "nn sure nnnnnnnnnn ........"
    $ kp += 10
    "+10 Kokoro Points!!!"
    jump together
    
label notsticktogether:
    k "but but but sppoky woods is not cool i need help to buddy systemu~~ yeah?"
    w "sure whatever ok hai come if you want its not like i want you to come you silly baka <3<3<3"
    k "haaaaaaaaaaaa~~~~~~"
    $ kp += 5
    "+5 Kokoro Points!!!! that was really cool yea?"
    jump together

label together:
    #new scene picture is ogether
    "so we are one group ima (now)"
    w "hhmmmm why are anata even here desuka???"
    k "oh yea i ned to resue the tsukihime!!!!"
    w "huuuhh??? nani is tsukihim??? nani ga nani ga desuka??? haaahh?"
    show tsukihime at Position(xpos = 0.5, xanchor=0.5, ypos=0.5,yanchor=0.5)
    k "is twukihime yeah?"
    hide tsukihime
    w "thank you for explanation tres magnificent et exceptionale, j'a i comprend tout les chose mainetment agigatou gossamer rarw xd nya~~ des"
    show k_blush
    $ kp +=10
    "you compliment! +10 kokoro point!"
    w "yah ok so yah like wadawanna do now like"
    k "mmmmmmmmmmmmmmmmmmmm aaann hahha iiii jyyaa wwee-  nee-eed to-oo uuuhhhh climb moun-tain no?"
    w "agree"
    k "eheheh you know da wae??? cuz idk .... .... ...."
    w "... ... ..."
    w "well there are 2 tree tunnels so yah???"
    k "mm i trush anata eheh growl rawr nya~~~"
    "hmmmmm pick which you wanna huh uuuuuuuuuuuuuuhhhhhhhhhuuuhhhhhhuuuuhhhhhhh la la al alalalal hm hm hm hm!!"

$ leftDone = False
$ rightDone = False
$ downDone = False
$ upDone = False

label tunnels:
    scene bg scene1
    show k_none

menu:#crucial 2nd branch
    

    "pick left" if not leftDone:
        jump left
    "pick right" if not rightDone:
        jump right
    "pick down" if not downDone:
        jump down
    "pick up" if not upDone:
        jump up

label up:
    scene tunnel_up
    "we try jump up yah but can not go up :("
    "bouncy"
    $ upDone = True
    jump tunnels

label down:
    scene tunnel_down
    k "uhh watashi wa afraid of heights and watashi suki ja nai small holes lets not ok? :)"
    w "wakarimasu"
    $ downDone = True
    jump tunnels

label left:
    scene tunnel_left
    w "ok we go left then..."
    k "unn"
    scene birdeye_forest
    "anatatachi wa walk real long...."
    "anatatachi wa see tsukihime???!!!! HUH????"
    scene run_to_moon
    k "mite mite!!~~ is watashitachi com her to reu srce you!!!!"
    #show aiko chan run to cliff scene and watashi in back reach out stop
    "aiko runs to it"
    w "AIKO CHAN STOP IT IS A CLIFF DONT GO"
    w "STOP STOP SAKRA COOKING STOP SAKRAUA COOKING STOP COOK made COOKIN STOP!"
    k "huh???~"
    #show aiko fall into abyss
    "{image=愛子狐ちゃん.png} uhh she uh falss off cliff and into abyss of you know yah??....... iii"
    scene run_to_moon2
    with vpunch
    k "KYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaa~~~~~~~~~~~~~"
    pause
    w "..."
    scene black
    with dissolve
    w "naze.... why... it was clif.... aik wif uuuhhhh uh huh uuuuukkk :("
    w "....... is not real huh?? so unkawaii unsugoi kakui ja nai arimasen......"
    w "mA B if I jump down too i can safe Kanojo mmm??"
    w "yah i jump now sayonara |(^o^)/ wwweeeee!!! aiko chan"
    "you go down uhuh yah and"
    #credits maybe but could be seperate story very neato ----------------------------------------------------------------------------------------------------
    return#for now

label right:
    scene tunnel_right
    w "um i choose you,,,,,,Right Tunnel!!!! GO!!"
    k "right tunnel right tunnel"
    "so you guys             .      .    go right tunnel :)"
    scene birdeye_forest
    "Watashitachi" "Let us walk and sing campfire song lee daa dii la~~~"
    scene forest_road
    show k_normal
    w "i hope it s  this wayyy ... yeah you?"
    show k_pray
    k "uuumm moi ausii i pray to Buddha: plz let this be right path"
    w "umm im athiest but i respect ur religin so yah but nic that you pray for watashitachis ^o^"
    hide k_pray
    k "arigatou~~~!!"
    $ kp += 1
    "ya got 1 Kokoro point cuz you were respectful to aikos religin and u didnt kil her wait you didnt right? ne~"
    w "ya ya less kep walk yah?"
    k "mm~"
    w "GUD! wink"
    show k_blush
    k "eheh"
    $ kp += 10
    "earn +10 kokoro point hey that wink was gud"
    hide k_blush
    w "hey how's school son"
    k "is great papa i made a paper airplane"
    w "i want "
    k "-sadal"
    w "!!!!"
    k "!!!!!!!"
    "watashitai" "!!!! GASP HAHAHHAHAHAHHAHAHAHAHHAHAHAHAHHAHHAHAHHHAHHAHAHHHAHHAHAHAHAHHAHHAHAHHAHAHAHAAHAAHHAHAHAHAHHHHHAHHHAHAHAAHAHAHA"
    w "oh hold on gotta make a call to the ya know 'cat'"
    show k_confuse
    k "??? nani ga 'cat' desuka????"
    w "lets take this into the bush?"
    k "k"
    scene black
    "???" "uh"
    "???" "hu"
    "???" "were jus t wasting time e now lest get mov i ng"
    "???" "ok"

label walk_forest:
    scene main_menunot1
    pause 0.001
    scene forest_road
    "be continue walk --ai en gee--"
    # "you know i dont even know what im doing why am i even doing this why am i even doing this why am i even doing this why why why why why why"
    # "its not even funny kawaiikitsunelover645 ur not funny just stop"
    show k_spook
    with dissolve
    k "i think wer geting close to the tsukim!!!! a few more hundrd meter or less???"
    "... ... ..."
    k "konichi wa hai osu hello???? dare ka ga ici is there who?"
    w "ohhh hiiii i am was just space out ya knwo i tire from wrok and stuff"
    show k_scare
    k "oohh that is badd!! you needd rest sleep you know!! you need more than 8 hour 8 hour a least??"
    hide k_scare
    k "i read that on digitaru newsu on tha INTERNET"
    k "BONSI BUDY help me find it. BONSI BUDY is very good buddy ^_^"
    "you smile becuz aiko chan do best and worry abou t you very nice"
    "you flash sexy smilreu and say:"
    w "thanks you! sexy babe foxy huh uh"
    show k_blush
    hide k_spook
    k "thank thank nnnnuuuuuuuuuuuuuu~~~"
    $ kp += 20
    "you got +20 kokoro point use foxy and sexy are real deal words yea???"
    k "you should.... take a ..... nap .... get some rest yah??? you look tire!!"
menu:
    "take rest slappy nappie":
        jump nap
    "nah we waste time":
        jump nonap

label nap:
    w "ur rite i am get tire and i there is nerve delay?? so  anoying amnn--- uugh what ever i nap"
    $ kp +=1
    ":) +1 kokoro point u did what she wan t"
    k "uuuhh ok uh go down on to ground yea? uhh uhuh"
    "you go on the ground and fal aspleelp"
    scene peeksleep
    play music "sleep.mp3"
    pause 9
    "..."
    scene black
    with fade
    "???" "wak up dud"
    stop music
    "???" "uuuughghhgg"
    "???" "WHAT ARE YOU DOING"
    "???" "RIGHT JA NAI >:("
    scene forest_road
    with fade
    play music "night_time.mp3"
    show k_normal
    k "wake up"
    jump continue_after_sleep


label nonap:
    w "I kindly refuse the offer u real nice but we waste time here i wanna get outta here you know and resuec! :)"
    show k_sad
    "{image=愛子狐ちゃん.png} looks real sad :( rejected hahhahahhhha"
    $ kp -=1
    "ohno!!! anata wa lost 1 kokoro point and now {image=愛子狐ちゃん.png} is not felin wel"
    k "nya rawr not XD :( ~~~"
    "sad mood"
    jump continue_after_sleep
#ugh im done for today and it is 6/17/18

label continue_after_sleep:
    w "whatever like lests just go i wana go to convention invetion center tomorow"
    k "uuuuhh okkk desu"
    "and you know yah? they walk and serch more but they get close to TSUKHIME!?!??!?!?"
    scene birdeye_forest
    with dissolve
    "walk"
    "w alk"
    "wa lk"
    "uhuh is me!!"
    "lalalalalalalalala they say"
    k "so close!!!!"
    "finale....and out of bush they arrife at open flat rock area moon gaze place..."
    scene look_at_tsukihime
    k "LOOK ITS THERE RIht THER LETS GO FETCH ME A LADDAR PARNER!"
    w "ah cant gomen ne~~"
    scene look_at_tsukihime_clear
    with fade
    show k_scare
    k "NANDESUKA NANI GA ANATA SAY NANI???"
    w "it is too high up wwe can never save tsukihim we need to "
menu:
    "send signal to the above using my new sigal shooter i got on amazer":
        jump disaster
    "... hey aiko chan...":
        jump true_love
label true_love:
    w "aiko chan is none of our busines ne?"
    w "yeah I now!! watashitachi wa perforn idniam ritual to god and let they hepl resuec tge tsukihime!! sugoi ideane ne~~"
    k "aaaaaaaahhh~~!!!watachi thought of that ja nai!! NEver think!! Watashi, you are such smarto!!!"
    $ kp +=10
    "ya gaut tan ko koro pointsa ya she thinke ya smart butt bee ward ,(o0o),"
    k "lets hajime yo then!!~"
    w "mm!"
    scene black
    with fade
    "???" "GOOOOO SETUP!!!"
    "???" "setup setup"
    image ritual:
        "ritual1.png" with Dissolve(0.5, alpha=True)
        0.7
        "ritual2.png" with Dissolve(0.5,alpha=True)
        0.7
        repeat
    scene ritual
    with dissolve
    "watashitachis" "mmmmmmmm relaaxxxxxxxxx~~~ "
    k "*sniff sniff mmph mmphn"
    w "huh!"
    "???" "pssssssss....."
    w "mmmmm oooooohh momoko sama"
    stop music
    "persons are down in silenc..."
    "wind blowss no crickets anymore..."
    k "wait ur atheist"
    w "golden rule"
    k "i see"
    w "we need help it is the time theat we real ned help becuz we need to resuce tsukihime and then get outta here but idk how to get so high and i am lost"
    k "ye- uh-ah- um- yah -uh -i am wit-ness i can p-p-rove uh got colder??"
    "the temperature drops by 1 degree celsius"
    w "plz help watasicahis!!! here i know you love these bitsy meaty treats here take some"
    "you take out your bag of cat chow"
    k "oooh tha look delisoicu can i haf one"
    w "hey aiko chan you wannt pain?? huuuh???"
    "aiko chan is not here anymore she focus on meaty bitsy pieces in your hand"
    w "you need a firm beating i see mm"
    "you start punishing aiko kitsune chan because of bad behorbvor"
    play music "hit.mp3"
    pause 7.0
    stop music
    scene bg scene2
    with fade
    k "eeeeteeeeeee ooowwwwiieee im sorry sir im sorry sir ih"
    w "good lets go back summonn momoko sama desu"
    scene ritual
    with fade
    w "kore wa the cat chowwwwwuuu~ to tabemasuka hai"
    k "m m hai"
    play music "sleep.mp3"
    pause 2
    stop music
    "you hear a sound!!!!"
    scene white
    with dissolve
    pause 1
    show momoko_sama
    with hpunch
    scene ritual
    with dissolve
    show momoko_sama at center
    with dissolve
    play music "noise.mp3"
    m "mreaow nya wan"
    "the {image=桃子樣.png} eats the meaty bits"
    "{image=愛子狐ちゃん.png} stares and feels real sad"
    scene look_at_tsukihime_clear
    with dissolve
    show momoko_sama at left
    show k_sad at right
    w "holo como estsas {image=桃子樣.png} i need you to go resuc the tsukihim you have to go up you know? we dont have laddar so we neeed help from spirit help? if you can do i give rest of bag ya?"
    "aiko chan becomes saddar because she can not eat the meaty treat bits"
    "you seee it"
menu:
    "feed aiko chan a meaty bitsy treat":
        jump feed
    "give rest of bag to momoko sama":
        jump notfeed

label feed:
    "you sneak a meaty treat bit out of the bag while momoko sama is eating and give it to aiko chan"
    show k_spook at right
    "aiko real happy desu"
    $ kp += 30
    "you got 30 kokoro point is yummy trsat"
    "Aiko chan will remember this :)"
    jump rescue

label notfeed:
    "you ignore aiko chan"
    $ kp -= 10
    "minis 10 kokoro point aiko chan understand situation but really want to eat but whatever buy later or somethnng :|"
    jump rescue

label rescue:
    hide k_spook
    show k_none at right
    "the {image=桃子樣.png} finish s eat the bag of tasty bits"
    m "uh ok leave everythins to me i resuc tsukihime hai desu promise done this thing is count as done and i tak all c redit cuz i a cool kiddo"
    m "... nothin presoneil....kidz....yea?? anatatachis have no idea.. no idea.... soo ughh"
    w "uh sure idc and get us outta here to civilization area yeah?"
    k "mmmm yeah agreae do it we gave you tasty bits"
    m "ok wait"
    m "mmmmmmmm oooommmmmmmm mmmmmm oooommmmmm"
    "momoko sama seperates from its body and resuces the tsukihime"
    m "mmmmmmmmmmm uuuuuuhhghghhghgh uoooooffff oooooooofff uuuuuugggg"
    m "I GOT IT"
    m "ok i resuce tsukime now i uuhh get anatatasis to civilize ation area..."
    #fly in sky
    scene travel_back
    with fade
    "so then the momoko sama did some magic trick idk but then sppoky magic start hapen like white stuff? idk but it was like gushing out of this place and like"
    "it was really cool but then we like rode on a thing and the next thing we knew we were in like a parking lot??? like idk but it was like a wildlife camp"
    scene parking_lot
    play music "night_time.mp3"
    with fade
    "area where people you know do the camping campfires and like there were wildlife things everywehere yah?"
    show k_normal
    with dissolve
    k "final watashitachu outta here sooo kimooochiiiii anata wa???"
    w "oohhh ugh so late i will need to tabemasu 10 gallons of coffe when i get home uugh so dizzy i canot walk straight even everythgn so wigly woblle... at least we rescu tsukihime yeah?"
    w "we are also ouuta heere yah? oh heck-"
    "you aidentaly drop an extra bag of tasty bitz on the floor"
    show k_spook
    "you slowly bend down and grab it and then you pic it up and then you put it back in"
    k "!!!"
    "aiko chan think hhmmm if he has one he must have more"
    hide k_spook
    k "hheeyy wanna go into that bathroom overthere??? nya"
    show k_blush
    k "ha"
    stop music
init:
    image movie = Movie(size=(1280, 720), xalign=0.5, yalign=0.5)
label credits:
    scene end
    play movie "credits_movie.ogv" noloop
    "you got [kp] Kokoro Points desu!!! ^_^"
#the end for now it is 6/18/18