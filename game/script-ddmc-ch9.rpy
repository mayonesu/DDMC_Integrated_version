label ch9_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[8] = True
    if persistent.chapter == True:
        window hide(None)
        scene black
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 9
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    if not persistent.save_graphic:
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
    else:
        show monika_back
    show monika_bg
    if not persistent.save_graphic:
        show monika_bg_highlight
    play music m1
    voice "voice/monika/monika_ch9_01.ogg"
    m "What is the reality for you,[player]?"
    mc "W-well,reality is reality,isn't it? But..."
    mc "I don't know whether this is my dream or the reality now,I just decided to accept that this is the reality."
    voice "voice/monika/monika_ch9_02.ogg"
    m "Bingo!"
    "She smiles."
    voice "voice/monika/monika_ch9_03.ogg"
    m "Your reality,my reality. They might be different."
    voice "voice/monika/monika_ch9_04.ogg"
    m "Have you thought like that before?"
    mc "What do you mean?"
    voice "voice/monika/monika_ch9_05.ogg"
    m "You see your reality as you want to see,while I see my reality as I want to see,too."
    voice "voice/monika/monika_ch9_06.ogg"
    m "Someone sees his reality as that."
    voice "voice/monika/monika_ch9_07.ogg"
    m "They are all different. But they are all true. At the same time,they are all fake."
    mc "..."
    "What in the world is she talking about?"
    voice "voice/monika/monika_ch9_08.ogg"
    m "Reality is possibility,chosen unconciously from the infinite numbers of possibilities."
    voice "voice/monika/monika_ch9_09.ogg"
    m "We call it reality. The chosen one. We choose and choose and choose...and so on."
    mc "W-wait...I...I don't underst..."
    voice "voice/monika/monika_ch9_10.ogg"
    m "Monika's last tip of the day. Number 3."
    voice "voice/monika/monika_ch9_11.ogg"
    m "'3.Don't bother Monika till she finishes the story.'"
    mc "..."
    voice "voice/monika/monika_ch9_12.ogg"
    m "Everyone has his own reality. That's the way it is."
    voice "voice/monika/monika_ch9_13.ogg"
    m "Each reality is almost the same,but sometimes..."
    voice "voice/monika/monika_ch9_14.ogg"
    m "very different."
    m "..."
    voice "voice/monika/monika_ch9_15.ogg"
    m "It makes much easier that you see it."
    if renpy.windows and _preferences.language != None and not ("steamapps" in config.basedir.lower()):
        python:
            open(config.basedir + "/monika.vbs", "w").write(renpy.file("monika.vbs").read())
            import os
            import subprocess
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            cmd = "cscript " + config.basedir + "\\monika.vbs"
            subprocess.call(cmd, startupinfo=si)
            os.unlink(config.basedir + "/monika.vbs")
    else:
        $ renpy.call_screen("dialog", message="Okay everyone?", ok_action=Return())
    window hide(None)
    stop music fadeout 1.0
    pause 0.5
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    pause 2.0
    show layer master
    show layer screens
    hide monika_scare
    scene black
    with dissolve_scene_full
    window show(None)
    "Wha..."
    "What...was...it...?"
    voice "voice/monika/monika_ch9_16.ogg"
    m "Sorry. I didn't plan to scare you..."
    if not persistent.save_graphic:
        show mask_2
        show mask_3
        show room_mask as rm:
            size (320,180)
            pos (30,200)
        show room_mask2 as rm2:
            size (320,180)
            pos (935,200)
    else:
        show monika_back
    show monika_bg
    if not persistent.save_graphic:
        show monika_bg_highlight
    play music m1
    voice "voice/monika/monika_ch9_17.ogg"
    m "You saw one of the possibilities. It might be real,or not. But if you think you saw it,you accept it as your reality."
    voice "voice/monika/monika_ch9_18.ogg"
    m "Reality has many faces. The reality you saw is not the only one. Only the reality you saw might be very different from the other realities."
    mc "..."
    voice "voice/monika/monika_ch9_19.ogg"
    m "Is it meaningless to you? But it's important. Very important for the story I'm going to tell."
    stop music fadeout 1.0
    m "..."
    voice "voice/monika/monika_ch9_20.ogg"
    m "Sayori,Yuri and Natsuki...their last moments you saw. They were..."
    voice "voice/monika/monika_ch9_21.ogg"
    m "They were what you chose. They were what you wanted to see."
    voice "voice/monika/monika_ch9_22.ogg"
    m "And they were...very different from the others."
    window hide(None)
    scene black
    with dissolve_scene_full
    if persistent.chapter == False:
        return
    else:
        call ch9_1_main

