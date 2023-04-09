default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None
define mc_text = ""

image monika_back = "images/monika_back.png"

label ch7_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[6] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 7
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    stop music
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    scene black
    voice "voice/monika/monika_ch7_01.ogg"
    m "Uh,can you hear me?"
    voice "voice/monika/monika_ch7_02.ogg"
    m "...Is it working?"
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
    voice "voice/monika/monika_ch7_03.ogg"
    m "Yay, there you are!"
    voice "voice/monika/monika_ch7_04.ogg"
    m "Hi again,[player]."
    voice "voice/monika/monika_ch7_05.ogg"
    m "Um...welcome to the Literature Club!"
    voice "voice/monika/monika_ch7_06.ogg"
    m "Of course,we already know each other,because we were in the same class last year,and...um..."
    voice "voice/monika/monika_ch7_07.ogg"
    m "Ahaha..."
    m "..."
    voice "voice/monika/monika_ch7_08.ogg"
    m "Again. Welcome to the Literature Club."
    "Where...what...is here?"
    "As I once thought,am I still dreaming?"
    "I am now too tired to think about it."
    voice "voice/monika/monika_ch7_09.ogg"
    m "Hmm... you think you are in your dream,right?"
    voice "voice/monika/monika_ch7_10.ogg"
    m "Or this is the reality...which do you think is correct?"
    "Enough is Enough."
    "I don't understand what she says."
    menu:
        "Because this is..."
        "Just a Nightmare":
            stop music fadeout 1.0
            scene black
            with dissolve_scene_full
            $ monika_end = 1
            if persistent.chapter == True:
                call bad_monika_main
                call endgame
                return
            else:
                return
        "My reality.Accept it.":
            $ monika_end = 0
    show expression "#000000c0"
    "I glare at her."
    "I don't care which I'm in a dream or not anymore."
    "This is my reality as long as I'm trapped in this nightmare."
    "I will put an end to this mess."
    hide expression "#000000c0"
    voice "voice/monika/monika_ch7_11.ogg"
    m "Ooh [player]... you scare me."
    show expression "#000000c0"
    "I had a linkling as to it."
    "That she knew something."
    "When She said she knew the exchange among Sayori and me,"
    "I felt a chill down my spine. That was the answer."
    "She said she knew a lot more than I thought."
    "That means,she already knew that Sayori had gone away."
    "Even though she knew it...she let me go..."
    "When I was back,she smiled sadly."
    "I was back...because of...my temporary...amnesia..."
    "..."
    "Anyway,I was back. It made her disappointed."
    "Why? Was she disappointed with my serenity?"
    "Serenity...no. Now I rememver everything. Every moment I think of Sayori..."
    "It drives me really crazy."
    "You won,Monika. I am crazy as you intended."
    "I hold the fist with anger and sadness."
    hide expression "#000000c0"
    "Nevertheless,I control not to lost myself,and begin to talk quietly."
    mc "Tell me Monika,you knew that Sayori was dead at that time,didn't you?"
    m "..."
    mc "Don't tell me a lie. I just want to know everything."
    voice "voice/monika/monika_ch7_12.ogg"
    m "I knew...maybe. Yes,at least I knew it might be going to."




    if persistent.chapter == False:
        return
    else:
        call ch7_1_main

label ch7_1_main:
    show expression "#000000c0"
    "The anger in me disappeared befor I knew it."
    "Well,it doesn't completely but,"
    "More than that,I want to know the truth."
    "She said she knew it."
    "That Sayori was dead. Why did she know it?"
    "The answer is simple. She killed Sayori."
    "Monika killed Sayori."
    "..."
    "No doubt Sayori commited suicide. At least it seemed so."
    "Her rainclouds did't go away,either."
    "Still,I don't believe she committed it."
    "I believe she was forced to."
    "By Monika."
    "..."
    hide expression "#000000c0"
    mc "Monika,I don't understand."
    "I say quietly."
    mc "Why you did......that thing."
    voice "voice/monika/monika_ch7_13.ogg"
    m "That thing? I didn't do anything."
    "She says,smiling."
    show expression "#000000c0"
    "Yeah,you didn't."
    "You didn't get your hands dirty."
    "You just implanted something dirty into Sayori."
    "With smiling,as same as now."
    hide expression "#000000c0"
    mc "Thinking back of it,YOU left Yuri and me alone in the classroom."
    m "..."
    mc "She lost her mind suddenly,because someone inplanted something into her."
    mc "Someone who knows Yuri carries a knife with her and she might use it."
    show expression "#000000c0"
    "I stop talking and watch her."
    "She's smirking as always."
    "YOU GODDAMN BASTARD !"
    hide expression "#000000c0"
    mc "Natsuki...yes,she..."
    mc "She was back alone,though she went out with YOU."
    mc "Because you,you planned it."
    mc "She said something random,it was also because of your..."
    show expression "#000000c0"
    "I talk on and on,fast and furious."
    "But Monika doesn't turn her face pale or anything."
    "My anger rises up again."
    hide expression "#000000c0"
    mc "Monika,you..."
    mc "You've done it all? You've..."
    mc "Killed them all !?"
    "I scream. I can't stand it anymore."
    m "..."
    mc "Say,say something to me! You..."
    menu:
        "You did it all.":
            if persistent.gamepad:
                if persistent.change_buttons:
                    $ config.pad_bindings["pad_a_press"] = [ ]
                else:
                    $ config.pad_bindings["pad_b_press"] = [ ]
            $ quick_menu_limit = True
            stop music fadeout 1.0
            window hide(None)
            $ persistent.autoload = "normal_end"
            pause 1.0
            $ consolehistory = []
            call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
            $ delete_character("monika")
            pause 1.0
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            $ pause(1.5)
            call normal_end
            return
        "OK,I listen to you.":
            $ normal_end = 0
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    if persistent.chapter == False:
        return
    else:
        call ch8_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
