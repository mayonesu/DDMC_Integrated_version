image colorbar:
    "images/colorbar.png"
    size (1280,720)

label color_bar_main:
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ ]
    $ config.allow_skipping = False
    stop music
    window hide(None)
    show colorbar
    play sound "tl/None/sfx/pi.ogg"
    pause 5.0
    hide colorbar
    scene black
    if not persistent.achievement[12]:
        $ renpy.notify(achievement_notify + achievement_name_13)
        $ persistent.achievement[12] = True
        play sound "tl/None/sfx/achievement.ogg"
    pause 2.0
    $ config.allow_skipping = True
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
    if persistent.chapter == False:
        return
    else:
        call ch1_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
