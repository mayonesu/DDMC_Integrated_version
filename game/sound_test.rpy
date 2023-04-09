init python:
    def Finishentermusictag_not_debug():
        renpy.hide_screen("music_tag_input")
        renpy.music.play("bgm/" + music_filename + ".ogg")
        #play music "music_tag"
        renpy.call("other_music")

    def Finishentersfxtag_not_debug():
        renpy.hide_screen("music_tag_input")
        renpy.sound.play("sfx/" + music_filename + ".ogg")
        #play music "music_tag"
        
        renpy.call("sound_effect")

    def play_voice_not_debug():
        renpy.hide_screen("voice_num_input")
        renpy.sound.play("voice/" + set_character + "/" + set_character + set_scene + set_num + ".ogg")

init -501 screen sound_volume():
    add "bg/back.png"
    style_prefix "game_menu"
    hbox:
        xalign 0.75 ypos 200
        vbox:
            style_prefix "check"
            label _("Voice Mode")
            textbutton _("ON") action [SetPersistent("disable_voice", False),SetDict(_preferences.volumes,'voice',1.00)]
            textbutton _("OFF") action [SetPersistent("disable_voice", True),SetDict(_preferences.volumes,'voice',0.00)]
    hbox:
        style_prefix "slider"
        box_wrap True
        xalign 0.5 yalign 0.5
        vbox:
            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume")

            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume")

            if config.has_voice and not persistent.disable_voice:
                label _("Voice Volume")
                hbox:
                    bar value Preference("voice volume")
    hbox:
        vbox:
            ypos 700
            textbutton _("Return to menu"):
                style "return_button"
                action Hide("sound_volume"),Jump("sound_test_not_debug")
        vbox:
            ypos 700
            xpos 800
            textbutton _("Reset Volume"):
                style "return_button"
                action Function(reset_volume)

label sound_test_not_debug:
    scene tos
    $ music_filename = ""
    $ filelist = ""
    $ music_filelist = config.basedir + "/music_filelist.txt"
    $ sfx_filelist = config.basedir + "/sfx_filelist.txt"
    menu:
        "Only DDMC Music":
            menu:
                "m1b":
                    play music m1b
                "t10s":
                    play music t10s
                "t5nr":
                    play music t5nr
                "smad":
                    play music smad
                "Back":
                    call sound_test_not_debug
        "Other Music":
            call other_music
        "Sound Effect":
            call sound_effect
        "Stop music":
            stop music
        "Voice":
            call voice_test_not_debug
        "Volume Setting":
            call screen sound_volume()
        "Back":
            #$ renpy.full_restart()
            hide tos
            call special_menu
    call sound_test_not_debug
    return()

label other_music():
    $ music_filename = ""
    menu:
        "Enter Music Filename":
            $ renpy.show_screen("music_tag_input",message="Please enter music filename without \".ogg\".", ok_action=Function(Finishentermusictag_not_debug))
        "Show Music Filelist":
            python:
                try: renpy.file(config.basedir + "/music_filelist.txt")
                except: open(config.basedir + "/music_filelist.txt", "wt").write(renpy.file("music_filelist.txt").read())
                import os
                if renpy.windows:
                    import subprocess
                    subprocess.Popen(['start',music_filelist], shell=True)
                elif renpy.macintosh:
                    os.system('open -t ' + music_filelist)
                elif renpy.linux:
                    os.system('xdg-open ' + music_filelist)
                else:
                    "None"
        "Back":
            call sound_test_not_debug
    call other_music
    return()

label sound_effect():
    $ music_filename = ""
    menu:
        "Enter Sfx Filename":
            $ renpy.show_screen("music_tag_input",message="Please enter sfx filename without \".ogg\".", ok_action=Function(Finishentersfxtag_not_debug))
        "Show Sfx filelist":
            python:
                try: renpy.file(config.basedir + "/sfx_filelist.txt")
                except: open(config.basedir + "/sfx_filelist.txt", "wt").write(renpy.file("sfx_filelist.txt").read())
                if renpy.wondows:
                    import subprocess
                    subprocess.Popen(['start',sfx_filelist], shell=True)
                elif renpy.macintosh:
                    os.system('open -t ' + sfx_filelist)
                elif renpy.linux:
                    os.system('xdg-open ' + sfx_filelist)
                else:
                    "None"
        "Back":
            call sound_test_not_debug
    call sound_effect
    return()

label voice_test_not_debug:
    $ set_character = ""
    $ set_scene = ""
    $ set_num = ""
    menu:
        "Sayori":
            $ set_character = "sayori"
            call voice_sayori_select
        "Natsuki":
            $ set_character = "natsuki"
            call voice_natsuki_select
        "Yuri":
            $ set_character = "yuri"
            call voice_yuri_select
        "Monika":
            $ set_character = "monika"
            call voice_monika_select
        "Back":
            call sound_test_not_debug
    return()

label voice_sayori_select:
    menu:
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 05)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "Sayori Mad":
            $ set_scene = "_mad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 19)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "Normal End":
            $ set_scene = "_normal_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 13)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "Back":
            call voice_test_not_debug
    return()

label voice_natsuki_select:
    menu:
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_natsuki_select
        "chapter 6":
            $ set_scene = "_ch6_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice_not_debug))
            call voice_natsuki_select
        "chapter 10":
            $ set_scene = "_ch10_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_natsuki_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice_not_debug))
            call voice_natsuki_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice_not_debug))
            call voice_sayori_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 04)", ok_action=Function(play_voice_not_debug))
            call voice_natsuki_select
        "Back":
            call voice_test_not_debug
    return()

label voice_yuri_select:
    menu:
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_yuri_select
        "chapter 6":
            $ set_scene = "_ch6_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_yuri_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 06)", ok_action=Function(play_voice_not_debug))
            call voice_yuri_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 08)", ok_action=Function(play_voice_not_debug))
            call voice_yuri_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 04)", ok_action=Function(play_voice_not_debug))
            call voice_yuri_select
        "Back":
            call voice_test_not_debug
    return()

label voice_monika_select:
    menu:
        "chapter 3":
            $ set_scene = "_ch3_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 19)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "chapter 4":
            $ set_scene = "_ch4_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "chapter 7":
            $ set_scene = "_ch7_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 13)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "chapter 8":
            $ set_scene = "_ch8_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "Next":
            call voice_monika_select2
        "Back":
            call voice_test_not_debug

label voice_monika_select2:
    menu:
        "chapter 9":
            $ set_scene = "_ch9_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 93)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "chapter 10":
            $ set_scene = "_ch10_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 172)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 06)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 10)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 09)", ok_action=Function(play_voice_not_debug))
            call voice_monika_select
        "Previous":
            call voice_monika_select
        "Back":
            call voice_test_not_debug