label ch9_1_main:
    play music t10
    show monika 1i at t11
    voice "voice/monika/monika_ch9_23.ogg"
    m "We are going to look back your 'reality' one by one..."
    voice "voice/monika/monika_ch9_24.ogg"
    m 1h "But it may hurt you so much."
    voice "voice/monika/monika_ch9_25.ogg"
    m 1r "I'm very sorry. However,get hold of youself,I'm alway by your side."
    m 1h "..."
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    pause 1.0
    play music td
    show expression "images/cg/monika/monika_room.png"
    show expression "images/cg/s_kill_bg2.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    show expression "#00000060":
        zoom 0.5 xalign 0.2 yalign 0.3
    show monika 3h at t44
    mc "Wha...!"
    mc "It...is..."
    voice "voice/monika/monika_ch9_26.ogg"
    m 3i "Yes,it's the place you saw Sayori the last time."
    show monika 3h
    mc "W...why..."
    voice "voice/monika/monika_ch9_27.ogg"
    m 1p "Well,I'm...The One Who Watches."
    mc "Eh?"
    voice "voice/monika/monika_ch9_28.ogg"
    m 1r "Nevermind for now."
    m "..."
    voice "voice/monika/monika_ch9_29.ogg"
    m 1i "In this room, you found her noose..."
    show monika 3h
    stop music fadeout 1.0
    "She points her forefinger. What is she going to..."
    show monika 3i
    mc "STOP IT!"
    play music t10
    voice "voice/monika/monika_ch9_30.ogg"
    m 1i "...Okay."
    voice "voice/monika/monika_ch9_31.ogg"
    m 1h "You found her in this room,right?"
    mc "...Yes."
    voice "voice/monika/monika_ch9_32.ogg"
    m 1i "I don't ask you what you thought or you felt."
    voice "voice/monika/monika_ch9_33.ogg"
    m 1r "Because that's not what I can see."
    voice "voice/monika/monika_ch9_34.ogg"
    m 1q "I didn't know what Sayori thought or felt,either."
    voice "voice/monika/monika_ch9_35.ogg"
    m 1h "You said...that I should know what happened to her,didn't you?"
    mc "Yes...I did."
    voice "voice/monika/monika_ch9_36.ogg"
    m 1i "Do you think so even now?"
    mc "I don't know...but I'm sure you knew something."
    voice "voice/monika/monika_ch9_37.ogg"
    m 1r "...I knew. Roughly."
    voice "voice/monika/monika_ch9_38.ogg"
    m 1i "I'll show you...all I know."
    show monika 1i zorder 1 at thide
    hide monika
    hide expression "images/cg/s_kill_bg2.png"
    hide expression "#00000060"
    pause 1.0
    if persistent.chapter == False:
        return
    else:
        call ch9_2_main

