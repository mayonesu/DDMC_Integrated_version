label ch10_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[9] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 10
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    scene black
    play music t6
    "..."
    scene bg closet
    with dissolve_scene_full
    show natsuki 4d at t11
    "...I get a closer look at the box set she's admiring."
    mc "Parfait Girls...?"
    "It's a series I've never heard of in my life."
    "Natsuki pulls out the first volume of Parfait Girls from the box."
    show natsuki 5g
    "I stare at the cover."
    "It features four girls in colorful attire striking animated feminine poses."
    "It's...exceedingly 'moe'."
    voice "voice/natsuki/natsuki_ch10_01.ogg"
    n 5c "Chairs wouldn't work."
    voice "voice/natsuki/natsuki_ch10_02.ogg"
    n 5k "We can't read at the same time like that."
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    hide natsuki
    "..."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    voice "voice/natsuki/natsuki_ch10_03.ogg"
    n "A lot of the beginning is about simple things..."
    show n_cg1_exp1 at cgfade
    voice "voice/natsuki/natsuki_ch10_04.ogg"
    n "Like there's a really funny chapter where they're obsessed with a guy at the icecream shop..."
    hide n_cg1_exp1
    voice "voice/natsuki/natsuki_ch10_05.ogg"
    n "But later on,there's all kinds of drama..."
    show n_cg1_exp5 at cgfade
    voice "voice/natsuki/natsuki_ch10_06.ogg"
    n "Like when they get into all their backstories,and when some of the romance starts to happen..."
    hide n_cg1_exp5
    show n_cg1_exp4 at cgfade
    voice "voice/natsuki/natsuki_ch10_07.ogg"
    n "There are so many touching parts."
    hide n_cg1_exp4
    "..."
    if persistent.horror_effects and renpy.random.randint(0,10) == 0:
        stop music
        show n_cg1b
        hide n_cg1_base
        play music "tl/None/sfx/error.ogg"
        $ gtext = glitchtext(renpy.random.randint(20, 180))
        n "[gtext]"
        play music t6
        hide n_cg1b
        show n_cg1_base
        show n_cg1_exp1
        if not persistent.achievement[10]:
            $ renpy.notify(achievement_notify + achievement_name_11)
            $ persistent.achievement[10] = True
            play sound "tl/None/sfx/achievement.ogg"
        if ddmm_online and persistent.ddmm_achievement:
            $ ddmm_register_achievement("NATSUKI_FACE", achievement_name_11, achievement_message_11)
            $ ddmm_earn_achievement("NATSUKI_FACE")
    else:
        show n_cg1_exp1 at cgfade
    "Suddenly Natsuki starts laughing."
    voice "voice/natsuki/natsuki_ch10_08.ogg"
    n "Ahahaha!"
    "Natsuki puts her finger on one of the panels."
    stop music fadeout 1.0
    voice "voice/natsuki/natsuki_ch10_09.ogg"
    n "Sayori is my favorite character!"
    show expression "#000000a0"
    "...Huh?"
    play music m1
    show monika 1d at t42
    voice "voice/monika/monika_ch10_01.ogg"
    m "..."
    show monika 1h
    mc "What the...?"
    voice "voice/monika/monika_ch10_02.ogg"
    m 1e "Do you remember...Parfait Girls?"
    show monika 1f
    show expression "#000000a1"
    "W-was I dreaming then?"
    "I was reading a manga with Natsuki...No."
    "I was talking with Monika,and she..."
    "She told me that I killed everyone."
    "Did I...?"
    hide expression "#000000a1"
    voice "voice/monika/monika_ch10_03.ogg"
    m 2g "What do you think of Parfait Girls?"
    show monika 2f
    mc "Huh!?"
    mc "W-what the heck are you talking about?"
    mc "How dare you ask me such a dumb question? Do you think it's more important than..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch10_04.ogg"
    m 1q "Yes."
    voice "voice/monika/monika_ch10_05.ogg"
    m 1i "Important. Very important."
    show monika 1h
    mc "..."
    voice "voice/monika/monika_ch10_06.ogg"
    m 2i "What do you think of Parfait Girls?"
    show monika 2h
    mc "W-well...it's just typical...manga... What do you want me to say?"
    voice "voice/monika/monika_ch10_07.ogg"
    m 1i "Yes. It's typical. Like..."
    show monika 1h
    mc "Like?"
    play music m1
    voice "voice/monika/monika_ch10_08.ogg"
    m 1r "Us."
    show monika 1h
    mc "..."
    voice "voice/monika/monika_ch10_09.ogg"
    m 2i "Four girls. In high school. They fall in love with a new guy, who came to them one day."
    show monika 2h
    mc "Things like that often happen...in manga."
    voice "voice/monika/monika_ch10_10.ogg"
    m 2i "Yes. Common story. Like us."
    voice "voice/monika/monika_ch10_11.ogg"
    m 3i "By the way, did you notice four girl's school uniforms? They were very similar to us,weren't they?"
    show monika 3h
    mc "I-I don't know..."
    show expression "#000000a1"
    "Yes,I remember. They were very similar to us,actually."
    hide expression "#000000a1"
    mc "But it happened to be..."
    voice "voice/monika/monika_ch10_12.ogg"
    m 2d "Hmm. Have you read all the volume of Parfait Girls?"
    show monika 2c
    mc "No,I just read volume 1."
    voice "voice/monika/monika_ch10_13.ogg"
    m 2d "So,you don't know one of the gilrs commits suicide later?"
    show monika 2c
    mc "Eh!?"
    voice "voice/monika/monika_ch10_14.ogg"
    m 2g "Like..."
    show monika 2o
    "She speaks evasively."
    voice "voice/monika/monika_ch10_15.ogg"
    m 1i "I know that many more things are similar...to us."
    voice "voice/monika/monika_ch10_16.ogg"
    m "Though you may say you don't know."
    voice "voice/monika/monika_ch10_17.ogg"
    m 2i "Actually, I've read all the volume. For several times."
    voice "voice/monika/monika_ch10_18.ogg"
    m 1o "To learn about this..."
    show expression "#000000a1"
    "What in the world is she talking about...?"
    "It's just an ordinary moe manga...isn't it?"
    hide expression "#000000a1"
    show monika 1h
    mc "Monika...What do you want to say? Do you want to tell me that Parfait Girl was written about us?"
    mc "Huh,horrible thought. I can't believe..."
    voice "voice/monika/monika_ch10_19.ogg"
    m 1i "No."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch10_20.ogg"
    m 2r "Parfait Girls wasn't written about us."
    voice "voice/monika/monika_ch10_21.ogg"
    m 2i "We were made to be similar to Parfait Girls."
    voice "voice/monika/monika_ch10_22.ogg"
    m 1i "To be accurate, this world was."
    show expression "#000000a1"
    show monika 1h
    "..."
    play music m1
    "Ha ha...the craziest joke of the day..."
    "But..."
    "But why?"
    "Why is my heart pounding?"
    hide expression "#000000a1"
    voice "voice/monika/monika_ch10_23.ogg"
    m 2d "Natsuki loved Parfait Girls."
    voice "voice/monika/monika_ch10_24.ogg"
    m 2c "She loved it so much."
    voice "voice/monika/monika_ch10_25.ogg"
    m 3g "Because there was the happiness she dreamed."
    voice "voice/monika/monika_ch10_26.ogg"
    m "Because there was a typical slicec-of-life affair she longed for."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch10_27.ogg"
    m 1r "She created this world."
    voice "voice/monika/monika_ch10_28.ogg"
    m "The world of Parfait Girls she loved."
    voice "voice/monika/monika_ch10_29.ogg"
    m 1i "In other words,YOU created this world."
    if persistent.chapter == False:
        return
    else:
        call ch10_1_main

