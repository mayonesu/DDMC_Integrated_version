image you_are_cheater:
    "images/cheater.png"
    size (1280,720)

translate None label:
    label start:

        $ anticheat = persistent.anticheat


        $ chapter = 0


        $ _dismiss_pause = config.developer


        $ s_name = "Sayori"
        $ m_name = "Monika"
        $ n_name = "Natsuki"
        $ y_name = "Yuri"

        $ quick_menu = True
        $ style.say_dialogue = style.normal
        $ in_sayori_kill = None
        $ allow_skipping = True
        $ config.allow_skipping = True
        $ sayori_end = 0
        $ yuri_end = 0
        $ natsuki_end = 0
        $ monika_end = 0
        $ normal_end = 0
        $ sayori_end = False

        if persistent.newyear:
            call happynewyear
            return

        python:
            try:
                renpy.file("../characters/sayori.chr")
            except:
                sayori_end = True
        if _preferences.language != None and sayori_end == True:
            call sayori_mad
            return
        if persistent.horror_effects and renpy.random.randint(0,3) == 0:
            call color_bar_main
        call ch1_main
        call ch1_1_main
        call ch2_main
        call ch3_1_main
        if sayori_end == 1:
            call bad_sayori_main
            call endgame
            return

        call ch3_2_main
        call ch4_main
        call ch5_1_main
        call ch5_2_main
        call ch6_1_main
        call ch6_1_1_main
        if yuri_end == 1:
            call bad_yuri_main
            call endgame
            return
        call ch6_2_main
        if natsuki_end == 1:
            call bad_natsuki_main
            call endgame
            return
        call ch6_3_main
        call ch7_main
        if monika_end == 1:
            call bad_monika_main
            call endgame
            return
        call ch7_1_main
        call ch8_main
        if normal_end == 1:
            call normal_end
        call ch8_1_main
        call ch9_main
        call ch9_1_main
        call ch9_2_main
        call ch9_3_main
        call ch9_4_main
        call ch10_main
        call ch10_1_main
        call ch10_2_main
        call ch10_3_main
        call ch10_4_main
        call ch10_5_main
        jump credits
        return

    label endgame(pause_length=4.0):
        $ quick_menu = False
        window hide(None)
        stop music fadeout 2.0
        scene black
        show end
        with dissolve_scene_full
        pause pause_length
        $ quick_menu = True
        $ renpy.full_restart(transition=None, label="splashscreen")
        return

    label you_are_cheater:
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        $ config.allow_skipping = False
        stop music
        $ quick_menu = False
        $ main_menu = True
        play sound "tl/None/sfx/pi.ogg"
        show yct
        "That's why I told you."
        window hide(None)
        pause 6.0
        hide yct
        scene red
        $ renpy.call_screen("dialog", message="ILLEGAL INSTRUCTION\n596F752073686F756C646E2774206861766520646F6E6520746861742E", ok_action=Function(UninstallMod))
        return

    label first_horror:
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        $ config.allow_skipping = False
        stop music
        window hide(None)
        show you_are_cheater
        play sound "tl/None/sfx/pi.ogg"
        pause 5.0
        if not persistent.achievement[15]:
            $ persistent.achievement[15] = True
        $ renpy.quit()

image yct = Movie(play="cheater.webm", size=(1280,720), loop=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