label ch9_2_main:
    show expression "images/cg/monika/monika_room.png"
    show expression "images/cg/s_kill_bg.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    with dissolve
    show monika 2i at t44
    voice "voice/monika/monika_ch9_39.ogg"
    m "When you entered her room,"
    voice "voice/monika/monika_ch9_40.ogg"
    m "She was going to commit it."
    voice "voice/monika/monika_ch9_41.ogg"
    m 2q "But she hesitated to do it..."
    show expression "#000000a0"
    "What...? What did she say now?"
    "'Going to'...? 'Hesitated to'...?"
    hide expression "#000000a0"
    voice "voice/monika/monika_ch9_42.ogg"
    m 2i "And she saw you. Of course,she got astonished."
    voice "voice/monika/monika_ch9_43.ogg"
    m "She mumbled something to you,but you..."
    show monika 2h
    show expression "#000000a0"
    stop music
    mc "S-STOP IT! WHAT THE HELL ARE YOU TALKING ABOUT? S-she was already d-d-dead,h-h-hung from the ceiling,when I entered the roo..."
    hide expression "#000000a0"
    play music t10
    voice "voice/monika/monika_ch9_44.ogg"
    m 2i "It was what you wanted to see."
    voice "voice/monika/monika_ch9_45.ogg"
    m 2o "Your...reality."
    voice "voice/monika/monika_ch9_46.ogg"
    m 2p "Anyway,"
    show monika 2o
    stop music
    mc "I SAID STOP IT!"
    mc "S-she was hung when I entered the room and I saw her so I thought I had to carriy her body it was cold yet to the bed and she was already dead and quiet like she was sleeping so I thought she was sleeping but she won't wake up and I wondered if I could wake her up or not but I didn't know how or why so I looked into her face she was so calm but I..."
    play music t10
    voice "voice/monika/monika_ch9_47.ogg"
    m 2q "...Anyway."
    voice "voice/monika/monika_ch9_48.ogg"
    m 3i "How did you carry her body to the bed when she was hung from the ceiling,by youself alone?"
    voice "voice/monika/monika_ch9_49.ogg"
    m "Or how did you untie the noose from the ceiling, with someone's body was hung?"
    voice "voice/monika/monika_ch9_50.ogg"
    m "I think it's not so easy for a thin man like you."
    show monika 1h
    "Wha...what did she say now?"
    stop music
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    "I remember that I hold her...my both hands remember her weight..."
    "But I...how did I untie the noose? Surely it wasn't poissible if I didn't untie it but"
    "I-I don't remember. I don't. I don't."
    play music t10
    voice "voice/monika/monika_ch9_51.ogg"
    m 2i "What I know is that..."
    m 1p "..."
    voice "voice/monika/monika_ch9_52.ogg"
    m 1r "You hold her tight,like you wanted to stop her from committing it..."
    voice "voice/monika/monika_ch9_53.ogg"
    m 1o "...At least it seemed so."
    voice "voice/monika/monika_ch9_54.ogg"
    m 1i "Then you carried her to the bed,put her there,and..."
    m 1q "..."
    voice "voice/monika/monika_ch9_55.ogg"
    m 1o "Well..."
    voice "voice/monika/monika_ch9_56.ogg"
    m 1r "You gripped her throat..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch9_57.ogg"
    m 1q "To death."
    show expression "#000000a0"
    "..."
    "......"
    "...Eh?"
    "Did I do...what?"
    "I...killed...Sayori?"
    hide expression "#000000a0"
    voice "voice/monika/monika_ch9_58.ogg"
    m 3h "Tip 1. You don't have to believe Monika's story."
    voice "voice/monika/monika_ch9_59.ogg"
    m "Tip 2. Monika doesn't tell a lie to you."
    show expression "#000000a0"
    "I...I didn't do it."
    "But I don't remember partly what I did."
    "I didn't. I didn't. "
    "But my memory can't explain what happened there which I remember."
    hide expression "#000000a0"
    show monika 2i
    mc "I -I don't trust you."
    mc "But...I can't trust myself,either..."
    mc "Go on...please."
    voice "voice/monika/monika_ch9_60.ogg"
    m 2e "Okay. You obey the tip number 3,don't you?"
    stop music fadeout 1.0
    hide expression "images/cg/s_kill_bg.png"
    with dissolve
    if persistent.chapter == False:
        return
    else:
        call ch9_3_main

