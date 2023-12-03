image bsod_mac1:
    "bg/mac_error.png"
    size (1280,720)

image bsod_linux1:
    "bg/linux_error.png"
    size (1280,720)

image bsod_mac = LiveComposite((1280, 720), (0, 0), "bsod_mac1", (0, 0), "bsod_2")
image bsod_linux = LiveComposite((1280, 720), (0, 0), "bsod_linux1", (0, 0), "bsod_2")

label ch8_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[7] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 8
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    stop music
    if persistent.horror_effects and renpy.windows and renpy.game.preferences.fullscreen and not persistent.achievement[9]:
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        $ quick_menu = False
        $ mouse_visible = False
        play sound "tl/None/sfx/sfx_ERROR.ogg"
        scene bsod
        $ pause(5.0)
        scene black
        $ pause(1.0)
        if not persistent.achievement[9]:
            $ renpy.notify(achievement_notify + achievement_name_10)
            $ persistent.achievement[9] = True
            play sound "tl/None/sfx/achievement.ogg"
            pause 2.5
            if not persistent.chapter and persistent.autosave_mode:
                $ renpy.save('autosave')
                $ renpy.notify('autosaved.')
        $ quick_menu = True
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
        $ mouse_visible = True
    elif persistent.horror_effects and renpy.macintosh and renpy.game.preferences.fullscreen and not persistent.achievement[9]:
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        $ quick_menu = False
        $ mouse_visible = False
        play sound "tl/None/sfx/sfx_ERROR.ogg"
        scene bsod_mac
        $ pause(5.0)
        scene black
        $ pause(1.0)
        if not persistent.achievement[9]:
            $ renpy.notify(achievement_notify + achievement_name_10)
            $ persistent.achievement[9] = True
            play sound "tl/None/sfx/achievement.ogg"
            pause 2.5
            if not persistent.chapter and persistent.autosave_mode:
                $ renpy.save('autosave')
                $ renpy.notify('autosaved.')
        $ quick_menu = True
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
        $ mouse_visible = True
    elif persistent.horror_effects and renpy.linux and renpy.game.preferences.fullscreen and not persistent.achievement[9]:
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        $ quick_menu = False
        $ mouse_visible = False
        play sound "tl/None/sfx/sfx_ERROR.ogg"
        scene bsod_linux
        $ pause(5.0)
        scene black
        $ pause(1.0)
        if not persistent.achievement[9]:
            $ renpy.notify(achievement_notify + achievement_name_10)
            $ persistent.achievement[9] = True
            play sound "tl/None/sfx/achievement.ogg"
            pause 2.5
            if not persistent.chapter and persistent.autosave_mode:
                $ renpy.save('autosave')
                $ renpy.notify('autosaved.')
        $ quick_menu = True
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
        $ mouse_visible = True
    else:
        scene black
        if not persistent.chapter and persistent.autosave_mode:
            $ renpy.save('autosave')
            $ renpy.notify('autosaved.')
    mc "Say something to me,Monika."
    mc "I only want to know the truth."
    mc "Sayori,Yuri and Natsuki...they are gone..."
    mc "Now that I have only you...Just Monika."
    "I didn't want to,but I sob out it."
    "Smile on her face disappears."
    show expression "images/cg/monika/monika_room_highlight.png"
    with dissolve
    play music mend
    show monika 1h at face
    m "..."
    voice "voice/monika/monika_ch8_01.ogg"
    m 1i "I..."
    m 1q "..."
    voice "voice/monika/monika_ch8_02.ogg"
    m 1i "I thought that It was okay if you hated me."
    voice "voice/monika/monika_ch8_03.ogg"
    m "I thought it was not so bad to drag out this happiness,though it'd not be so long."
    voice "voice/monika/monika_ch8_04.ogg"
    m "Because it was...my resistance,which I could do the most."
    mc "Resistance...what...?"
    show monika 1q
    "She doesn't answer. She just closes her eyes."
    voice "voice/monika/monika_ch8_05.ogg"
    m 1r "It's not always right,to know the truth."
    voice "voice/monika/monika_ch8_06.ogg"
    m "Maybe it's too late,but maybe it's not too late."
    voice "voice/monika/monika_ch8_07.ogg"
    m 1p "Trust me, I want you to be happy...at least not to be unhappy."
    "She looks she's having pain inside."
    voice "voice/monika/monika_ch8_08.ogg"
    m 1o "Nonetheless...Do I have to tell?"
    show expression "#00000060"
    "I'm shaken up. I've never seen her like this."
    "She...She might be right. I don't know."
    "I..."
    menu:
        "Believe in Monika.":
            window hide(None)
            pause 1.0
            $ consolehistory = []
            call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
            $ delete_character("monika")
            pause 1.0
            show screen tear(8, offtimeMult=1, ontimeMult=10)
            $ pause(1.5)
            stop music
            call normal_end
        "Don't believe in Monika.":
            $ restore_all_characters()
            $ normal_end = 0
    if persistent.chapter == False:
        return
    else:
        call ch8_1_main

label ch8_1_main:
    hide expression "images/cg/monika/monika_room_highlight.png"
    hide monika
    show expression "images/cg/monika/monika_room.png"
    show monika 1o at face
    stop music fadeout 1.0
    mc "Monika,you may be telling me the truth."
    voice "voice/monika/monika_ch8_09.ogg"
    m 1h "I don't tell you a lie,[player]. I didn't, I won't tell you a lie."
    voice "voice/monika/monika_ch8_10.ogg"
    m 1i "No one would come back to life,even if you knew the truth. But if you believe me,they might..."
    mc "I know...but I can't believe you. I can't believe anything."
    mc "As I said,now I have just you,Monika. And I don't want anyone to suffer pain. Nevertheless...I don't know. I don't know what to believe..."
    m 1q "..."
    "She closes her eyes again,and keeps silent."
    m "..."
    voice "voice/monika/monika_ch8_11.ogg"
    m 1f "Okay everyone."
    voice "voice/monika/monika_ch8_12.ogg"
    m 1d "Here's Monika's last listening tip of the day."
    voice "voice/monika/monika_ch8_13.ogg"
    m "'1.You don't have to believe Monika's story.'"
    voice "voice/monika/monika_ch8_14.ogg"
    m "'2.Monika doesn't tell a lie to you. Believe it.'"
    voice "voice/monika/monika_ch8_15.ogg"
    m "'3.Don't bother Monika till she finishes the story.'"
    show monika 1f
    "I nod."
    show monika 1e
    "She smiles a little."
    scene black
    with dissolve_scene_full
    hide monika
    hide expression "images/cg/monika/monika_room.png"
    if persistent.chapter == False:
        return
    else:
        call ch9_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
