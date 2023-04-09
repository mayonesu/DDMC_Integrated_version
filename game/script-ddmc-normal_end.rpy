init python:
    currentuser = ""
    try:
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                currentuser = user
    except:
        pass
    player = persistent.playername
    message = "Hey," + currentuser + "?"
    message2 = "\"Hey,another " + player + "?\""
    message_vbs = "Call MsgBox(\""+player+" \"\""+message+"\"\"\",vbInformation,\"DDLC.exe\")"
    message2_vbs = "Call MsgBox(\""+player+" \"\""+message2+"\"\"\",vbInformation,\"DDLC.exe\")"

label normal_end:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[14] = True
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ ]
    $ config.allow_skipping = False
    $ persistent.normal_end = 1
    window hide(None)
    if renpy.variant("pc"):
        $ persistent.autoload = "normal_end"
    python:
        persistent.clear[0] = True
        persistent.clear[1] = True
        persistent.clear[2] = True
        persistent.clear[3] = True
        persistent.clear[4] = True
        persistent.clear[5] = True
        persistent.clear[6] = True
        persistent.clear[7] = True
        persistent.clear[8] = True
        persistent.clear[9] = False
        renpy.save_persistent()
        style.say_dialogue = style.normal
        style.say_window = style.window
        main_menu = True
        renpy.full_restart(transition=None, label="fakesplash")