label ch10_1_main:
    stop music fadeout 1.0
    show monika 1i at thide
    hide monika
    hide expression "#000000a0"
    hide n_cg1_exp1
    show n_cg1_exp5 at cgfade
    show expression "#000000a0"
    play music t5nr
    "It happens,sometimes."
    "I don't deny it. Now I don't deny anything."
    "Because,"
    show monika 1g at t42
    voice "voice/monika/monika_ch10_30.ogg"
    m "You remember it,right?"
    show monika 1f
    show expression "#000000a1"
    "Monika, the answer is 'NO'."
    "I don't remember anything as ever."
    "Too many things happened at the same time."
    "I'm too tired to deny them all."
    "And my heart is still pounding so much."
    "Yeah, my brain wants to deny it, but my body doesn't admit it."
    hide expression "#000000a1"
    mc "I remember Parfait Girls."
    mc "Natsuki always pushed me so hard to read it."
    mc "But I didn't know why."
    mc "That's all I remember."
    voice "voice/monika/monika_ch10_31.ogg"
    m 1e "Okay..."
    show monika 1i
    mc "But I don't understand what you said."
    show monika 1h
    mc "Natsuki created...what?"
    mc "Why does it mean I did it?"
    voice "voice/monika/monika_ch10_32.ogg"
    m 2r "This world is..."
    stop music
    voice "voice/monika/monika_ch10_33.ogg"
    m 2i "Fake."
    voice "voice/monika/monika_ch10_34.ogg"
    m 2n "In a sense."
    voice "voice/monika/monika_ch10_35.ogg"
    m 2r "But at the same time,it's our reality."
    voice "voice/monika/monika_ch10_36.ogg"
    m 3i "And it..."
    show monika 3h
    mc "You want to say that Natsuki created this 'fake' world as if it's real?"
    play music t9
    voice "voice/monika/monika_ch10_37.ogg"
    m 2p "Yes...or no."
    voice "voice/monika/monika_ch10_38.ogg"
    m 2r "She didn't know it,at least conciously."
    voice "voice/monika/monika_ch10_39.ogg"
    m 2h "And this world is not fake,for us. This is our reality."
    voice "voice/monika/monika_ch10_40.ogg"
    m 1r "But...um..."
    show monika 1q
    mc "Now I don't care whether this world is fake or not."
    mc "Everything happens here. Now I know it."
    mc "I don' believe all the things you tell me."
    mc "But tell me."
    "She closes her eyes and is quiet for a while."
    voice "voice/monika/monika_ch10_41.ogg"
    m 1h "...Okay. I'm going to tell you all...as long as I know."
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    if persistent.chapter == False:
        return
    else:
        call ch10_2_main

