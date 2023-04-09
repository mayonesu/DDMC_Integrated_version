label ch6_1_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[5] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 6
        $ style.say_dialogue = style.normal
        $ quick_menu = True
        scene bg club_day2
    play music mend
    show yuri 4b at t11
    y "Umm...[player]?"
    "I'm about to follow them, but yuri stops me."
    voice "voice/yuri/yuri_ch6_01.ogg"
    y 4a "I have...something to tell you,please?"
    mc "Ah...yes."
    "I was expecting it in the morning."
    "She sent me an enormous volume of texts."
    "They were about not only the festival,but some random...well,a kind of suggestive one."
    voice "voice/yuri/yuri_ch6_02.ogg"
    y 3g "Well,you've read through the pamphlet yet?"
    "Jeez, not about the texts?"
    mc "Ah...almost."
    voice "voice/yuri/yuri_ch6_03.ogg"
    y 3h "Have you read Sayori's poem?"
    "Suddenly my heart aches.I forget about it.No,I wanted to."
    voice "voice/yuri/yuri_ch6_04.ogg"
    y 3j "Why do you think she wrote that kind of one?"
    mc "That kind of...well,it's her usual style,isn't it?"
    voice "voice/yuri/yuri_ch6_05.ogg"
    y 3r "No. She won't write like that,usually."
    show yuri 2r
    "She's not shy anymore now. I sigh."
    mc "W-won't she?"
    voice "voice/yuri/yuri_ch6_06.ogg"
    y 1l "She looked different these days. Yesterday,too."
    voice "voice/yuri/yuri_ch6_07.ogg"
    y 1k "It is why she doesn't come to school today,isn't it?"
    mc "W-well...she's,ah,tired...because of the preparations of the festival?"
    voice "voice/yuri/yuri_ch6_08.ogg"
    y 2r "I don't mean that."
    mc "..."
    voice "voice/yuri/yuri_ch6_09.ogg"
    y 2f "Sayori...has done something to you,right?"
    stop music fadeout 1.0
    show expression "#000000c0"
    "I'm stunned. What the heck is she talking about...? I know my friend was..."
    "She was...just asleep...and I looked into her face...wait,wait."
    "Did I go straight to her bed? Why did it take so much time?"
    "Before I went to her...I was doing something. I am slowly remembering it."
    "I...I hold her...her body? W-why?"
    "...I remember my hands felt the weight of her...what,what happened there?"
    hide expression "#000000c0"
    play music t10
    y 3p "...[player]?"
    mc "...Eh?"
    voice "voice/yuri/yuri_ch6_10.ogg"
    y 3o "Well...your...tears..."
    "I get flustered and touch my cheeks. I...I'm weeping...???"
    mc "W-what the...? Why...why am I..."
    voice "voice/yuri/yuri_ch6_11.ogg"
    y 2h "Damn...she...Sayori did..."
    stop music fadeout 1.0
    mc "S...SAYORI...?"
    play sound "sfx/s_kill_glitch1.ogg"
    window hide(None)
    show noise zorder 9:
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
        repeat
    pause 1.0
    hide noise
    window auto
    "Suddenly,something has changed in my mind."
    scene black
    "I was taking care not to say her name unconsciously."
    "But now,all the feeling are storming into me. I...I now remember that..."
    stop music fadeout 1.0
    "..."
    "..."
    hide yuri
    scene bg club_day2
    with dissolve_scene
    show yuri 3n at face
    play music t10
    "...Finally I realize that Yuri is shaking my shoulders."
    voice "voice/yuri/yuri_ch6_12.ogg"
    y 2n "[player]! Are you OK? are you REALLY OK!?"
    show expression "#ff000060"
    voice "voice/yuri/yuri_ch6_13.ogg"
    y 2w "What a pity...I knew it but...She...She did it to my [player]...!"
    show yuri 3y7
    "Suddenly she realeases her hands,and I fall on the floor."
    stop music fadeout 1.0
    voice "voice/yuri/yuri_ch6_14.ogg"
    y 3y4 "I never forgive that girl."
    show yuri 1y4
    "She lowers her tone. Her eyes get darkened."
    voice "voice/yuri/yuri_ch6_15.ogg"
    y 1y1 "I never forgive YOU,too. You played on my heart and you fell on her."
    show yuri 3y1
    "I see something glitter in her hand...A knife!?"
    show yuri 2y1
    "She regrips it slowly, and give me a fierce look."
    show yuri 2y4
    mc "Hey...you...w-what...!"
    show yuri 3y4
    "I jump to her as soon as I hear her scream."
    mc "Stop it!...what the...hey! Calm down...!"
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    play sound "sfx/stab.ogg"
    pause 6.0
    play sound fall
    pause 1.0
    if persistent.chapter == False:
        return
    else:
        call ch6_1_1_main

label ch6_1_1_main:
    "Alright,alright."
    "Now I come to remember it."
    "Sayori is not here. Nevermore."
    "And what's next?"

    pause 1.0
    show y_kill
    with dissolve_cg
    pause 1.0
    play music t6s
    "WHY IS YURI DEAD HERE !?"
    "What the hell..."
    "WHAT THE HELL !!!"
    "I didn't do it..."
    "I didn't do anything..."
    "I remember that something drove Yuri crazy suddenly..."
    "I tried to stop her..."
    "And..."
    "What happened?"
    "I don't remember."
    "Here,I'm looking at the body which once was Yuri."
    "Ha ha..."
    "Ha ha ha ha ha..."
    "What an awful nightmare."
    "I am still dreaming now."
    "Yuri,Sayori...they are still in their own beds,right?"
    menu:
        "Yeah this is..."
        "Just a Nightmare.":
            $ yuri_end = 1
        "My reality.Accept it.":
            $ yuri_end = 0
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    if persistent.chapter == True:
        if yuri_end == 1:
            call bad_yuri_main
            call endgame
            return
        else:
            jump ch6_2_main
    return