label normal_end2:
    $ config.allow_skipping = False
    if persistent.chapter == True:
        $ style.say_dialogue = style.normal
    python:
        quick_menu_limit = True
        main_menu = False
    window auto
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    scene bg house
    with dissolve_scene_full
    play music t2
    $ s_name = "???"
    voice "voice/sayori/sayori_normal_01.ogg"
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance,waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori,my neighbor since we are children."
    "You know,the kind of friend you'd never see yourself making today,but it just kind of works out because you've known each other for so long?"
    "And,um,she's my girlfriend,too."
    "Well,I've been going with her for a day."
    "Yes,since yesterday."
    "However,I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    show sayori 4p zorder 2 at t11
    $ s_name = "Sayori"
    voice "voice/sayori/sayori_normal_02.ogg"
    s "Haahhh...haahhh..."
    voice "voice/sayori/sayori_normal_03.ogg"
    s "I overslept again!"
    voice "voice/sayori/sayori_normal_04.ogg"
    s "But I caught you this time!"
    mc "Maybe,but only because I decided to stop and wait for you."
    voice "voice/sayori/sayori_normal_05.ogg"
    s 5c "Eeehhhhh,you say that like you were thinking about ignoring me!"
    voice "voice/sayori/sayori_normal_06.ogg"
    s "That's mean,[player]!"
    "I can't help but smile."
    mc "I won't. The festival without our president won't go well,you know?"
    voice "voice/sayori/sayori_normal_07.ogg"
    s 1a "Fine,fine."
    show sayori 1r
    "We cross the street together and make our way to school."
    show sayori 1b
    mc "By the way,I got a text from Yuri."
    voice "voice/sayori/sayori_normal_08.ogg"
    s 3c "What does she say?"
    mc "\' I came here earlier and am now preparing for the festival with Natsuki,because I thought our president would oversleep again. Please come to us as soon as possible. P.S. She's so mad about it.\'..."
    voice "voice/sayori/sayori_normal_09.ogg"
    s 5a "E..ehehe..."
    mc "Jeez,you dummy you my...sweet."
    voice "voice/sayori/sayori_normal_10.ogg"
    s 4m "W-what? Y-You say wh..."
    "I burst into laugh."
    show sayori 4n
    mc "Nevermind. Let's hurry, or Natsuki would kill us,seriously!" 
    voice "voice/sayori/sayori_normal_11.ogg"
    s 4r "She would! Yay!"
    show sayori 3b
    window hide(None)
    play sound "tl/Japanese/sfx/Cell_Phone-Notification01-3.ogg"
    pause 1.5
    mc "Um? Wait...I got a text from Natsuki,too..."
    voice "voice/sayori/sayori_normal_12.ogg"
    s 3c "What does she say?"
    mc "\'Never never forget to bring the pamphlets or I'll kill you two.\'..."
    show sayori 4o
    "We exchange a look and cry..."
    show sayori 4m
    voice "voice/sayori/sayori_normal_13.ogg"
    mcs "We forgot it!"
    show sayori 4m zorder 1 at thide
    hide sayori
    "..."
    "Our president is unreliable,but thanks for her our Literature Club has come this far."
    "Yuri and Natsuki are getting along with each other,though they sometimes get into a little fight."
    "I'm happy to be Sayori's side."
    "Time will solve her rainclouds."
    "I'm for sure."
    "Moreover,"
    stop music fadeout 1.0
    "I appriciate you."
    "You took the right path."
    "I turned to you."
    scene black
    with dissolve_scene_full
    mc "You think so,too,don't you?"
    if renpy.variant("pc"):
        if persistent.hideusername == False:
            python:
                currentuser = ""
                try:
                    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                        user = os.environ.get(name)
                        if user:
                            currentuser = user
                except:
                    pass
            if not renpy.windows:
                if renpy.macintosh:
                    window hide(None)
                    python:
                        import os
                        os.system("osascript -e \'display notification \""+message+"\" with title \""+player+"\" sound name \""+config.gamedir+"/tl/None/sfx/trytone.ogg\"\'")
                elif renpy.linux:
                    window hide(None)
                    play sound "tl/None/sfx/system29.ogg"
                    python:
                        try: renpy.file(config.basedir + "/window_icon.png")
                        except: open(config.basedir + "/window_icon.png", "wb").write(renpy.file("/tl/None/gui/window_icon.png").read())
                        import os
                        os.system("notify-send -i "+config.basedir+"/window_icon.png "+player+" \""+message+"\"")
                        try: os.unlink(renpy.config.basedir + '/window_icon.png')
                        except: pass
                else:
                    mc "Hey,[currentuser]?"
            else:
                window hide(None)
                #$ tip.showWindow(player,message)
                if not ("steamapps" in config.basedir.lower()):
                    python:
                        try:
                            with open(config.basedir + "/normal.vbs", "w") as f:
                                f.write(message_vbs)
                                f.close
                        except:
                            pass
                        import os
                        import subprocess
                        si = subprocess.STARTUPINFO()
                        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        cmd = "cscript " + config.basedir + "\\normal.vbs"
                        subprocess.call(cmd, startupinfo=si)
                        os.unlink(config.basedir + "/normal.vbs")
                else:
                    mc "Hey,[currentuser]?"
        else:
            if not renpy.windows:
                if renpy.macintosh:
                    window hide(None)
                    play sound "tl/None/sfx/system29.ogg"
                    python:
                        import os
                        os.system("osascript -e \'display notification \""+message2+"\" with title \""+player+"\" sound name \""+config.gamedir+"/tl/None/sfx/trytone.ogg\"\'")
                elif renpy.linux:
                    window hide(None)
                    python:
                        try: renpy.file(config.basedir + "/window_icon.png")
                        except: open(config.basedir + "/window_icon.png", "wb").write(renpy.file("/tl/None/gui/window_icon.png").read())
                        import os
                        os.system("notify-send -i "+config.basedir+"/window_icon.png "+player+" \""+message2+"\"")
                        try: os.unlink(renpy.config.basedir + '/window_icon.png')
                        except: pass
                else:
                    mc "Hey,another [player]?"
            else:
                window hide(None)
                #$ tip.showWindow(player,message2)
                if not ("steamapps" in config.basedir.lower()):
                    python:
                        try:
                            with open(config.basedir + "/normal.vbs", "w") as f:
                                f.write(message_vbs)
                                f.close
                        except:
                            pass
                        import os
                        import subprocess
                        si = subprocess.STARTUPINFO()
                        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        cmd = "cscript " + config.basedir + "\\normal.vbs"
                        subprocess.call(cmd, startupinfo=si)
                        os.unlink(config.basedir + "/normal.vbs")
                else:
                    mc "Hey,another [player]?"

    else:
        if not renpy.windows or ("steamapps" in config.basedir.lower()):
            mc "Hey,another [player]?"
        else:
            window hide(None)
            #$ tip.showWindow(player,message2)
            if not ("steamapps" in config.basedir.lower()):
                python:
                    try:
                        with open(config.basedir + "/normal.vbs", "w") as f:
                            f.write(message2_vbs)
                            f.close
                    except:
                        pass
                    import os
                    import subprocess
                    si = subprocess.STARTUPINFO()
                    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    cmd = "cscript " + config.basedir + "\\normal.vbs"
                    subprocess.call(cmd, startupinfo=si)
                    os.unlink(config.basedir + "/normal.vbs")
            else:
                mc "Hey,another [player]?"
    if not persistent.achievement[4]:
        $ renpy.notify(achievement_notify + achievement_name_5)
        $ persistent.achievement[4] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 3.0
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_earn_achievement("WITHOUT_MONIKA")
    pause 1.0
    jump credits
    return

