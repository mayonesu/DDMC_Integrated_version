label bad_monika_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[13] = True
    if persistent.chapter == True:
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 14
        $ style.say_dialogue = style.normal
        $ quick_menu_limit = False
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
    show monika 2c at face
    mc "..."
    play music t5m
    m "..."
    mc "..."
    m "..."
    show monika 2j
    mc "...WOW!"
    voice "voice/monika/monika_bad_01.ogg"
    m 5a "Morning!"
    mc "W-w-why are you here?"
    voice "voice/monika/monika_bad_02.ogg"
    m 4b "Hey,I'm the president. It's my job to wake up members who overslept."
    mc "D...did I?"
    voice "voice/monika/monika_bad_03.ogg"
    m "You worked so hard,[player]. I really really appreciate that."
    voice "voice/monika/monika_bad_04.ogg"
    m "The important thing in the GAME is not winning but taking part. And it's the festival time!"
    "..."
    "...Ha ha."
    "I'm back. Back to the reality."
    "No more nightmares. Nevermore."
    voice "voice/monika/monika_bad_05.ogg"
    m 2d "[player]...are you OK?"
    "I stared at her eyes...and I hold her gently."
    m 1e "..."
    mc "Thank you Monika. Thank you very much. You saved me."
    m 1g "[player]..."
    "That nightmare ended."
    "Now I'm back to the usual life."
    "Dull,boring...but sometimes happy. My usual life."
    show monika 1q
    stop music fadeout 1.0
    "..."
    mc "Monika?"
    voice "voice/monika/monika_bad_06
    .ogg"
    m 1i "I can't believe...that we're going to...end."
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
    if not persistent.achievement[3]:
        stop music fadeout 2.0
        scene black
        with dissolve_scene_full
        $ renpy.notify(achievement_notify + achievement_name_4)
        $ persistent.achievement[3] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 2.0
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_earn_achievement("BAD_MONIKA")
    if persistent.chapter == False:
        return
    else:
        call endgame
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