label ch9_3_main:
    show expression "images/cg/monika/monika_room.png"
    show expression "images/cg/y_kill/1a.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    show expression "#00000050":
        zoom 0.5 xalign 0.2 yalign 0.3
    play music "<loop 4.444>bgm/5_yuri2.ogg"
    show monika 3h
    m 3h "..."
    hide expression "#00000050"
    hide expression "images/cg/y_kill/1a.png"
    show expression "#000000a0"
    show expression "images/cg/y_kill/1a.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    "That is...Yuri."
    "I want to turn away from it,but..."
    show monika 1h
    "Don't. I have to know the truth."
    hide expression "#000000a0"
    mc "You may want to say that..."
    mc "I also killed her."
    mc "...don't you?"
    m "..."
    show expression "#000000a0"
    "She keeps silent."
    "I don't remeber what happend then."
    "When I realized that..."
    hide expression "#000000a0"
    show monika 1i
    mc "She lost her mind suddenly and..."
    mc "She took out a knife..."
    mc "I tried to stop her..."
    mc "..."
    mc "Did I...did I stab her?"
    show monika 1h
    "She nods."
    mc "I-I...didn't intend to..."
    mc "I just wanted to stop her...but accidentally..."
    stop music fadeout 1.0
    show monika 1o
    stop music fadeout 1.0
    "Monika shakes her head quietly."
    mc "...Eh?"
    voice "voice/monika/monika_ch9_61.ogg"
    m 1r "She confessed to you."
    mc "Yes,maybe. Then she suddenly..."
    voice "voice/monika/monika_ch9_62.ogg"
    m 1i "She just consessed to you gently."
    voice "voice/monika/monika_ch9_63.ogg"
    m "She...she didn't lost her mind...until her last moment."
    show monika 1h
    mc "What do you..."
    hide expression "images/cg/y_kill/1a.png"
    show expression "#000000a0"
    show expression "images/cg/y_kill/1a.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    voice "voice/monika/monika_ch9_64.ogg"
    m 1i "You once said that she loved knives,right?"
    show monika 1h
    mc "Y-yeah......"
    voice "voice/monika/monika_ch9_65.ogg"
    m 1i "I knew it,too. I also knew that she sometimes carried a knife with her."
    voice "voice/monika/monika_ch9_66.ogg"
    m 2h "Her favorite knife."
    voice "voice/monika/monika_ch9_67.ogg"
    m 3i "But not an ordinary kitchen knife."
    hide expression "images/cg/y_kill/1a.png"
    hide expression "#000000a0"
    show expression "images/cg/y_kill/1a.png":
        zoom 0.5 xalign 0.2 yalign 0.3
    show expression "#000000a0"
    show monika 1h
    play music "<loop 4.444>bgm/5_yuri2.ogg"
    "...Wait."
    "She had a...kitchen knife?"
    hide expression "#000000a0"
    voice "voice/monika/monika_ch9_68.ogg"
    m 1i "She was stabbed with a kitchen knife."
    voice "voice/monika/monika_ch9_69.ogg"
    m "Not with her own knife."
    show monika 1h
    mc "..."
    voice "voice/monika/monika_ch9_70.ogg"
    m 1i "You know the knife,right?"
    show monika 1h
    mc "Argh...!"
    show expression "#000000a0"
    "My...kitchen knife."
    "Why...?"
    hide expression "#000000a0"
    mc "Why did she have it?"
    voice "voice/monika/monika_ch9_71.ogg"
    m 2i "No..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch9_72.ogg"
    m "YOU had it."
    show monika 2h
    "Huh?"
    voice "voice/monika/monika_ch9_73.ogg"
    m 1i "You carried it there."
    voice "voice/monika/monika_ch9_74.ogg"
    m "You picked it up from the kitchen in that morning."
    voice "voice/monika/monika_ch9_75.ogg"
    m "And you put it in your bag."
    show monika 1h
    mc "..."
    voice "voice/monika/monika_ch9_76.ogg"
    m 1p "She didn't lose her mind."
    voice "voice/monika/monika_ch9_77.ogg"
    m "She didn't take out her knife,either."
    voice "voice/monika/monika_ch9_78.ogg"
    m "Even she didn't tried to scare you or anything."
    voice "voice/monika/monika_ch9_79.ogg"
    m "If you thought you saw her madness..."
    play music "<loop 4.444>bgm/5_yuri2.ogg"
    voice "voice/monika/monika_ch9_80.ogg"
    m 1r "It was YOUR reality."
    show monika 1q
    mc "My...reality..."
    voice "voice/monika/monika_ch9_81.ogg"
    m 1i "Can I go on?"
    show monika 1h
    mc "...Yes."
    stop music fadeout 1.0
    if persistent.chapter == False:
        return
    else:
        call ch9_4_main

