label ch2_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[1] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 2
        $ style.say_dialogue = style.normal
        $ quick_menu = True
        scene black
        stop music fadeout 1.0
        with dissolve_scene_full
    else:
        pause 2.0
    $ main_menu = None
    scene bg bedroom
    with open_eyes
    play music t2
    window show(None)
    if not persistent.chapter and persistent.autosave_mode:
        $ renpy.save('autosave')
        $ renpy.notify('autosaved.')
    "Glorius morning."
    "Except the nightmare tortured me and pooled me into sweat."
    "I take a shower quickly and put the uniform on."
    "I should have some breakfast, anyway."
    scene bg kitchen
    with wipeleft_scene
    "I come to the kitchen, but I'm not so hungry."
    "(Sigh)"
    "Because I've got knot in my stomach."
    "About Sayori, of course."
    "She said that her rainclouds haven't gone yet."
    "But, what can I do for her?"
    "..."
    "Does she skip breakfast so often?"
    "I don't think she's good at cooking."
    "I also doubt if she can just cut the vegetable."
    "Neither can I, but I don't think I'm worse than her."
    "Like, chopping green onion. It's not so hard for me."
    "If I could make a miso-soup for her in the morning,"
    "She might feel happy, at least she would eat it."
    "I take a kitchen knife in the hand."
    "I look at it, and my train of thoughts go..."
    "Umm... When did I cook something last time?"
    "..."
    "..."
    "..."
    "..."
    "...Oh shit."
    "I was spacing out for... how long? I'm late."
    "I shurug and pick up my school bag."
    "Good bye my breakfast, again."
    window hide(None)
    scene black
    stop music fadeout 1.0
    with dissolve_scene_full
    if persistent.chapter == False:
        return
    else:
        jump ch3_1_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
