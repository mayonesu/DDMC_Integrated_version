label wallace_main:
    if persistent.chapter == True:
        $ style.say_dialogue = style.normal
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    pause 2.0
    show wallace 1b zorder 2 at t11
    w "Hi,[player]!"
    w "You put in a lot of hard work to get here, didn't you?"
    w 1d "Hm?　Maybe I haven't seen you before, huh?"
    w 1a "I'm Wallace. Nice to meet you."
    w 1g"Why am I here?"
    w 1q "Because..."
    w 1s "I have something to tell you."
    w 1a "You maybe play this DDMC normally."
    w "This game has many secrets."
    w 1q "For example..."
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
    pause 1.0
    w 1k "Hey! Your mouse icon changes into Sayori!"
    w 1n "I don't tell you where it happens, but it will appear in the high probability scene."
    w 1b "In addition to this, there are some scene that comes out with probability so please try looking!"
    $ config.mouse = None
    w "And,there is a secret file in this mod."
    w "The file name is 'mc.chr'."
    w 1g "This 'mc' dosen't mean you."
    w 1s "(m)ayo's (c)omment"
    w "That means the comment from this mod's dev, 'mayo'."
    w "You think he made funny thing,don't you?"
    w 1b "This file is image file. You can change file extension from '.chr' to '.png' and find the QR code."
    w "I don't tell you what to do next."
    w 1q "But I'll tell you a hint..."
    w 1i "Same Monika."
    w "You can't understand what I told you."
    w "But if you have played vanilla DDLC, you can find it."
    w "If you can't understad, you should serch from Google."
    w 1b "That's all."
    w 1k "Have a nice day! Bye!"
    scene black
    with dissolve_scene_full
    pause 1.0
    $ renpy.full_restart(transition=None, label="splashscreen")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
