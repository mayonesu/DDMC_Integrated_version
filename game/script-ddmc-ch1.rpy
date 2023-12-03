label ch1_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[0] = True
    if persistent.chapter == True:
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 1
        window hide(None)
    stop music fadeout 2.0
    scene bg bedroom
    show expression "#000000b0"
    with dissolve_scene_full
    play music t9
    $ restore_all_characters()
    if persistent.new_name:
        $ renpy.notify("Saved your name as file \"name\".You can load your name from the file after you reset the game.")
        $ persistent.new_name = False
        pause 2.5
        if not persistent.chapter and persistent.autosave_mode:
            $ renpy.save('autosave')
            $ renpy.notify('autosaved.')
    else:
        if not persistent.chapter and persistent.autosave_mode:
            $ renpy.save('autosave')
            $ renpy.notify('autosaved.')
    window show(None)
    "What a wonderful weekend tonight !"
    "Now I'm spacing out for a while,sitting on the bed in my room."
    "Sayori, my childhood friend, invited me to the literature club. It was the flashpoint."
    "I met Queen Monika again."
    "(well,she is sometimes ironical with her beautiful smile on the face)"
    "Spent hours with Natsuki, reading her manga together."
    "(umm,Parfait Girls. She really really loves it. IDK why)"
    "Oh, Yuri came to my room."
    "(I've never invited any girls to my house, as long as I can remenber.)"
    "And..."
    "I confessed to Sayori. Yes,I did it."
    "It's just a couple hours ago."
    "I think I did the right thing, but..."
    "I don't know. I just don't know."
    "..."
    "She said that she liked it to be the way as it used to be."
    "..."
    "Ok boy, stop thinking too much. And tomorrow is the festival."
    stop music fadeout 1.0
    "Have a good night. Tomorrow's just another day."
    "Night night."
    "..."
    "I think I have to do something . What...?"
    "What...something important to me..."
    scene black
    with close_eyes
    "Jeez, I can't remember it."
    "Hello darkness, my old friend. It covers me slowly and,"
    "I fall into sleep."
    window hide(None)
    return

label ch1_1_main:
    pause 0.5
    show end_glitch1
    with dissolve_scene_full
    play music m1b
    "...Hmm?"
    "Am I dreaming?"
    "Yeah, I'm dreaming now."
    "A lucid dream, huh?"
    "...and what is this?"
    "I faintly see the figures of men...in white robes...?"
    q "Any changes in state?"
    q "No."
    q "(Sigh)"
    "..."
    show black
    scene black
    stop music fadeout 1.0
    with dissolve_scene_full
    "I don't know why but,"
    "They scare me."
    "...and they turned to me."
    "I must escape right now ,or..."
    "But my body won't move as I intend."
    "Goddamn!!"
    python:
        renpy.call_screen("dialog", message="Wake up!", ok_action=Return())
    scene black
    window hide(None)
    if persistent.chapter == False:
        return
    else:
        call ch2_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
