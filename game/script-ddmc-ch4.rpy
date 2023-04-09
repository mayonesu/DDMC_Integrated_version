label ch4_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[3] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 4
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    stop music fadeout 1.0
    scene bg corridor
    with wipeleft_scene
    show monika 3a zorder 2 at t11
    if persistent.horror_effects and renpy.random.randint(0,2) == 0:
        if not persistent.achievement[7]:
            $ renpy.notify(achievement_notify + achievement_name_8)
            $ persistent.achievement[7] = True
            play sound "tl/None/sfx/achievement.ogg"
        if ddmm_online and persistent.ddmm_achievement:
            $ ddmm_register_achievement("MOUSE_SAYORI", achievement_name_8, achievement_message_8)
            $ ddmm_earn_achievement("MOUSE_SAYORI")
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}
    voice "voice/monika/monika_ch4_01.ogg"
    m "Yay,you're back!"
    voice "voice/monika/monika_ch4_02.ogg"
    m "Later than expected,right?"
    voice "voice/monika/monika_ch4_03.ogg"
    m 3b "...Where is Sayori?"
    show monika 1f
    mc "She is..."
    "She is...well,what did I do to her? I remenber I went to her house and..."
    mc "She was in a good sleep. I could't wake her up."
    mc "And you know, she looked down these days. I don't think she's feeling well."
    mc "I told her to come to school,but she might be late."
    voice "voice/monika/monika_ch4_04.ogg"
    m 2a "Ah,I see..."
    "She doesn't ask me why anymore."
    voice "voice/monika/monika_ch4_05.ogg"
    m "But..."
    mc "But?"
    voice "voice/monika/monika_ch4_06.ogg"
    m 1e "Nevermind."
    "And she smiles to me."
    "A sad smile which I've never seen before."
    voice "voice/monika/monika_ch4_07.ogg"
    m 3d "Everyone's waiting for you in the classroom,you know?"
    "She says and walks away."
    stop music fadeout 1.0
    $ config.mouse = None
    if persistent.chapter == False:
        return
    else:
        call ch5_1_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