label normal_end2_2:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[15] = True
    if persistent.gamepad:
        if persistent.change_buttons:
            $ config.pad_bindings["pad_a_press"] = [ ]
        else:
            $ config.pad_bindings["pad_b_press"] = [ ]
    $ config.allow_skipping = False
    $ persistent.normal_end = 2
    if renpy.variant("pc"):
        $ persistent.autoload = "normal_end2_2"
    window hide(None)
    python:
        persistent.clear[0] = False
        persistent.clear[1] = False
        persistent.clear[2] = False
        persistent.clear[3] = False
        persistent.clear[4] = False
        persistent.clear[5] = False
        persistent.clear[6] = False
        persistent.clear[7] = False
        persistent.clear[8] = False
        persistent.clear[9] = False
        try: os.remove(config.basefir + "characters/monika.chr")
        except: delete_character("monika")
        try: os.remove(config.basefir + "characters/natsuki.chr")
        except: delete_character("natsuki")
        try: os.remove(config.basefir + "characters/sayori.chr")
        except: delete_character("sayori")
        try: os.remove(config.basefir + "characters/yuri.chr")
        except: delete_character("yuri")
        renpy.save_persistent()
        style.say_dialogue = style.normal
        style.say_window = style.window
        renpy.full_restart(transition=None, label="fakesplash")

label normal_end2_2_main:
    if persistent.chapter == True:
        $ style.say_dialogue = style.normal
    $ quick_menu_limit = True
    $ main_menu = False
    window auto
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    scene bg house
    with dissolve_scene_full
    play music t2
    mc "Heeeeeeeyyy!!"
    "I cry like an annoying girl,running around and waving my arms in the air like I'm totally oblivious to any attention I might draw to myself."
    "My name is...what? What am I?"
    "You know,the kind of friend you'd never see yourself making today,but it just kind of works out because you've known each other for so long?"
    "However,I just sigh and idle in front of the crosswalk and...hey,catch up to me."
    mc "Haahhh...haahhh..."
    mc "I overslept again!"
    mc "But I caught you this time!"
    mc "Maybe,but only because I decided to stop and wait for you."
    stop music fadeout 1.0
    "Ha! Who is \'you\'? Who is \'I\'?"
    "Now I am alone."
    "Now I am the ONE."
    "Now I am the Literature Club."
    scene black
    with dissolve_scene_full
    "Welcome to my Literature Club."
    python:
        renpy.call_screen("dialog", message="Wake up!", ok_action=Return())
    window hide(None)
    if not persistent.achievement[5]:
        $ renpy.notify(achievement_notify + achievement_name_6)
        $ persistent.achievement[5] = True
        play sound "tl/None/sfx/achievement.ogg"
        pause 3.0
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_earn_achievement("NO_ONE")
    pause 2.0
    jump credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