label ch10_2_main:
    play music t3d
    if not persistent.save_graphic:
        show mask_2
        show mask_3
        show room_mask as rm zorder 1:
            size (1280,720)
            pos (0,0)
        show room_mask2 as rm2 zorder 2:
            size (1280,720)
            pos (0,0)
    else:
        show monika_back
    show expression "images/bg/club.png" zorder 3
    with Dissolve(1)
    show monika 1i zorder 4 at t43
    voice "voice/monika/monika_ch10_42.ogg"
    m "I'm going to tell you an old story."
    voice "voice/monika/monika_ch10_43.ogg"
    m 2i "Or a myth."
    voice "voice/monika/monika_ch10_44.ogg"
    m 2h "..."
    voice "voice/monika/monika_ch10_45.ogg"
    m 2r "Once upon a time,there was a miserable girl."
    voice "voice/monika/monika_ch10_46.ogg"
    m 2i "She lived in a facility, surrounded by thick walls."
    show monika 1h
    stop music fadeout 1.0
    mc "Was she...Natsuki?"
    voice "voice/monika/monika_ch10_47.ogg"
    m 1d "Um...Monika's tip number 3?"
    mc "Don't bother Monika...okay."
    play music t3d
    voice "voice/monika/monika_ch10_48.ogg"
    m 2r "She was miserable."
    voice "voice/monika/monika_ch10_49.ogg"
    m 2i "Once in a week,sometimes twice or more..."
    voice "voice/monika/monika_ch10_50.ogg"
    m 1i "She earned punishment. Well,she thought it was a punishment."
    voice "voice/monika/monika_ch10_51.ogg"
    m 1g "Anyway,she was very afraid of it. It was so painful,so dreadful,so ruthless."
    voice "voice/monika/monika_ch10_52.ogg"
    m 1r "To avoid it, she hoped she could go insane,but couldn't."
    voice "voice/monika/monika_ch10_53.ogg"
    m 2i "She was too intellectual to go insane."
    show monika 1h
    stop music fadeout 1.0
    "..."
    "Is she talking on an allegory or something?"
    play music t3d
    voice "voice/monika/monika_ch10_54.ogg"
    m 3i "The only comfort for her was reading."
    voice "voice/monika/monika_ch10_55.ogg"
    m 2i "When she was left alone, she was allowed to read something."
    voice "voice/monika/monika_ch10_56.ogg"
    m "There was a lot of books. Although the most of them were texts and documents for her education."
    voice "voice/monika/monika_ch10_57.ogg"
    m 3d "But there was a set of Parfait Girls. I don't know why there was a manga. Maybe someone from the staff gave them to her, who felt sympathy or something..."
    show monika 1c
    stop music fadeout 1.0
    mc "Wait. The staff? What kind of? In the first place,what was the facility?"
    voice "voice/monika/monika_ch10_58.ogg"
    m 1g "Um...I don't say anything for now."
    play music t3d
    voice "voice/monika/monika_ch10_59.ogg"
    m 1r "Anyway,Parfait Girls was the only comfort for her. She didn't know what was outside the facility for the long time,"
    voice "voice/monika/monika_ch10_60.ogg"
    m 2i "So Parfait Girls was exactly a whole world for her."
    voice "voice/monika/monika_ch10_61.ogg"
    m 2d "...She always imagined she was a character in Parfait Girls."
    voice "voice/monika/monika_ch10_62.ogg"
    m 1d "Sometimes she was a clumsy girl full of energy, sometimes a mature and timid girl, sometimes a smart and beautiful girl who was the most popular in class."
    voice "voice/monika/monika_ch10_63.ogg"
    m "Of course she could be a cute tsundere. She could even be a handsome boy of the ice cream shop."
    voice "voice/monika/monika_ch10_64.ogg"
    m 3d "Just only in her imagination."
    voice "voice/monika/monika_ch10_65.ogg"
    m 2g "But the reality is cruel."
    voice "voice/monika/monika_ch10_66.ogg"
    m 2r "Once in a week, the time of The Punishment came to her."
    voice "voice/monika/monika_ch10_67.ogg"
    m 2i "She told to herself that it was just a nightmare,"
    voice "voice/monika/monika_ch10_68.ogg"
    m "When the morning came,she would wake up in her bed and would go to high school,"
    voice "voice/monika/monika_ch10_69.ogg"
    m "Where her friends were waiting for her to meet in the club room."
    show monika 1r
    stop music fadeout 1.0
    "Monika breathes a sigh."
    "And she starts telling the story again."
    play music t3d
    voice "voice/monika/monika_ch10_70.ogg"
    m 2i "One day,on the day of The Punishment,one of the staff noticed,"
    voice "voice/monika/monika_ch10_71.ogg"
    m "That the results were so irregular every time they experimented on her."
    voice "voice/monika/monika_ch10_72.ogg"
    m "As if they did the experiment on multiple subjects,not on only one person."
    voice "voice/monika/monika_ch10_73.ogg"
    m "They tried to find the cause of it,"
    voice "voice/monika/monika_ch10_74.ogg"
    m "And finally they found,"
    voice "voice/monika/monika_ch10_75.ogg"
    m "That she had four or more personalities."
    voice "voice/monika/monika_ch10_76.ogg"
    m "That she was Multiple Identity Disorder."
    m 2h " ..."
    voice "voice/monika/monika_ch10_77.ogg"
    m 1r "...All the experiments were cancelled."
    voice "voice/monika/monika_ch10_78.ogg"
    m "They couldn't get the right numeric data from her anymore."
    voice "voice/monika/monika_ch10_79.ogg"
    m "Unless they put her multiple personalities together,"
    voice "voice/monika/monika_ch10_80.ogg"
    m 1i "As one."
    if persistent.chapter == False:
        return
    else:
        call ch10_3_main