label ch9_4_main:
    hide expression "images/cg/y_kill/1a.png"
    show expression "images/cg/monika/monika_room.png"
    show expression "bg/rooftop.jpg":
        zoom 0.5 xalign 0.2 yalign 0.3
    show expression "#00000050":
        zoom 0.5 xalign 0.2 yalign 0.3
    with dissolve
    play music "<loop 10.893>bgm/6o.ogg"
    show monika 3h at t44
    m "..."
    hide expression "#00000050"
    hide expression "bg/rooftop.jpg"
    show expression "#000000a0"
    show expression "bg/rooftop.jpg":
        zoom 0.5 xalign 0.2 yalign 0.3
    "Yes,I know where."
    "It's the rooftop."
    hide expression "#000000a0"
    show monika 1h
    hide expression "bg/rooftop.jpg"
    hide expression "#000000a0"
    show expression "bg/rooftop.jpg":
        zoom 0.5 xalign 0.2 yalign 0.3
    mc "OK,let me tell you."
    mc "You want to say that"
    mc "I killed Natsuki,too,huh?"
    voice "voice/monika/monika_ch9_82.ogg"
    m 1i "...Kind of."
    show monika 1h
    mc "I saw her jumped off the rooftop."
    mc "At least I think I saw it,but"
    mc "You say it was MY reality,right?"
    mc "Like,I threw her off the rooftop or something..."
    stop music fadeout 1.0
    voice "voice/monika/monika_ch9_83.ogg"
    m 1i "No."
    show monika 1h
    mc "Huh?"
    play music "<loop 10.893>bgm/6s.ogg"
    voice "voice/monika/monika_ch9_84.ogg"
    m 1i "Like you said,she didn't jump off."
    voice "voice/monika/monika_ch9_85.ogg"
    m 2i "The fences are too high to climb for her."
    voice "voice/monika/monika_ch9_86.ogg"
    m 2h "It was impossible. Either..."
    voice "voice/monika/monika_ch9_87.ogg"
    m "You couldn't throw her off by yourself alone."
    voice "voice/monika/monika_ch9_88.ogg"
    m 2i "Do you really think you can?"
    show monika 2h
    mc "Um..."
    stop music fadeout 1.0
    hide expression "bg/rooftop.jpg"
    show expression "#000000a0"
    show expression "bg/rooftop.jpg":
        zoom 0.5 xalign 0.2 yalign 0.3
    voice "voice/monika/monika_ch9_89.ogg"
    m 1i "I think she's there yet."
    show monika 1h
    mc "What? Is she alive?"
    voice "voice/monika/monika_ch9_90.ogg"
    m 1p "W-well...I didn't mean it..."
    voice "voice/monika/monika_ch9_91.ogg"
    m "She's...not. Because you strangled her there."
    show monika 1o
    hide expression "bg/rooftop.jpg"
    hide expression "#000000a0"
    show expression "bg/rooftop.jpg":
        zoom 0.5 xalign 0.2 yalign 0.3
    show expression "#000000a0"
    "...Oh."
    "...God."
    "The story she told me sounds consistent."
    "But..."
    "Why? Why can't I recall anything?"
    show monika 1r
    "She closes her eyes."
    "Is it..is it really THE TRUTH I wanted to know?"
    "I..."
    if renpy.random.randint(0,1) == 0:
        python:
            madechoice = renpy.display_menu([("I am the serial killer.","true_end"),("I don't believe it.","normal_end")], screen="rigged_choice")
        if madechoice == "true_end":
            $ persistent.normal_end = 0
            stop music fadeout 1.0
            scene black
            with dissolve_scene_full
        else:
            stop music
            call ch9_5_main
    else:
        menu:
            "I am the serial killer.":
                $ persistent.normal_end = 0
                stop music fadeout 1.0
                scene black
                with dissolve_scene_full
            "I don't believe it.":
                stop music
                call ch9_5_main
    if persistent.chapter == False:
        return
    else:
        call ch10_main

