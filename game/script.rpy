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

        gunman "We can still search the school together. It's not that big, so if there's a murderer hiding somewhere, they won’t go unnoticed."

        bang "That's true. There are still eleven of us. Even if we're dealing with a ninja, they can't kill all of us in a second!"

        forest "Still, while we're walking around in such a large group, the murderer might sneak away."

        kitten "Are you suggesting we split up, Shinkan-san?"

        forest "Yes. Five of us will go upstairs, and the rest will watch the first floor and the schoolyard."

        forest "If you don't mind, of course..."

        curly "Sounds good. I'm gonna stay here. Who’s with me?"

        queen "Me!"

        basic "Okay, me too."

        bang "Same here. Menmou-san?"

        kitten "Alright, I'm in."

        handsome "I’d better stay here too."

        barling "So, Katakiyaku-kun, Soradaki-chan, Shinkan-san, Kinzoku-san, and I will go upstairs."

        bang "Let’s meet in the kitchen when we’re done."

        gunman "Okay. Good luck, guys."

        main_ch "Looks like I need to choose which group to follow."

        menu:

            "Stay at the 1st floor":
                jump choice1_down

            "Go upstairs":
                jump choice1_up

    label choice1_down:

        $ choice1_flag = True

        main_ch "So, I'm staying here."

        main_ch "My current company is Curly, Queen, Basic, Bang, Handsome and Kitten. Four boys, two girls."

        handsome "So, let's go."

        kitten "Where are we going to start from?"

        bang "Maybe let's split up and move from the ends of the hallway to the exit?"

        queen "I'm taking the kitchen part!"

        bang "As you wish. I'm going to start from the gym. Who's with me?"

        curly "Count me in."

        basic "Same here."

        queen "Isn't it more wise to form groups of one girl and two boys instead?"

        handsome "Sounds rational."

        queen "Kuumojiretsu-kun, would you like to join us?"

        curly "Hmmm..."

        curly "Okay..."

        kitten "So, I'm with you, Keisetsu-kun, Hichou-kun."

        bang "We don't mind at all."

        basic "Yeah, sure!"

        curly "See you later, guys!"

        main_ch "Okay, they are leaving me alone again."

        angel "Chase someone, then!"

        main_ch "Fair enough."

        main_ch "Feels like Ougyoku-san stole Kuumojiretsu-san from his company. I'm curious about what do they think of it, so..."

        bang "...And nobody's here. Us only."

        main_ch "And me."

        kitten "Definitely."

        basic "Or they're ninjas!"

        kitten "Or they are ninjas."

        main_ch "No ninjas around here. Just me."

        angel "How can you say you're not a ninja if you don't remember anything, my cute dead one?"

        main_ch "..."

        main_ch "I don't feel like a ninja."

        angel "What kind of feeling is it supposed to be?"

        main_ch "..."

        main_ch "Who knows?"

        angel "Don't stare at me, I'm not a ninja!"

        main_ch "Okay, okay."

        kitten "To the Classroom A, then?"

        basic "Yes, sure. Let's go!"

        bang "Hari, wait a sec."

        basic "What, your heart is beating too fast when you're at the same place with lil Kitten, hah?"

        bang "Shut up! It's not the point!"

        basic "The Queen stuff, then? Just chill out, dude!"

        bang "..."

        basic "Queen is Queen. You know her. She is crazy about controlling everything around her."

        basic "And smile, dude! Be fuckin' nice! It's your Misora-chan with us, not Queen!"

        bang "..."

        bang "My bad."

        basic "See?"

        kitten "Aren't you attacked by ninjas, guys?"

        basic "Sorry, Menmou-san, we're coming!"

        bang "Yeah!"

        main_ch "Interesting."

        angel "What exactly?"

        main_ch "The nicknames."

        angel "Not the romantical stuff?"

        main_ch "No."

        angel "Your heart is too cold, you know?"

        main_ch "Not only the heart. I'm cold from head to toes."

        angel "..."

        main_ch "I'm dead, you know?"

        angel "I'm just realising how hilarious you are, my little dead one!"

        main_ch "I have a normal name, don't I?"

        angel "You can choose any nickname instead!"

        main_ch "No, thanks."

        main_ch "In addition, I'm sure I already have one."

        angel "Looks like that."

        main_ch "So, now I know that Menmou-san is Kitten and Ougyoku-san is Queen."

        main_ch "I think, these nicknames are a real match."

        main_ch "I wonder what's mine."

        main_ch "Anyway, I wanna take a look at the Queen's group."

        angel "Sure, go on, my pretty dead one!"

        queen "Keep the door open, Gojinka-kun. I don't wanna get stuck at the murderer's trap."

        handsome "The door don't have any locks, but if you wish so..."

        curly "It seems to me, there's nobody except us around here. Just like at the kitchen."

        curly "The only ones that could accompany us are ghosts, but they don't seem to give us any hints. Or throw any knifes."

        handsome "Exactly."

        main_ch "Dunno about the knifes, but I can't give you any hints."

        main_ch "Sorry, guys, I know less then you do, really."

        queen "Are you mocking at me?"

        curly "Not at all, Ougyoku-san."

        queen "..."

        queen "I believe you. But only for {i}this{/i} time."

        curly "Glad to hear."

        curly "Anyway, let's proceed to the Sciense Class."

        handsome "Sounds good."

        queen "I agree."

        queen "Who's that murderer, I wonder."

        handsome "If we knew, we wouldn't search them here and there."

        curly "Cannot disagree."

        queen "What would we do if we found nobody? It feels..."

        handsome "Scary?"

        queen "Like, the danger may wait for us everywhere - and we won't be able to protect ourselves!"

        curly "Let's hope for better."

        curly "The girls couldn't just lay down and die from nothing. It means, someone did it. A real human, with flesh and bones."

        curly "So, if that someone is real, we can catch them."

        curly "I don't know what we'll do with them when catch, still there will be all of us against one human being."

        curly "We are bound to succeed."

        handsome "Sounds rational."

        queen "I'm glad you joined us, Kuumojiretsu-kun! Your words make me feel better."

        curly "Happy to hear."

        curly "So, no one's here again."

        handsome "If only we could fix the phone..."

        queen "Forest and Goldsmith tried, but nothing changed. As I heard."

        handsome "Yeah, they're kinky about the wire stuff as nobody else, so, if they failed, no one of us will succeeds."

        curly "Right."





        jump choice1_done

    label choice1_up:

        $ choice1_flag = False

        main_ch "So, let's proceed upstairs."

        main_ch "My current company is Forest, Barling, Fly, Gunman and Goldsmith. Three boys, two girls."

        barling "We're here again..."

        barling "A lot of things changed from our last time here."

        fly "You're right. How could any of us imagine that our classmates... our friends..."

        fly "..."

        forest "..."

        goldsmith "..."

        gunman "We *must* find the murderer."

        goldsmith "It's the only thing we can do for them three, isn't it?"

        fly "Not only for them, actually. The murderer may kill someone else, so..."

        forest "Looks like nobody's here."

        main_ch "Except me."

        barling "That's true. Only us five."

        main_ch "And me. Us six."

        barling "I wish we opened their room and they're here..."

        main_ch "I'm still here."

        forest "We have to accept the reality as it is. They're gone."

        main_ch "Not actually..."

        forest "And there's no way for them to return."

        main_ch "If I were you, I won't be so confident about it."

        angel "Hahaha, what a hilarious dead one! I've just gone away and - here you are! Already talking to yourself!"

        main_ch "Nah. Was talking to them. They just didn't answer."

        angel "Oh, really annoying alive ones!"

        main_ch "I'm not annoyed."

        angel "Neither am I."

        main_ch "..."

        angel "..."

        main_ch "Hey, I'm not even sure I know anybody here."

        main_ch "They're kinda sad and it looks like my death is the reason, but..."

        main_ch "I feel nothing, you know?"

        main_ch "Just like I was always..."

        main_ch "Like this."

        angel "Dead."

        angel "Okay, right now gonna prove you were alive. Look!"

        forest "There's no one at the study room."

        gunman "Just as at any other one here, hah?"

        goldsmith "And no traces that anyone from outside were here."

        gunman "Ah, Shinri, found something?"

        barling "..."

        barling "That's nothing... I've just... You know..."

        barling "..."

        fly "We were at the girls' room and... There was their photo..."

        forest "The one they've took yesterday?"

        barling "...Yes."

        goldsmith "Show it to us, please, Rikorisu-san."

        barling "Yes, of course..."

        #photo

        main_ch "Wait a minute."

        forest "They seem to be so happy here..."

        main_ch "Isn't it the photo from the photo booth?"

        goldsmith "They look like they know nothing about what would happen to them in a few hours..."

        main_ch "And the date is... Yesterday, right?"

        angel "Yeah."

        #memory of three with pizza

        main_ch "Nah, that can't be true!"

        angel "Just because you don't allow it to be?"

        angel "That's the truth, my dear dead one!"

        main_ch "And how am I supposed to understand which one is me?!"

        angel "Not my business."

        main_ch "Wait! Don't..."

        main_ch "...dissappear. Yeah, just like this."

        main_ch "But who cares, right?"

        gunman "So, looks like that's all here."

        fly "We've found nothing..."

        goldsmith "Nothing is also something. Like, it means that the murderer is not here."

        gunman "I guess, it's time to join the guys downstairs. Maybe they were more lucky..."

        barling "Or unlucky..."

        gunman "Or unlucky."

        fly "Okay, let's go!"

        main_ch "So, dunno about them, but the thing I've found out doesn't make me happier at all."

        jump choice1_done

    label choice1_done:

        bang "What's up, guys?"

        gunman "Nothing at all."

        goldsmith "At least, there were no ninjas upstairs. Or they're hiding too well."

        basic "They couldn't call themselves ninjas if they let you found themselves so easily, you know?"

        forest "No objections."

        bang "See?"

        fly "You two are talking like you've actually found those ninjas!"

        $ if choice1_flag == True:
        
            main_ch "Not really."

        basic "..."

        basic "Not really..."

        $ if choice1_flag == True:
        
            main_ch "Just as I said."

        queen "Let me interrupt this obviously intelligent discussion."

        $ if choice1_flag == True:

            main_ch "Queen as she is."

            angel "I'm a bit tired of Her Magesty."

            main_ch "Me too."        

        $ else:

            main_ch "Sounded like passive agression."

            main_ch "What's whong with her?"

            angel "Perhaps the crown's too heavy."

            main_ch "Which crown?"

            angel "The metaphorical one."

            main_ch "Okay..."

        kitten "No one is here. No one except ouselves."

        fly "It should sound like relief but..."

        barling "It's too scary to admit that..."

        curly "The murderer is someone we already know."

        basic "One of..."

        bang "...us."

        "..."

        angel "You have dramatic classmates, you know?"

        main_ch "They are shocked. It's okay to stare at anyone in silence when you realise such an awful thing."

        angel "Probably. Any suspects?"

        main_ch "Not really..."

        main_ch "Everyone seems to be suspicious and innocent at the same time."

        main_ch "The time..."

        angel "Limited, yeah."

        main_ch "I know."

        angel "Okay, okay, don't get mad."

        main_ch "Madness is not one of my plans."

        main_ch "At least, for now."

        angel "Scary-scary!"

        main_ch "And they're gone. Again."

        main_ch "..."

        main_ch "Who's the murderer?"

        main_ch "..."

        main_ch "Nah. No ideas."

        basic "So, why are we just standing here as silly statues? We have to do something!"

        queen "What are we supposed to do, then?"
        
        queen "Don't you think the murderer's gonna raise the hand and say something like:"
        
        queen "\"Oh, I'm so, sooooo soooorry! Forgive me, {i}please{/i}!!!!!!!!!!!!!!\" "

        queen "Don't be an idiot, Hichou Hari!"

        basic "Ougyoku-saaaaan, you're too rude!"

        main_ch "Cannot disagree."

        bang "Let's return to the topic."

        bang "Are there any other suspects except us eleven?"

        handsome "Who else could it be? We've searched everything from top to bottom and - nothing."

        fly "Oh, wait-wait-wait! I have an idea!"

        curly "I guess it's the same as mine. About three more suspects, right?"

        fly "Yeah!"

        barling "What do you both mean?"

        curly "Look, there are three bodies at the art class. But what if they've just killed each other?"

        gunman "But for what reason?"

        kitten "Looks like there's no reason. They were besties. I can't remember them arguing or something."

        bang "They could be... You know..."

        gunman "No way! Aren't you talking about..."

        bang "Yeah. One of them was actually {i}Junkie{/i}."

        $ if choice1_flag == True:

            main_ch "Another strange nickname?"

        $ else:

            main_ch "Junkie? Who's that?"

        barling "Hey, couldn't you be a bit more respectful, Keisetsu-kun? She's our dead classmate..."

        bang "And what's next?"

        bang "Let's stop pretending we don't know that everyone calls everyone by nicknames!"

        bang "Don't make such a face, {i}Barling{/i}."

        bang "You too, {i}Forest{/i}. And {i}Queen{/i}, don't act like it's the first time you hear it. Weren't you the one who started it all?"

        $ if choice1_flag == False:

            main_ch "Oh, {i}that{/i} kind of crown..."

        queen "You!.."

        bang "I know. Bang, right? Just because I'm kinda crazy, like I'm gonna to blow up the whole school at the next second, hah?"

        bang "It's not a secret for me at all!"

        curly "You guys need to cool down."

        handsome "Yeah, we already have three corpses. We don't want to get two more."

        kitten "Midori-chan, let's go out."

        fly "May I join you?"

        kitten "Sure. We're going to library. It's calm there."

        kitten "Midori-chan, {i}let's go{/i}."

        queen "..."

        bang "Don't say I'm wrong!"

        basic "You're not wrong, Udonge. It's just..."

        curly "The timing was a bit..."

        bang "I know..."

        bang "It's not everyday stuff. Those three deaths."

        handsome "Anyway, are we going to stay here all day?"

        curly "Really. I'm thinking of sleeping a bit."

        barling "Sleeping?"

        curly "Wanna skip this day as fast as I can."
        
        curly "We have to admit that we can't do anything without the police."

        curly "Even if we found the murderer, what would we do next? Kill them too, just in case?"

        basic "Maybe it isn't the worst idea ever..."

        bang "And what's next? Jail? No, thanks. I'd better go to the university instead."

        curly "Yeah. Me too."

        curly "So, I'm leaving."

        handsome "I'm going with you."

        curly "Oh, Gojinka-kun, you won't regret, I promise! Sleep is the perfect way of skipping time!"

        barling "See you later, guys."

        handsome "Sure."

        gunman "There's still some homework left for me to do, so..."

        barling "Oh, Nanka, I've completely forgotten about it! The project!"

        gunman "That's exactly what I'm talking about. To the study room, then?"

        barling "Let's go!"

        basic "Are they serious about that project?"

        forest "That's the last thing to care about, don't you think so?"

        bang "Hah, that's true. I can't believe we're going to study at Monday. It feels like Monday will never come. Like the time's frosen."

        goldsmith "It's obviously normal. Three deaths stand between us and our usual life. Feeling of time can't be the same as before."

        bang "Mhm..."

        basic "Udonge, what about playing some card games?"

        bang "Why not? Everyone skips the time, why can't we do the same? Guys, are you with us?"

        forest "Yeah."

        goldsmith "Of course."

        basic "So, the cards..."

        bang "Okay, okay, I'll bring them."

        bang "Hari, it's ridiculous - invite me to play and don't have the cards!"

        basic "I'm kinda sorry."

        bang "Not at all."

        basic "Who knows? Hey, go already!"

        bang "Hahahaha!"

        main_ch "Okay, they finally settled."

        angel "It looks like your classmates split up again, hah?"

        main_ch "Yes, that's true."

        angel "So, are you going to stay here or haunt anyone else?"

        main_ch "Hmmm..."

        tutor "Ding-dong! It's time to add a new screen!"

        tutor "Here's the School Map screen."

        # tutor explains how the screen works. Player can visit two places with people at 1 hour. Places without people don't affect time.
        # Every hour someone moves somewhere, soooo...









        











        # ... the game continues here.
 


        






























        


 
 





    

    # This ends the game.

    return