label ch10_3_main:
    voice "voice/monika/monika_ch10_81.ogg"
    m 3d "[player],do you know how to put the multiple personalities together as one?"
    show monika 3c
    mc "Well...no."
    voice "voice/monika/monika_ch10_82.ogg"
    m 1d "To put them together,"
    voice "voice/monika/monika_ch10_83.ogg"
    m "You have to delete them."
    show expression "#000000a0" zorder 5
    "..."
    "W...what did she say right now?"
    hide expression "#000000a0"
    mc "'To delete'?"
    voice "voice/monika/monika_ch10_84.ogg"
    m 2r "They thought like that."
    voice "voice/monika/monika_ch10_85.ogg"
    m 2i "It's not so bad, indeed."
    voice "voice/monika/monika_ch10_86.ogg"
    m "At least, only one personality remains in the end."
    show expression "#000000a0" zorder 5
    show monika 2h
    "..."
    "What...what is she talking about?"
    "Perhaps..."
    hide expression "#000000a0"
    voice "voice/monika/monika_ch10_87.ogg"
    m 3d "But in most cases, deleted personalities don't disappear completely."
    voice "voice/monika/monika_ch10_88.ogg"
    m "They are living in..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch10_89.ogg"
    m 2p "...Oh."
    voice "voice/monika/monika_ch10_90.ogg"
    m 1q "Nevermind."
    voice "voice/monika/monika_ch10_91.ogg"
    m 3i "Anyway,"
    play music t3d
    voice "voice/monika/monika_ch10_92.ogg"
    m "They built the fake world for her."
    voice "voice/monika/monika_ch10_93.ogg"
    m 2r "Fake...no. The another reality for her."
    voice "voice/monika/monika_ch10_94.ogg"
    m 1i "The reality similar to her favorite manga."
    stop music
    voice "voice/monika/monika_ch10_95.ogg"
    m "Like..."
    window hide(None)
    show monika 1i at t31
    pause 0.3
    play sound "sfx/crack.ogg"
    hide expression "images/bg/club.png"
    show expression "bg/club_hole.png" zorder 3
    $ pause(0.5)
    stop sound
    show monika 1i at t43
    window show(None)
    voice "voice/monika/monika_ch10_96.ogg"
    m 3i "THIS."
    show monika 3i at thide
    hide monika
    show expression "#000000a0" zorder 5
    "...Wow."
    "...What the..."
    "...What the f..."
    show monika 2m zorder 4 at t43
    play music m1
    voice "voice/monika/monika_ch10_97.ogg"
    m "Well,you don't seem to remember yet..."
    voice "voice/monika/monika_ch10_98.ogg"
    m 2n "Um...we should talk to each other some more."
    voice "voice/monika/monika_ch10_99.ogg"
    m 1q "Ahem."
    hide expression "#000000a0"
    voice "voice/monika/monika_ch10_100.ogg"
    m 3i "In her reality, there was also her favorite people."
    voice "voice/monika/monika_ch10_101.ogg"
    m 2r "Her precious friends."
    show monika 2r at thide
    hide monika
    voice "voice/monika/monika_ch10_102.ogg"
    m "One of them had..."
    show sayori 3c zorder 4 at t43
    voice "voice/monika/monika_ch10_103.ogg"
    m "The name which started with S."
    show sayori 4m
    voice "voice/monika/monika_ch10_104.ogg"
    m "Bright, energetic but clumsy."
    show sayori 1b
    voice "voice/monika/monika_ch10_105.ogg"
    m "But she had the other side."
    show sayori 1f
    voice "voice/monika/monika_ch10_106.ogg"
    m "Lonely. Introvated. Depressive."
    show sayori 1g
    voice "voice/monika/monika_ch10_107.ogg"
    m "She was not a fool. Actually, she was a wise girl in a sense."
    show sayori 1k
    voice "voice/monika/monika_ch10_108.ogg"
    m "You know? S stands for Shadow."
    show sayori 1u
    voice "voice/monika/monika_ch10_109.ogg"
    m "Your shadow."
    show expression "#000000a0" zorder 5
    mc "Huh?"
    mc "W-who are you talking about?"
    mc "...Me? Why me? I thought you were talking about the miserable girl..."
    hide expression "#000000a0"
    show sayori 1u at thide
    hide sayori
    voice "voice/monika/monika_ch10_110.ogg"
    m "Shadow. The other side of you. The side you don't know conciously."
    show yuri 1f zorder 4 at t43
    voice "voice/monika/monika_ch10_111.ogg"
    m "Okay. Next came the girl whose initial was Y."
    show yuri 1m
    voice "voice/monika/monika_ch10_112.ogg"
    m "Mature and gentle. Timid and mysterious."
    show yuri 1l
    voice "voice/monika/monika_ch10_113.ogg"
    m "She loved you. Loved you madly."
    show yuri 1i
    voice "voice/monika/monika_ch10_114.ogg"
    m "She loved your everything. She never denied you even though you were insolent and indecisive."
    show yuri 1e
    mc "..."
    voice "voice/monika/monika_ch10_115.ogg"
    m "Y stands for Yes. The girl who affirms all of you."
    voice "voice/monika/monika_ch10_116.ogg"
    m "Who never denies you."
    show yuri 1e at thide
    hide yuri
    voice "voice/monika/monika_ch10_117.ogg"
    m "If there's the girl of Yes,of course there's also the girl of No."
    show natsuki 5c zorder 4 at t43
    voice "voice/monika/monika_ch10_118.ogg"
    m "Cute but childish. Aggressive and sarcastic."
    show natsuki 5g
    voice "voice/monika/monika_ch10_119.ogg"
    m "She stands on the opposite side of the girl of Yes."
    show natsuki 5o
    voice "voice/monika/monika_ch10_120.ogg"
    m "So they can't get along with."
    show natsuki 5n
    voice "voice/monika/monika_ch10_121.ogg"
    m "She loves you in her own way. But she denies you."
    show natsuki 5s
    voice "voice/monika/monika_ch10_122.ogg"
    m "The Girl of No."
    mc "Monika,wait a minute..."
    show natsuki 5k
    mc "Wasn't...wasn't the miserable girl...Natsuki?"
    voice "voice/monika/monika_ch10_123.ogg"
    m "Yes...or no. She wasn't Natsuki,but sometimes she was."
    voice "voice/monika/monika_ch10_124.ogg"
    m "The personality of Natsuki was the closest to hers. But she wasn't Natsuki completely."
    show natsuki 5k at thide
    hide natsuki
    show expression "#000000a0" zorder 5
    mc "Monika..."
    stop music
    mc "{cps=5}WHO IN THE WORLD ARE YOU?{/cps}"
    hide expression "#000000a0"
    show monika 1f zorder 4 at t43
    voice "voice/monika/monika_ch10_125.ogg"
    m "Umm...well..."
    voice "voice/monika/monika_ch10_126.ogg"
    m 1g "I am..."
    window hide(None)
    pause 0.3
    play sound "sfx/crack.ogg"
    hide expression "bg/club_hole.png"
    $ pause(0.5)
    stop sound
    pause 1.0
    window show(None)
    if persistent.chapter == False:
        return
    else:
        call ch10_4_main

