label bad_natsuki_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[12] = True
    if persistent.chapter == True:
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 13
        $ style.say_dialogue = style.normal
        $ quick_menu = True
        scene black
        stop music
    pause 1.0
    "..."
    "...Ah."
    "Where...am I?"
    "I open my eyes slowly"
    scene bg bedroom
    show expression "#000000b0"
    with dissolve_scene_full
    "My...room?"
    scene bg bedroom
    with open_eyes
    show natsuki 4c at face
    mc "..."
    play music t5n
    n "..."
    mc "..."
    n "..."
    show natsuki 4p
    mc "...WOW!"
    voice "voice/natsuki/natsuki_bad_01.ogg"
    n 5y "Jeez..."
    mc "W-w-why are you here?"
    voice "voice/natsuki/natsuki_bad_02.ogg"
    n 5e "Huh? You don't remember what you said?"
    mc "D...did I?"
    voice "voice/natsuki/natsuki_bad_03.ogg"
    n "You told us to come to wake you up,that it'd fatal if you'd oversleep."
    voice "voice/natsuki/natsuki_bad_04.ogg"
    n 5u "I-I came here NOT for you, just because everyone looked so busy but me..."
    "..."
    "...Ha ha."
    "I'm back. Back to the reality."
    "No more nightmares. Nevermore."
    voice "voice/natsuki/natsuki_bad_05.ogg"
    n 4c "[player]...are you OK?"
    "I stared at her eyes...and I hold her gently."
    voice "voice/natsuki/natsuki_bad_06.ogg"
    n 1v "W-what...what are you...PERVERT...!"
    mc "Thank you Natsuki. Thank you very much. You saved me."
    n 1m "[player]..."
    "That nightmare ended."
    "Now I'm back to the usual life."
    "Dull,boring...but sometimes happy. My usual life."
    show natsuki 12d
    stop music fadeout 1.0
    "..."
    mc "Natsuki?"
    voice "voice/natsuki/natsuki_bad_07.ogg"
    n 12f "NO."
    "Eh."
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ ]
    play music t4g
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
    pause 4
    if not persistent.achievement[2]:
        stop music fadeout 2.0
        scene black
        with dissolve_scene_full
        $ renpy.notify(achievement_notify + achievement_name_3)
        $ persistent.achievement[2] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 2.0
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_earn_achievement("BAD_NATSUKI")
    if persistent.chapter == False:
        return
    else:
        call endgame
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
