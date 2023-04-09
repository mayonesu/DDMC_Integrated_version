label bad_yuri_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[11] = True
    if persistent.chapter == True:
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 12
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
    show yuri 1f at face
    mc "..."
    play music t5y
    y "..."
    mc "..."
    y "..."
    mc "...WOW!"
    voice "voice/yuri/yuri_bad_01.ogg"
    y 1p "Eek!"
    mc "W-w-why are you here?"
    voice "voice/yuri/yuri_bad_02.ogg"
    y 4c "I'm sorry! You told me that you wanted me to pick you up,so..."
    mc "D...did I?"
    voice "voice/yuri/yuri_bad_03.ogg"
    y "In my texts...I sent you if you needed my help,then you returned OK,so I just thought..."
    voice "voice/yuri/yuri_bad_04.ogg"
    y "But,but! What a shame that I invaded your room like an idiot..."
    "..."
    "...Ha ha."
    "I'm back. Back to the reality."
    "No more nightmares. Nevermore."
    voice "voice/yuri/yuri_bad_05.ogg"
    y 3e "[player]...are you OK?"
    "I stared at her eyes...and I hold her gently."
    y 3n "...!!"
    mc "Thank you Yuri. Thank you very much. You saved me."
    y 3m "[player]..."
    "That nightmare ended."
    "Now I'm back to the usual life."
    "Dull,boring...but sometimes happy. My usual life."
    show yuri 3l
    stop music fadeout 1.0
    "..."
    mc "Yuri?"
    voice "voice/yuri/yuri_bad_06.ogg"
    y 1b "I am sorry."
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
    if not persistent.achievement[1]:
        stop music fadeout 2.0
        scene black
        with dissolve_scene_full
        $ renpy.notify(achievement_notify + achievement_name_2)
        $ persistent.achievement[1] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 2.0
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_earn_achievement("BAD_YURI")
    if persistent.chapter == False:
        return
    else:
        call endgame
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