label ch10_4_main:
    voice "voice/monika/monika_ch10_127.ogg"
    m 1p "...It seems we have little time left."
    voice "voice/monika/monika_ch10_128.ogg"
    m "Can't you remember yet?"
    show monika 1o
    mc "I'm sorry,but...no."
    voice "voice/monika/monika_ch10_129.ogg"
    m 1g "Oh..."
    window hide(None)
    pause 10.0
    window show(None)
    voice "voice/monika/monika_ch10_130.ogg"
    m 1d "...Oh."
    voice "voice/monika/monika_ch10_131.ogg"
    m "How fool I am!"
    voice "voice/monika/monika_ch10_132.ogg"
    m 1r "Gimme a second..."
    window hide(None)
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.")
    $ delete_character("sayori")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    pause 1.0
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    pause 1.0
    call hideconsole
    window show(None)
    "Just at the moment,"
    window hide(None)
    scene white
    with Dissolve(1)
    pause 1.0
    window show(None)
    "The world gets white out."
    "And the lightning streams into my mind."
    window hide(None)
    pause 1.0
    play sound "sfx/glitch1.ogg"
    show sayori 5a at face
    pause 0.3
    pause 0.3
    show sayori 5a at thide
    hide sayori
    pause 0.5
    stop sound
    pause 1.5
    play sound "sfx/glitch1.ogg"
    show yuri 4b at face
    pause 0.3
    pause 0.3
    show yuri 4b at thide
    hide yuri
    pause 0.5
    stop sound
    pause 1.5
    play sound "sfx/glitch1.ogg"
    show natsuki 5u at face
    pause 0.3
    pause 0.3
    show natsuki 5u at thide
    hide natsuki
    pause 0.5
    stop sound
    pause 1.5
    play music "sfx/gnid.ogg"
    window show(None)
    "..."
    "Ah..."
    "Now...I understand."
    stop music
    show monika 1g zorder 4 at t11
    voice "voice/monika/monika_ch10_133.ogg"
    m "Do you remember now?"
    show monika 1f
    mc "Yes...completely."
    voice "voice/monika/monika_ch10_134.ogg"
    m 1d "They're dead, but at the same time, They're living in you."
    voice "voice/monika/monika_ch10_135.ogg"
    m "You know, now you're almost the one."
    voice "voice/monika/monika_ch10_136.ogg"
    m 1g "And now..."
    show monika 1f
    mc "Tell me,Monika."
    mc "Who are you?"
    mc "In other words, what does M stand for?"
    if not persistent.save_graphic:
        show mask_2
        show mask_3
        show room_mask as rm zorder 1:
            size (1280,720)
            pos (0,0)
        show room_mask2 as rm2 zorder 2:
            size (1280,720)
            pos (0,0)
    else:
        show monika_back
    show monika 2d
    voice "voice/monika/monika_ch10_137.ogg"
    m "M stands for..."
    voice "voice/monika/monika_ch10_138.ogg"
    m "Mother."
    voice "voice/monika/monika_ch10_139.ogg"
    m "The one who embraces you, who advices and leads you."
    voice "voice/monika/monika_ch10_140.ogg"
    m 3i "And where you came from."
    voice "voice/monika/monika_ch10_141.ogg"
    m "And where you go back to."
    voice "voice/monika/monika_ch10_142.ogg"
    m 1o "..."
    play music t10
    voice "voice/monika/monika_ch10_143.ogg"
    m 1p "No. I'm not such an outstanding one."
    voice "voice/monika/monika_ch10_144.ogg"
    m "I'm just a..."
    voice "voice/monika/monika_ch10_145.ogg"
    m 1o "Helpless girl."
    voice "voice/monika/monika_ch10_146.ogg"
    m 1p "Who can only watch. Just watching everything."
    voice "voice/monika/monika_ch10_147.ogg"
    m 1n "Do you know that the name Monika associates with Latin word 'monere'?"
    show monika 1m
    mc "..."
    voice "voice/monika/monika_ch10_148.ogg"
    m 2i "Monere means 'the one who advices', also means 'to watch'."
    voice "voice/monika/monika_ch10_149.ogg"
    m "I've been watching, since an epiphany striked me."
    if persistent.chapter == False:
        return
    else:
        call ch10_5_main

