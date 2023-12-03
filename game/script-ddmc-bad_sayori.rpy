label bad_sayori_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[10] = True
    if persistent.chapter == True:
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 11
        $ style.say_dialogue = style.normal
        $ quick_menu = True
        scene black
        stop music
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
    show sayori 1c at face
    mc "..."
    play music t5s
    s "..."
    mc "..."
    s "..."
    show sayori 4m
    mc "...WOW!"
    voice "voice/sayori/sayori_bad_01.ogg"
    s 4n "Sur...prised."
    mc "W-w-why are you here?"
    voice "voice/sayori/sayori_bad_02.ogg"
    s 4o "How dare you say WHY? You called me here!"
    mc "D...did I?"
    voice "voice/sayori/sayori_bad_03.ogg"
    s "You told me to wake you up,that it'd fatal if you'd oversleep."
    voice "voice/sayori/sayori_bad_04.ogg"
    s "Yesterday. So I'm here because you didn't answer my phone."
    "..."
    "...Ha ha."
    "I'm back. Back to the reality."
    "No more nightmares. Nevermore."
    voice "voice/sayori/sayori_bad_05.ogg"
    s 4j "[player]...are you OK?"
    "I stared at her eyes...and I hold her gently."
    voice "voice/sayori/sayori_bad_06.ogg"
    s 4m "W-what...what are you...suddenly..."
    mc "Thank you Sayori. Thank you very much. You saved me."
    s 4e "[player]..."
    "That nightmare ended."
    "Now I'm back to the usual life."
    "Dull,boring...but sometimes happy. My usual life."
    show sayori 4u
    stop music fadeout 1.0
    "..."
    mc "Sayori?"
    voice "voice/sayori/sayori_bad_07.ogg"
    s 4w "Impossible."
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
    if not persistent.achievement[0]:
        stop music fadeout 2.0
        scene black
        with dissolve_scene_full
        $ renpy.notify(achievement_notify + achievement_name_1)
        $ persistent.achievement[0] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 2.0
    if persistent.chapter == False:
        return
    else:
        call endgame
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