label ch6_2_main:
    if persistent.horror_effects and renpy.random.randint(0,8) == 0:
        play sound "sfx/gnid.ogg"
        scene red
        with Dissolve(7)
        pause 2.0
        play sound "sfx/giggle.ogg"
        pause 2.0
        scene black
        if not persistent.achievement[8]:
            $ renpy.notify(achievement_notify + achievement_name_9)
            $ persistent.achievement[8] = True
            play sound "tl/None/sfx/achievement.ogg"
            pause 2.0
        if ddmm_online and persistent.ddmm_achievement:
            $ ddmm_register_achievement("MAD_YURI", achievement_name_9, achievement_message_9)
            $ ddmm_earn_achievement("MAD_YURI")
        pause 1.0
    scene bg club_day2
    with dissolve_scene_full
    play music t6
    voice "voice/natsuki/natsuki_ch6_01.ogg"
    n "I'm back yay~ It's the festival time!"
    show natsuki 4k zorder 2 at t11
    voice "voice/natsuki/natsuki_ch6_02.ogg"
    n "Wow,you got here before me?"
    voice "voice/natsuki/natsuki_ch6_03.ogg"
    n "What are you doing th..."
    show natsuki scream at h11
    stop music
    voice "voice/natsuki/natsuki_ch6_04.ogg"
    n "EYAH!"
    mc "N-No...it's nothing...to do with me..."
    voice "voice/natsuki/natsuki_ch6_05.ogg"
    n "AAAAAAAAAAAAAAAHHHH!!!"
    window hide(None)
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki vomit at lhide
    hide natsuki
    "Natsuki runs away."
    mc "Wait! You're misunderstanding me!"
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    "I come to my sense and run out of the classroom in a hurry."
    scene bg stairs
    with wipeleft_scene
    "Trails of vomitting...did she go upstairs?"
    mc "Natsuki!"
    "I run up the stairs."
    mc "Wait,please!"
    "I hear the cracking sound of the door above my head...the rooftop."
    scene bg rooftop
    with wipeleft_scene
    show natsuki 1o zorder 2 at t11
    "There I find Natsuki. A frightened look on her face,she steps backwards from me."
    mc "Natsuki..."
    voice "voice/natsuki/natsuki_ch6_06.ogg"
    n scream "Go away,GO AWAAAAAY!"
    mc "Calm down,please,and listen,listen to me..."
    voice "voice/natsuki/natsuki_ch6_07.ogg"
    n "No,noooo!"
    scene bg rooftop:
        zoom 1.5
    hide natuski
    show natsuki 1p at face
    "She steps backwards and is back against the fence,which I didn't intend to."
    "I slowly walk to her. She's now too nervous."
    mc "Please,listen to me."
    "I talk to her gently. Her tension goes away, and she squats down."
    voice "voice/natsuki/natsuki_ch6_08.ogg"
    n 1n "Don't...come near...don't...please don't..."
    voice "voice/natsuki/natsuki_ch6_09.ogg"
    n 1m "S-sorry...I am...very...s-sorry..."
    voice "voice/natsuki/natsuki_ch6_10.ogg"
    n 12b "I will...be...a good girl...so..."
    voice "voice/natsuki/natsuki_ch6_11.ogg"
    n 12f "Forgive me...forgive me...please...please..."
    stop music fadeout 0.5
    "I'm taken aback. What is she saying...?"
    "She's trembling. I put my hand on her shoulder gently and,"
    mc "{cps=30}Nats...{/cps}{nw}"
    play music t6r
    voice "voice/natsuki/natsuki_ch6_12.ogg"
    n scream "AAAAAAAAAAAAAAAHHHH!!!"
    show expression "#ff000060"
    "She screamed."
    "It happened so fast. She climbed up the fence and,"
    show natsuki scream at lfhide
    hide natsuki
    "She flew."
    "..."
    "..."
    stop music fadeout 1.0
    show expression "#000000b0"
    with dissolve_scene
    play sound "sfx/fall.ogg"
    pause 2.0
    "Ha ha."
    "Ha ha ha ha ha."
    "What the hell is it."
    "Surely the nightmare is going on."
    "Or I lost my mind completely."
    menu:
        "I don't care,because this is..."
        "Just a Nightmare.":
            $ natsuki_end = 1
        "My reality.Accept it.":
            $ natsuki_end = 0
    scene black
    with dissolve_scene
    if persistent.chapter == False:
        return
    else:
        if natsuki_end == 1:
            call bad_natsuki_main
            call endgame
            return
        else:
            jump ch6_3_main
    return

label ch6_3_main:
    pause 0.5
    show end_glitch1
    with dissolve_scene_full
    play music m1b    
    q "Howdy..."
    q "Hmm?"
    q "Over 75%%."
    q "Welldone."
    scene black
    stop music fadeout 1.0
    with dissolve_scene_full
    pause 1.0
    if persistent.chapter == False:
        return
    else:
        call ch7_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
