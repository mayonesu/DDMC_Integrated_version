define error_report = "H...EL...P...ME..."
image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat

python:
    error_title = "An exception has occurred."
    error_message = "File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details."

image fake_exception:
    Text(error_title, size=40, style="_default")
image fake_exception2:
    Text(error_message, size=20, style="_default")

label ch3_1_main:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.chapter_seen[2] = True
    if persistent.chapter == True:
        window hide(None)
        if persistent.chapter_sel == True:
            $ _history_list = []
            $ persistent.chapter_sel = False
        $ ddmc_chapter = 3
        $ style.say_dialogue = style.normal
        $ quick_menu = True
    $ main_menu = None
    if persistent.chapter == True:
        stop music fadeout 1.0
    pause 1.5
    scene bg house
    with dissolve_scene_full
    window show(None)
    if not persistent.chapter and persistent.autosave_mode:
        $ renpy.save('autosave')
        $ renpy.notify('autosaved.')
    "It's the day of the festival."
    "Of all days,I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I considered going to her house to wake her up,but decided that's a little too much."
    "Meanwhile,the preparations for the event should be nearly complete."
    "the banner Yuri and I painted is dry,and I gently rolled it up to take with me."
    "She sent me some random texts not only reminding me not to forget anything,and I reassured her."
    "Funnily enough,I probably feel the same way as natsuki about the event."
    "I'm also excited for it to be over so I can spend time with Sayori at the festival."
    "But knowing Monika,I'm sure the event will be great,too."
    scene bg club_day
    with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    voice "voice/monika/monika_ch3_01.ogg"
    m "You're the first one here."
    voice "voice/monika/monika_ch3_02.ogg"
    m "Thanks for being early!"
    mc "That's funny,I thought at least Yuri would be here by now"
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that have all the poems we're performing."
    "In the end,I found a random poem online that I thought Monika would like,and submitted it."
    "So,that's the one I'll be performinfg."
    voice "voice/monika/monika_ch3_03.ogg"
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah,she overslept again..."
    mc "That dummy."
    mc "You'd think that on the days this important,she'd try a little harder..."
    "I say that,but I suddenly remember what Sayori told me yesterday..."
    "And I suddenly feel awful,knowing it's not nearly that simple for her."
    "I only said it because it's the way I'm used to thinking."
    "But......"
    "Maybe I should have gone to wake her up after all?"
    voice "voice/monika/monika_ch3_04.ogg"
    m 1k "Ahaha."
    voice "voice/monika/monika_ch3_05.ogg"
    m 4b "You should take a little responsibility for her,[player]!"
    voice "voice/monika/monika_ch3_06.ogg"
    m "I mean,especially after your exchange with her yesterday..."
    voice "voice/monika/monika_ch3_07.ogg"
    m "You kind of left her hanging this morning,you know?"
    show monika 4a
    mc "Exchange...?"
    mc "Monika......You know about that??"
    voice "voice/monika/monika_ch3_08.ogg"
    m 2a "Of course I do."
    voice "voice/monika/monika_ch3_09.ogg"
    m "I'm the club president,after all."
    mc "But......!"
    "I stammer,embarrassed."
    "Did Sayori really tell her about it that quickly?"
    "That we're...a couple now?"
    "I didn't really plan on bringing it up with anyone yet..."
    mc "Jeez..."
    mc "You don't know the full story at all,so..."
    voice "voice/monika/monika_ch3_10.ogg"
    m 2j "Don't worry."
    voice "voice/monika/monika_ch3_11.ogg"
    m "I probably know a lot more than you think."
    mc "Eh...?"
    "Monika is being as friendly as usual,but for some reason I felt a chill down my spine after hearing that."
    voice "voice/monika/monika_ch3_12.ogg"
    m 5 "Hey,do you want to check out the pamphlets?"
    voice "voice/monika/monika_ch3_13.ogg"
    m "They came out really nice!"
    mc "Yeah,sure."
    "I grab one of the pamphlets laid out on the desks."
    mc "Oh yeah,they really did."
    mc "Something like this will definitely help people take the club more seriously."
    voice "voice/monika/monika_ch3_14.ogg"
    m "Yeah,I thought so too!"
    "I flip through the pages."
    "Each member's poem is neatly printed on its own page,giving it an almost professional feel."
    "I recognize Natsuki's and Yuri's poems from the ones they performed during our practice."
    mc "What's this...?"
    "I flip to Sayori's poem."
    "It's different from the ones she practiced."
    "It's one that I haven't read before..."
    call showpoem (poem_s3, music=False)
    mc "Ah..."
    "What is this...?"
    "Reading the poem,I get a pit in my stomach."
    m 1d "[player]?"
    voice "voice/monika/monika_ch3_15.ogg"
    m "What's wrong?"
    mc "Ah,nothing..."
    "This poem feels completely different from everything else Sayori's written."
    "But more than that..."
    mc "I-I changed my mind!"
    mc "I'm going to get Sayori,so..."
    voice "voice/monika/monika_ch3_16.ogg"
    m "Ah......"
    voice "voice/monika/monika_ch3_17.ogg"
    m 1b "Well,alright!"
    voice "voice/monika/monika_ch3_18.ogg"
    m "Try not to take too long,okay?"
    "I quickly leave the classroom."
    scene bg corridor
    with wipeleft_scene
    voice "voice/monika/monika_ch3_19.ogg"
    m "Don't strain yourself~"
    "Monika calls that out after me."
    "I quicken my pace."
    "What was I thinking?"
    "I should have tried a little bit harder for Sayori."
    "It's not a big deal to at least wait for her,or help her wake up."
    scene bg residential_day
    with wipeleft_scene
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs,and what I want to give her."
    scene bg house
    with wipeleft_scene
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer,since she's not picking up her phone,either."
    "Like yesterday,I open the door and let myself in."
    scene black
    with wipeleft_scene
    mc "Sayori...?"
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "That really is something that a boufriend would do,isn't it?"
    "In any case..."
    "It just feels right."
    "Outside Sayori's room,I knock on her door."
    mc "Sayori?"
    mc "Wake up,dummy..."
    "There's no response."
    "I really don't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    $ pause(6.0)
    if persistent.horror_effects and renpy.random.randint(0,5) == 0:
        $ renpy.notify("[player], why did you do that...?")
    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "What the hell...?"
    "What the hell??"
    "Is this a nightmare?"
    "It...has to be."
    "This isn't real."
    "There's no way this can be real."
    "Sayori wouldn't do this."
    "Everything was normal up until a few days ago."
    "That's why I can't believe what my eyes are showing me...!"
    "I suppress the urge to vomit."
    menu:
        "I don't believe it. This is..."
        "Just a Nightmare.":
            $ sayori_end = 1
        "My reality.Accept it.":
            $ sayori_end = 0
            if persistent.horror_effects and renpy.random.randint(0,5) == 0:
                stop music
                $ seen_eyes_this_chapter = True
                if persistent.gamepad:
                    if persistent.change_buttons:
                        $ config.pad_bindings["pad_a_press"] = [ ]
                    else:
                        $ config.pad_bindings["pad_b_press"] = [ ]
                $ quick_menu = False
                play sound "sfx/eyes.ogg"
                $ persistent.seen_eyes = True
                $ renpy.save_persistent()
                stop music
                scene black with None
                show bg eyes_move
                $ pause(1.2)
                hide bg eyes_move
                show bg eyes
                $ pause(0.5)
                hide bg eyes
                show bg eyes_move
                $ pause(1.25)
                hide bg eyes with None
                if not persistent.achievement[11]:
                    $ renpy.notify(achievement_notify + achievement_name_12)
                    $ persistent.achievement[11] = True
                    play sound "tl/None/sfx/achievement.ogg"
                $ quick_menu = True
                if persistent.gamepad:
                    if persistent.change_buttons:
                        $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
                    else:
                        $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
                $ pause(2.0)
    python:
        try: sys.modules['renpy.error'].report_exception(error_report, False)
        except: pass
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    $ in_sayori_kill = False
    if persistent.chapter == False:
        return
    else:
        if sayori_end == 1:
            stop music fadeout 1.0
            scene black
            with dissolve_scene_full
            call bad_sayori_main
            call endgame
            return
        else:
            jump ch3_2_main
    return