label ch9_5_main:
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ ]
    $ quick_menu_limit = True
    hide expression "bg/rooftop.jpg"
    show monika 1q at t11
    show expression "#000000a0"
    play music m1
    "I don't believe it."
    "I didn't kill anyone."
    "In token of that,I can't recall what she told me even now."
    "Don't trust Monika."
    show monika 1h
    hide expression "#000000a0"
    mc "Now I know clearly."
    mc "You are a liar."
    m 1a "..."
    show expression "#000000a0"
    "She doesn't say a thing."
    "On the contrary,she smiles."
    hide expression "#000000a0"
    mc "You tried to implant me the wrong thought."
    mc "Like...you did to others."
    mc "I'm not a fool."
    mc "Don't underestimate me."
    mc "Yeah,I'm NOT the killer,either."
    mc "But now...I can be the killer."
    show monika 1c
    show expression "#000000a0"
    "Anger,grief and something I can't explain."
    "The mixed emotion is controlling me."
    show monika 1d
    hide expression "#000000a0"
    mc "YOU killed them all."
    mc "I don't know how or why exactly,but you did."
    mc "I...I don't want to lose you. Because now I have nothing without you."
    mc "But more than that, I can't forgive you!"
    show monika 1d at face
    "I jump to her. I grip her throat."
    show monika 1a
    "She doesn't seem to be shocked. She just stares me in the eyes."
    "...with smiling."
    mc "Tell me...why did you do it?"
    voice "voice/monika/monika_ch9_92.ogg"
    m 1i "I did nothing."
    voice "voice/monika/monika_ch9_93.ogg"
    m 1r "All I did was untie the knot."
    show monika 1q
    "She closes her eyes."
    "I put my strength into arms and..."
    "..."
    if renpy.variant("pc"):
        $ persistent.autoload = "normal_end2_2"
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")
    pause 1.0
    call hideconsole
    stop music fadeout 1.0
    scene white with dissolve
    hide monika
    "At the moment, the room got white out."
    "I can't see anything."
    "..."
    "Some random memories is flashing back to me."
    "What...am I going to die?"
    "..."
    show sayori 4u at face
    "I see Sayori's face..."
    "Her eyes were filled with fear..."
    "...And I was gripping her throat."
    call updateconsole ("os.remove(\"characters/sayori.chr\")", "sayori.chr deleted successfully.")
    $ delete_character("sayori")
    pause 1.0
    call hideconsole
    show sayori 4u at thide
    hide sayori
    pause 1.0
    show yuri 3p at face
    "Yuri...with an astonished look..."
    "...I was sticking my kitchen knife into her."
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    pause 1.0
    call hideconsole
    show yuri 3p at thide
    hide yuri
    pause 1.0
    show natsuki 12f at face
    "Natsuki...please don't cry..."
    "...Her thin neck...I..."
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    pause 1.0
    show natsuki 12f at thide
    hide natsuki
    pause 1.0
    call hideconsole
    "NOW I RECALL THEM ALL."
    scene white with dissolve
    pause 1.0
    call normal_end2_2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