label ch10_5_main:
    stop music fadeout 0.5
    play music mend fadein 1.0
    show monika 2h
    mc "Epiphany..."
    voice "voice/monika/monika_ch10_150.ogg"
    m "You know, Sayori got the same epiphany,too. Yuri and Natsuki didn't,but they knew this world was something different from normal. Although not conciously."
    voice "voice/monika/monika_ch10_151.ogg"
    m "Only you didn't know that."
    show monika 3m
    mc "Yes,you're right."
    voice "voice/monika/monika_ch10_152.ogg"
    m 2g "To be sure, they weren't real, but"
    voice "voice/monika/monika_ch10_153.ogg"
    m "They could feel happy when pleased, could get upset when angry and could feel sad when sad."
    voice "voice/monika/monika_ch10_154.ogg"
    m 2e "They were alive, in a sense."
    voice "voice/monika/monika_ch10_155.ogg"
    m 2d "Well, I'm not blaming you..."
    voice "voice/monika/monika_ch10_156.ogg"
    m 2p "It was what you were to do. I knew it."
    voice "voice/monika/monika_ch10_157.ogg"
    m "But I wished we would continue that fake happiness,"
    voice "voice/monika/monika_ch10_158.ogg"
    m "A little longer..."
    show monika 1o
    mc "..."
    show expression "#000000a0" zorder 5
    "Now I know it. Now I know why Monika smiled sadly when I was back from Sayori's room."
    "She did nothing wrong. She just watched...what happened."
    "What I did."
    "Then she knew it started,and it couldn't be stopped either."
    hide expression "#000000a0"
    voice "voice/monika/monika_ch10_159.ogg"
    m 2i "All I did was untie the knot."
    voice "voice/monika/monika_ch10_160.ogg"
    m "I decided not to be against it at that time."
    voice "voice/monika/monika_ch10_161.ogg"
    m 1d "You know, the last knot is..."
    voice "voice/monika/monika_ch10_162.ogg"
    m 1e "ME."
    show monika 1e at thide
    hide monika
    "Okay, I know what I have to do now."
    "I grip her thin throat with my hands."
    window hide(None)
    scene white
    with Dissolve(1)
    window show(None)
    show monika 1c at face
    mc "Tell me,Monika."
    mc "Who am I?"
    mc "Am I just an ice cream shop guy, or a miserable girl in the facility?"
    voice "voice/monika/monika_ch10_163.ogg"
    m 1d "Both."
    voice "voice/monika/monika_ch10_164.ogg"
    m "But you are what you are."
    voice "voice/monika/monika_ch10_165.ogg"
    m "Maybe once you were one of the staff, who gave her Parfait Girls."
    voice "voice/monika/monika_ch10_166.ogg"
    m 1e "But nevermind."
    mc "..."
    voice "voice/monika/monika_ch10_167.ogg"
    m "You are going back to your reality."
    voice "voice/monika/monika_ch10_168.ogg"
    m "Even if there's no happiness at all, it's your reality."
    voice "voice/monika/monika_ch10_169.ogg"
    m 1q "Now you will be the one, and you will forget us."
    voice "voice/monika/monika_ch10_170.ogg"
    m 1e "Nor our Literature Club."
    show monika 1h
    mc "I won't..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch10_171.ogg"
    m 1a "You will. The game is over."
    show monika 1q
    "She closes her eyes."
    "I put my strength into arms and..."
    voice "voice/monika/monika_ch10_172.ogg"
    m 1k "Ah...I keep a promise to you...about...my...song..."
    window hide(None)
    python:
        renpy.call_screen("dialog", message="Wake up!", ok_action=Return())
    scene black
    $ persistent.clear[0] = True
    $ persistent.clear[1] = True
    $ persistent.clear[2] = True
    $ persistent.clear[3] = True
    $ persistent.clear[4] = True
    $ persistent.clear[5] = True
    $ persistent.clear[6] = True
    $ persistent.clear[7] = True
    $ persistent.clear[8] = True
    $ persistent.clear[9] = True
    $ renpy.save_persistent()
    pause 1.0
    if _preferences.language != None:
        if renpy.loadable("../characters/monika.chr") and renpy.loadable("../characters/sayori.chr") and renpy.loadable("../characters/yuri.chr") and renpy.loadable("../characters/natsuki.chr"):
            $ persistent.clearall = True
    if persistent.clearall == True:
        call specialend
    else:
        if not persistent.achievement[6]:
            $ renpy.notify(achievement_notify + achievement_name_7)
            $ persistent.achievement[6] = True
            play sound "tl/None/sfx/achievement.ogg"
        if ddmm_online and persistent.ddmm_achievement:
            $ ddmm_earn_achievement("THE_TRUTH")
        if persistent.chapter == False:
            return
        else:
            jump credits
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