label ch3_2_main:
    "I sink down to the floor."
    "I can hardly breathe,and my heart is pounding so hard."
    mc "ah..."
    "I can't say a word but a kind of noise."
    "..."
    "Ok boy,stand on your own feet,slowly,slowly..."
    "I almost sink down over and over, but manage not to faint. "
    "Somehow I stand up unsteadily."
    play music t10s
    "She once said that she liked the way as it used to be."
    "See. It's NOT the way she likes. NEVER."
    "You also wanted to make her wish come true,right?"
    "I murmur something obscure,and walk dizzily to her."
    mc "Sorry Sayori,very sorry.You don't like this kind of..."
    "I hold her body in my arm,and carry her to the bed."
    "..."
    show sayori_bedroom:
        zoom 2.5 xalign 0.5 yalign 1.0
    show expression "#ff000060"
    with dissolve_scene_full
    show sayori 1bq at t11
    "She is sleeping.I know she's a heavy sleeper."
    mc "Hey Sayori..."
    "I know she doesn't hear me,because she's now in a good sleep."
    "I just wanted to call her name."
    "Yes.Sayori is..."
    python:
        renpy.call_screen("dialog", message="Just Asleep.", ok_action=Return())
    "I stand up.Monika told me not to be so late."
    mc "Don't be late for school,Sayori."
    "I gently close the door."
    show sayori 1bq at thide
    hide sayori
    scene black
    with dissolve_scene_full
    if persistent.chapter == False:
        return
    else:
        call ch4_main
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
