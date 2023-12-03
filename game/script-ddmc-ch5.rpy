label ch5_1_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[4] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 5
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    if not persistent.chapter and persistent.autosave_mode:
        $ renpy.save('autosave')
        $ renpy.notify('autosaved.')
    scene bg club_day2
    with wipeleft_scene
    play music t5
    show yuri 1f zorder 2 at t11
    voice "voice/yuri/yuri_ch5_01.ogg"
    y "Oh,[player]..."
    show yuri 1f zorder 2 at t22
    show natsuki 1b zorder 2 at t21
    voice "voice/natsuki/natsuki_ch5_01.ogg"
    n "You're too late!"
    voice "voice/natsuki/natsuki_ch5_02.ogg"
    n 3e "We prepared all the decorations for this festival without you!"
    voice "voice/yuri/yuri_ch5_02.ogg"
    y 2c "But [player] helped it yesterday,so it was not so hard to prepare..."
    show yuri 2e
    voice "voice/natsuki/natsuki_ch5_03.ogg"
    n 5y "He helped YOU,but I baked all these damn cakes by myself alone!"
    voice "voice/natsuki/natsuki_ch5_04.ogg"
    n 5w "Do you know how hard it was?"
    voice "voice/natsuki/natsuki_ch5_05.ogg"
    n 5x "I had to go shopping again to buy ingredients because it got run out,besides dad called me while I was baking..."
    voice "voice/yuri/yuri_ch5_03.ogg"
    y 1d "Yes,you worked very hard,and here come cute cupcakes! They look so delicious!"
    voice "voice/natsuki/natsuki_ch5_06.ogg"
    n 1k "No,no,don't steal a teste like Sayori!"
    show yuri 1f
    voice "voice/natsuki/natsuki_ch5_07.ogg"
    n 1p "...Wait. Where is she? Aren't you with her?"
    mc "Yeah...she...she might be late."
    voice "voice/yuri/yuri_ch5_04.ogg"
    y "Y-you mean that she overslept?"
    voice "voice/natsuki/natsuki_ch5_08.ogg"
    n 5w "Jeez,she did it again? I can't believe!"
    show natsuki 5h
    mc "Yes,but...umm,I think she...she feels kind of sick."
    voice "voice/yuri/yuri_ch5_05.ogg"
    y 2f "Well,so she doesn't come to school today,does she?"
    mc "Maybe."
    voice "voice/yuri/yuri_ch5_06.ogg"
    y 1g "Ah,that reminds me yesterday she looked..."
    "Yuri hesitates."
    voice "voice/yuri/yuri_ch5_07.ogg"
    y "Well...it cannot be helped."
    voice "voice/natsuki/natsuki_ch5_09.ogg"
    n 1m "Do you know something on her,Yuri?"
    voice "voice/yuri/yuri_ch5_08.ogg"
    y 2n "N-no,but I remember that she looked a bit down these days..."
    voice "voice/yuri/yuri_ch5_09.ogg"
    y 2s "But, we four can do it if she isn't here."
    voice "voice/natsuki/natsuki_ch5_10.ogg"
    n 4y "Come on! Why can you be so carefree?"
    voice "voice/yuri/yuri_ch5_10.ogg"
    y 1t "Eh....?"
    voice "voice/natsuki/natsuki_ch5_11.ogg"
    n 5y "Who takes Sayori's part of reciting? Do you want to try it?"
    voice "voice/yuri/yuri_ch5_11.ogg"
    y 3p "Oh...my goddess...it's...uh...well,what can I do...?"
    show yuri 3p zorder 2 at t33
    show natsuki 5k zorder 2 at t32
    show monika 3b zorder 2 at t31
    voice "voice/monika/monika_ch5_01.ogg"
    m "Don't worry,Yuri. The president takes the part."
    "Monika's back. Good timing."
    voice "voice/natsuki/natsuki_ch5_12.ogg"
    n 1e "Monika! Did you hear? Of Sayori!"
    show monika 1h
    "She nods."
    show natsuki 1c
    voice "voice/yuri/yuri_ch5_12.ogg"
    y 1a "What a relief we have our president Monika,but..."
    voice "voice/yuri/yuri_ch5_13.ogg"
    y 1g "Without Sayori,I cant help but feel helpless a bit..."
    show natsuki 1n
    "So says Yuri, and it makes Natsuki look nervous."
    voice "voice/natsuki/natsuki_ch5_13.ogg"
    n 1q "Monika... what should we do? We might be in trouble..."
    "Monika keeps silent."
    mc "Monika..."
    if persistent.chapter == False:
        return
    else:
        call ch5_2_main

label ch5_2_main:
    show natsuki 1n
    show yuri 1n
    show monika 1a
    "She lifts her face and smiles gently to Natsuki."
    show yuri 3f
    show natsuki 1k
    voice "voice/monika/monika_ch5_02.ogg"
    m 3a "Natsuki,your cupcakes are my favorite. "
    voice "voice/monika/monika_ch5_03.ogg"
    m 3j "I love sweets,especially your cupcakes. I'm a big fan of you,Natsuki."
    voice "voice/monika/monika_ch5_04.ogg"
    m "You worked so hard,you know? I'm looking forward to them. Thank you."
    show monika 1j
    voice "voice/natsuki/natsuki_ch5_14.ogg"
    n 4t "You compliment it so much...b-but I'm going to share them equally!"
    "Yes,Natsuki is back to her usual tone now."
    "Then Monika turns her face to Yuri."
    show yuri 1f
    show natsuki 1k
    voice "voice/monika/monika_ch5_05.ogg"
    m 3a "Yuri,this incence is...lavender,right?"
    show natsuki 1j
    voice "voice/yuri/yuri_ch5_14.ogg"
    y 1e "Eh...s-sure..."
    voice "voice/monika/monika_ch5_06.ogg"
    m 1j "Very nice fragrant...it really soothes me."
    voice "voice/monika/monika_ch5_07.ogg"
    m 1r "You once said that you like kind of incense. I'm glad I left decorations to you.Thank you."
    show natsuki 1l
    show monika 1a
    voice "voice/yuri/yuri_ch5_15.ogg"
    y 1s "Y-you're welcome..."
    "She looks calm and smiles back shyly."
    show yuri 1e
    show natsuki 1k
    voice "voice/monika/monika_ch5_08.ogg"
    m 3b "We've prepared them almost perfect. You don't have to worry,right?"
    show monika 1a
    "Jeez, no comments for me..."
    voice "voice/monika/monika_ch5_09.ogg"
    m 3j "[player], you agree?"
    mc "T-t-totally."
    show yuri 1d
    show natsuki 4z
    show monika 3k
    "I get embarassed that she brings up a topic to me suddenly. They laugh cheerfully."
    show yuri 1a
    show natsuki 4l
    voice "voice/monika/monika_ch5_10.ogg"
    m 3a "Okay everyone! We've got enough time before our opening. We can enjoy the festival,both for each of us and for Sayori. She also looked forward to it."
    show yuri 1f
    show natsuki 4k
    voice "voice/monika/monika_ch5_11.ogg"
    m 5a "We will gather here an hour after,OK? I'm going to hunt a fried squid...Natsuki's today's game~!"
    voice "voice/natsuki/natsuki_ch5_15.ogg"
    n 4w "Jeez,you say I am such greedy?"
    show yuri 1c
    show natsuki 4z
    voice "voice/monika/monika_ch5_12.ogg"
    m 1a "Aren't you? Ahaha~"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    stop music fadeout 1.0
    "They step out the classroom chatting each other."
    if persistent.chapter == False:
        return
    else:
        call ch6_1_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
