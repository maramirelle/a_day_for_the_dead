# The script of the game goes in this file.


# The game starts here.

label start:

    label first_wake_up:

        scene bg darkness

        q_angel "Heeey! Heeey, you!"

        q_angel "Yeah, you! Exactly you! Wake up!"

        q_angel "No time to sleep — you're already dead!"

        q_angel "Heeey! Are you even listening?"

        q_angel "Ugh, what a terrible ghost..."

        q_angel "Get up or I’ll kill you again!!!"

        main_ch "Wh... what?"

        main_ch "Where am I?"

        q_angel "Ah, finally!"

        q_angel "At school, I think?"

        main_ch "But... I was just having pizza with my friends..."

        q_angel "That was over 24 hours ago."

        main_ch "No way! I remember... I remember..."

        q_angel "And now it’s gone, huh?"

        q_angel "Totally normal for a Star Soul."

        main_ch "A what soul? What are you talking about? Are you some kind of kidnapper?"

        q_angel "Oh yeah, sure — I kidnapped you and brought you to your own school. Makes total sense."

        main_ch "My... school?"

        main_ch "Guess I’m a student, then..."

        q_angel "You *were* a student. Now you're a corpse behind that door. Wanna take a peek?"

        main_ch "What door? I don’t see any..."

        q_angel "Later, later. I get it — you’re confused. Just take a deep breath and listen!"

        q_angel "Haha — oh wait, you can’t breathe anymore!"

        q_angel "Anyway! Let me introduce myself. I’m *insert name + dramatic title*!"

        main_ch "I must be dreaming..."

        angel "Call it whatever you want. I’ve got important info for you, my dear dead one!"

        main_ch "Okaaay..."

        angel "As a Star Soul, you get a little bonus. Since you were murdered, you’ve earned the right to trade your life for your killer’s. Not bad, huh?"

        main_ch "Not bad?! I was murdered! This dream keeps getting worse..."

        angel "Ughhh, what a dumb ghost..."

        angel "You’re running out of time!"

        main_ch "Me?!"

        angel "You’ve got 24 hours to figure out who you are — and who killed you."

        angel "Fail, and your soul goes straight to the Heaven Factory. You’ll become an energy source. Sounds fun?"

        main_ch "This is the worst dream ever..."

        angel "So, 24 hours. Tick-tock. Then you give me your answer. Are you ready?"

        main_ch "Let’s pretend I am."

        angel "Great! That was your choice."

        angel "Three..."

        angel "Two..."

        angel "One..."

        angel "The door opens!"

    label out_of_locker:

        scene bg bodies far

        main_ch "Wait... Wait, WHAT?!"

        main_ch "THREE dead girls?!"

        main_ch "I think I’m going to faint..."

        angel "Good luck with that, my dear dead one!"

        main_ch "Yes! Exactly! The dead ONE! But there are three bodies! This doesn’t feel like a funny joke!"

        angel "No jokes at all."

        main_ch "Then what am I supposed to do?"

        angel "As you already know — figure out who you are, and who killed you."

        main_ch "It didn’t sound easy before, but now..."

        main_ch "How am I even supposed to know which one is me? I don’t recognize any of them!"

        angel "Not my problem. Do whatever you like. Float around, haunt people, listen, watch — whatever works for you!"

        angel "Ah! One last rule!"

        angel "To make our cute little game more exciting, you won’t be able to enter any rooms you couldn't access while alive."

        angel "Pretty fair, don’t you think?"

        main_ch "Thinking’s not exactly my strong suit right now..."

        angel "Such a funny little dead one! I adore you, really!"

        angel "Time’s ticking! You’d better hurry!"

        main_ch "Okay. Okay..."

        main_ch "Three dead girls, then."

        main_ch "Guess I should take a look..."

        scene bg bodies close

        main_ch "Hmm... None of them look familiar. If one of these is really my body, it doesn’t stir anything. No weird feelings, no chills. Nothing."

        main_ch "Are all ghosts like this?"

        main_ch "I mean, pop culture told me ghosts can appear out of nowhere, throw stuff, write bloody messages on walls... and at the very least, remember their names!"

        angel "Nope. You're special, dear Star Soul."

        angel "Ah, I see. Memory’s not your forte either."

        angel "Then here's one more little gift for our lovely dead one!"

        $ remember_unlocked = True

        angel "Now you can remember anything you’ve seen or heard — *exactly* as it was. Just tap that REMEMBER button. It’s floating right beside you."

        angel "Why not start by remembering the crime scene?"

        angel "And now - you're all set up!"

    label tutorial_1:    

        tutor "Hi there! The Heaven Factory hopes you enjoy your after-death adventure!"

        tutor "We'd like to make sure you've managed to understand how it works."

        tutor "You can’t view past dialogue. The moment is all you have — so be careful, and make sure to remember what matters."

        tutor "To recall what you’ve chosen to remember, open the \"Memories\" screen."

        tutor "To move around the school, call \"School Map\" screen."

        tutor "To save your progress, choose \"Save\" screen."

        tutor "To load data, use \"Load\" screen."

        tutor "More tools will be unlocked when you proceed further."

        tutor "Time’s ticking! Don’t forget to check the clock now and then."

        tutor "Good luck, Star Soul! You’re bound to succeed — eventually."

    label hallway:

        angel "Well, that’s all around here. Why not go outside?"

        main_ch "If outside exists at all, hah."

        main_ch "Maybe I’m still in my bed, you know."

        angel "This bloody floor doesn’t look like a *convenient* bed, does it?"

        main_ch "Hmmm… At least I’ve got good company here."

        angel "It was a joke?"

        angel "This dead one is able to joke!"

        main_ch "Okay, okay. Outside. There should be a kind of hallway, I guess?"

        angel "Try and see."

        main_ch "I need a ‘Ghost Floating 101’ or something… hah."

        angel "That’s easy. Just wish — and you’re already moving!"

        main_ch "To the hallway, then..."

        scene bg hallway

        main_ch "Oh, I see. It’s the hallway."

        angel "Exactly."

        angel "Doors, windows… nothing special."

        angel "Ah, look!"

        scene bg board far

        main_ch "The Honor Board?"

        main_ch "Two, four, six... There are fourteen students there, right?"

        angel "As you can see. Wanna look closer?"

        main_ch "Mhm."

        scene bg board close
        
        main_ch "So..."

        main_ch "Fourteen talented students. But no clues on their talents here."

        angel "Wondering why these photos are here?"

        angel "Okay, here's your answer: these are all the students left at this school."

        angel "I’m too kind today! Must be because you’re such a cute little dead one!"

        main_ch "Oh, thanks."

        main_ch "Wait, what do you mean? Only fourteen students at this school at all? Why?"

        angel "Nah, I won't tell anything else."

        main_ch "..."

        main_ch "Okay."

        main_ch "The students..."

        main_ch "These three… They look just like the bodies in the classroom."

        main_ch "Yagasuri Eki. Sounds like a warrior… and looks like one too, with her inappropriate clothes and those rolled eyes."
        
        main_ch "Or maybe she just doesn't like to be photographed."

        main_ch "Chishibuki Yuri… That’s a weird combo for a name."

        main_ch "Hmmm… It sounds like a prophecy. A blood fountain with a young lily inside. Brrr..."

        main_ch "Anyway, Chishibuki-san looks serious. Like a yakuza daughter. Maybe the deaths are somehow connected to crime?"

        main_ch "Kusuriya Dokumi. I wonder if her family has a pharmacy business."

        main_ch "To be honest, she looks too weak for someone who could probably get any treatment she wants, hah."

        main_ch "Still, surnames are just weird words. They don’t define people."

        main_ch "So, who's left?"

        main_ch "Of course, almost everyone."

        main_ch "Four more girls."

        main_ch "Shinri Rikorisu. The only one with her name in katakana. Looks… sporty?"

        main_ch "Menmou Misora. Nice girl with a poetic name. Looks kind."

        main_ch "Ougyoku Midori. Looks important. Whatever that means."
        
        main_ch "Come ooon, her surname is Topaz - what else could I say, hah?"

        main_ch "Okay, no more surname associations."

        main_ch "And the last girl: Soradaki Gyokuro. I wonder if she actually resembles gyokuro tea."
        
        main_ch "If so, she must be like the sea under the sun — not hot, but soft and calm. Like jasper warmed by the hands."

        main_ch "Anyway, seven more students left. And I’ve already forgotten the first ones…"

        angel "Take it easy. I’ll make a little copy of this board for my cute dead one."

        main_ch "If so... Okay. Thanks."

        main_ch "Now - the boys."

        main_ch "Katakiyaku Nanka."

        main_ch "..."

        angel "Go on, comment on his surname."

        main_ch "..."

        main_ch "This world is definitely not real."

        angel "Why?"

        main_ch "Nobody has crazy surnames like this in real life."

        angel "Oh, believe me, little dead one, surnames are like the abyss. You never know what’ll come out next."

        main_ch "Let's pretend I believe. So, Katakiyaku-san is a bad guy with a soft heart. Probably."

        main_ch "Kuumojiretsu Kimyou. How could I even read this..."

        angel "You've managed somehow."

        main_ch "Obviously."

        main_ch "So, he doesn't look misterious at all. I guess his parents wanted him to be a dark hero, but they failed."

        main_ch "Kinzoku Kiiro. Looks shy. And kinda hungry. Or maybe more than kinda."

        main_ch "Had he ever eaten at all?"

        angel "The dead one is you, not him, so..."

        main_ch "Okay, okay."

        main_ch "Gojinka Kanki. Looks confident. Two god kanjis multiply the effect."

        main_ch "Shinkan Kiki. Why’s he called dangerous? Just a boy with a messy hair, I suppose."

        main_ch "But of course not so messy as this one's. Keisetsu Udonge. Does he protest against his clever surname? I wonder if he succeeds."

        main_ch "And the last one. Finally."
        
        main_ch "Hichou Hari. Hmmm... Nothing special. I'll forget his face the moment I look somewhere else."

        main_ch "So, what about my copy?"

        angel "Here you are."

        tutor "Hi there again! Congratulations with the first win! Now you have a complete suspects list!"

        tutor "Let's proceed to a new \"Students\" screen!"

        tutor "Here you can not only look through prepared info, but also add your own notes on any topic!"

        tutor "We hope this screen will help in your investigations!"

        tutor "Let's go, Star Soul!"

        scene bg hallway

        angel "Now you saw everyone from this school."

        angel "Fourteen students. Three are dead. Eleven are alive. Someone is a murderer."

        angel "So, let's..."

        angel "Oh, look! Who's there?"

        main_ch "Hmmm... Katakiyaku-san, as far as I remember."

        main_ch "Is he going..."

        angel "Kya-ha-ha-ha! Finally! Come on, come on, come oooon! The most interesting part is just about to start!"

        main_ch "Okay, okay."

        main_ch "I'm a bit nervous. This discovery will obviosly spoil his day."

        angel "What a *compassionate* dead one!"

        main_ch "Do you think I'm wrong?"

        angel "Nope! The only thing I think is — we’ve got to watch! Hurry up or I'll kill you again!"

        main_ch "..."

        main_ch "Good luck, then."

        angel "..."

        main_ch "..."

    label bodies_discover:

        scene bg bodies far

        gunman "..."

        gunman "..."

        gunman "..."

        gunman "What the hell?!"

        gunman "Hey, anyone! Anyone!.."

        angel "What a funny face! Glad we didn’t miss it!"

        main_ch "..."

        angel "What's up, little dead one?"

        main_ch "I'm feeling a bit guilty."

        angel "What?! Ha-ha-ha-ha-ha! Seriously?"

        main_ch "..."

        angel "No way!"

        angel "You're really incredible!"

        angel "Oh, look! The boy brought company!"

        barling "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!"

        kitten "..."

        barling "NO WAY — THEY CAN'T BE DEAD!!!"

        kitten "..."

        bang "What the..."

        bang "Oh... OH!"

        barling "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!"

        handsome "Shinri-san, why are you..."

        handsome "..."

        basic "Udonge, are you here?"

        basic "Oh, what's up guys? We've heard you from outside..."

        basic "Mmmm... I see..."

        basic "aaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!"

        basic "..."

        goldsmith "..."

        fly "They are all... They are all..."

        goldsmith "..."

        bang "...dead."

        forest "Must be a nightmare."

        curly "Oh, here you are, guys!"

        curly "..."

        curly "What's THIS?"

        curly "A drama club play?"

        angel "It definetely IS drama."

        main_ch "And maybe even a play."

        main_ch "Sorry, everyone..."

        angel "Oh, the last one!"

        queen "Who's crying? What's..."

        queen "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!"

        queen "THREE... THREE DEATHS!"

        bang "I'm not an expert, but it doesn't look like a collective suicide."

        kitten "Am I..."

        gunman "Definetely here. Nothing's changed."

        gunman "They are really dead."

        kitten "..."

        angel "What do you think, my little dead one? Any suspects already?"

        main_ch "Nope."

        main_ch "But if yesterday I was eating pizza with my friends, I just need to understand which of those dead girls it was. I'm sure her friends would mention it."

        angel "Ah, feels dramatical, right? Pizza for yesterday, spoilt meet for today..."

        main_ch "..."

        angel "Okay, that was really too much. I'm sorry."

        main_ch "That was funny. Don't stop."

        angel "What a hilarious dead one!"

        main_ch "So, what's happening at the moment? What are they discussing?"

        curly "...there must be a murderer hiding somewhere!"

        queen "Do you remember this night's weather? Who on Earth would go here at such a storm?"

        handsome "He could be hiding here before the storm started. Or maybe the girls brought him here when they were returning from the city?"

        barling "I saw them coming. They were alone. Nobody suspicious with them."

        basic "I was outside when the girls returned and I stayed there for approximately 15 more minutes. The road and the school yard was empty."

        fly "So, there is a mysterious murderer at the school. No one saw him, except his victims..."

        kitten "I understand that's important, but could we probably move somewhere else?"

        queen "That sounds like a good idea. Those bodies..."

        forest "A frightening view."

        main_ch "Everyone's gone."

        angel "What do you think?"

        main_ch "There were girls who went to the city yesterday."

        main_ch "I wonder who were those girls..."

        main_ch "Anyway, I don't want to lose the point of their conversation!"

        angel "Let's go, then."

    label murder_discussion:

        main_ch "Where are we going?"

        angel "That should be the science classroom."

        main_ch "..."

        angel "I see. Science doesn’t sound like your cup of tea?"

        main_ch "I was just thinking a bit."

        main_ch "I’m not even sure I used to study here. I can’t remember any lessons, any places, any students..."

        angel "You’re already dead. So calm down. No need to worry about exams."

        main_ch "Oh? What kind of exams are you talking about?"

        angel "Well, you know. Before you graduate, you usually have to pass some exams..."

        main_ch "So it’s my last school year now?"

        angel "Definitely. You won’t be studying anywhere ever again."

        main_ch "That’s not the point. I mean, I’ve almost graduated, haven’t I? Besides, if I succeed in my investigation, I’ll come back to life, so..."

        angel "What a clever dead one! Rrrr, I didn’t want to give you hints anymore!"

        main_ch "But you did."

        angel "Okay, I’m disappearing! Figure it out yourself!"

        main_ch "..."

        main_ch "And now they’re gone."

        main_ch "So, what are my classmates doing there?"

        scene bg science

        queen "We need to do something right now! Three girls are already dead! What if he’s planning to kill the rest of us *right now*?!"

        bang "We don’t even know if it was a planned murder. Maybe the girls just saw something they weren’t supposed to?"

        basic "We’d better call the police. They’re the experts — they’ll figure everything out."

        fly "Yeah, it’d be super cool if we could just..."

        gunman "Nobody can protect us except ourselves."

        curly "Okay, the phone’s broken, but we can still go out! Chishibuki-san and the others went to the city yesterday. Why can’t we do the same?"

        main_ch "Chishibuki-san... That serious dead girl!"

        bang "Hari and I were outside this morning. The storm damaged the road — rocks everywhere. I don’t think any of us could make it through."

        barling "So all we can do is just wait until tomorrow evening, then..."

        fly "Looks like it..."

        queen "But what about the murderer?! He might still be here!"

        handsome "If we don’t go anywhere alone, nobody can attack us. I think."

        kitten "But there were *three* of them in the art classroom!"

        curly "That’s true..."

        fly "It’s time to admit we’re in real danger."

        basic "And we can’t do anything about it."

        gunman "We're still able to search the school together. It's not so big, so if there is a murderer somewhere, he wouldn't remain unnoticed."

        bang "That's true. There are still eleven of us. Even if we have to deal with ninja, he won't kill all of us in a second!"

        forest "Still, while we're travelling here and there in such large company, the murderer may sneak off."

        kitten "Are you offering to divide our groop, Shinkan-san?"

        forest "Yes. Five of us will go upstairs, the rest will observe the first floor and the school yard."

        forest "If you don't mind, of course..."

        curly "Sounds good. I gonna stay here. Who's with me?"

        queen "Me!"

        basic "Okay, me too."

        bang "Me either. Menmou-san?"

        kitten "Okay, I'm in."

        handsome "I'd better stay here too."

        barling "So, Katakiyaku-kun, Soradaki-chan, Shinkan-san, Kinzoku-san and I are going upstairs."

        bang "Let's meet at the kitchen when we're done."

        gunman "Okay. Good luck, guys."

        main_ch "It looks like I need to choose which groop to haunt."



        






























        


 
 





    

    # This ends the game.

    return
