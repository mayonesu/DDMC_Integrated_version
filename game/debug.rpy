init python:
    def Finishentermusictag():
        renpy.hide_screen("music_tag_input")
        renpy.music.play("bgm/" + music_filename + ".ogg")
        #play music "music_tag"
        renpy.call("sound_test")

    def Finishentersfxtag():
        renpy.hide_screen("music_tag_input")
        renpy.sound.play("sfx/" + music_filename + ".ogg")
        #play music "music_tag"
        renpy.call("sound_test")

    def play_voice():
        renpy.hide_screen("voice_num_input")
        renpy.sound.play("voice/" + set_character + "/" + set_character + set_scene + set_num + ".ogg")

label debug_mode:
    $ debug_mode = False
    scene tos
    stop music
    menu:
        "Chapter all seen":
            $ chapter_all_seen()
            $ renpy.call_screen("dialog", message="Done.", ok_action=Return())
        "Chapter all not seen":
            $ chapter_all_not_seen()
            $ renpy.call_screen("dialog", message="Done.", ok_action=Return())
        "Chapter Select":
            window hide
            $ debug_mode =True
            $ renpy.call_screen("chapter1")
        "Sound Test":
            call sound_test
        "Next":
            call debug_mode2
        "Achievement all clear":
            python hide:
                for i in range(0,17):
                    persistent.achievement[i] = True
            $ renpy.call_screen("dialog", message="Done.", ok_action=Return())
        "Achievement all reset":
            python hide:
                for i in range(0,17):
                    persistent.achievement[i] = False
            $ renpy.call_screen("dialog", message="Done.", ok_action=Return())
        "Exit":
            $ renpy.full_restart(transition=None, label="splashscreen")
    call debug_mode
    return()

label debug_mode2:
    menu:
        "Monika Birthday in 2019":
            call monika_birthday
        "Sayori Mad":
            call sayori_mad
        "Special End":
            call specialend
        "Wallace":
            call wallace_main
        "Previous":
            call debug_mode
        "Exit":
            $ renpy.full_restart(transition=None, label="splashscreen")
        "Quit Game":
            $ renpy.quit()
    return()

label sound_test:
    $ music_filename = ""
    $ filelist = ""
    $ music_filelist = config.gamedir + "/music_filelist.txt"
    $ sfx_filelist = config.gamedir + "/sfx_filelist.txt"
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
                    call sound_test
        "Enter Music Filename":
            $ renpy.show_screen("music_tag_input",message="Please enter music filename without \".ogg\".", ok_action=Function(Finishentermusictag))
        "Show Music Filelist":
            python:
                import subprocess
                subprocess.Popen(['start',music_filelist], shell=True)
        "Enter Sfx Filename":
            $ renpy.show_screen("music_tag_input",message="Please enter sfx filename without \".ogg\".", ok_action=Function(Finishentersfxtag))
        "Show Sfx filelist":
            python:
                import subprocess
                subprocess.Popen(['start',sfx_filelist], shell=True)
        "Stop music":
            stop music
        "Voice":
            call voice_test
        "Back":
            call debug_mode
    call sound_test
    return()

label voice_test:
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
            call sound_test
    return()

label voice_sayori_select:
    menu:
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice))
            call voice_sayori_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_sayori_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 05)", ok_action=Function(play_voice))
            call voice_sayori_select
        "Sayori Mad":
            $ set_scene = "_mad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 19)", ok_action=Function(play_voice))
            call voice_sayori_select
        "Normal End":
            $ set_scene = "_normal_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 13)", ok_action=Function(play_voice))
            call voice_sayori_select
        "Back":
            call voice_test
    return()

label voice_natsuki_select:
    menu:
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_natsuki_select
        "chapter 6":
            $ set_scene = "_ch6_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice))
            call voice_natsuki_select
        "chapter 10":
            $ set_scene = "_ch10_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_natsuki_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice))
            call voice_natsuki_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice))
            call voice_sayori_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 04)", ok_action=Function(play_voice))
            call voice_natsuki_select
        "Back":
            call voice_test
    return()

label voice_yuri_select:
    menu:
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_yuri_select
        "chapter 6":
            $ set_scene = "_ch6_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_yuri_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 06)", ok_action=Function(play_voice))
            call voice_yuri_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 08)", ok_action=Function(play_voice))
            call voice_yuri_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 04)", ok_action=Function(play_voice))
            call voice_yuri_select
        "Back":
            call voice_test
    return()

label voice_monika_select:
    menu:
        "chapter 3":
            $ set_scene = "_ch3_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 19)", ok_action=Function(play_voice))
            call voice_monika_select
        "chapter 4":
            $ set_scene = "_ch4_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 07)", ok_action=Function(play_voice))
            call voice_monika_select
        "chapter 5":
            $ set_scene = "_ch5_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 12)", ok_action=Function(play_voice))
            call voice_monika_select
        "chapter 7":
            $ set_scene = "_ch7_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 13)", ok_action=Function(play_voice))
            call voice_monika_select
        "chapter 8":
            $ set_scene = "_ch8_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 15)", ok_action=Function(play_voice))
            call voice_monika_select
        "Next":
            call voice_monika_select2
        "Back":
            call voice_test

label voice_monika_select2:
    menu:
        "chapter 9":
            $ set_scene = "_ch9_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 93)", ok_action=Function(play_voice))
            call voice_monika_select
        "chapter 10":
            $ set_scene = "_ch10_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 172)", ok_action=Function(play_voice))
            call voice_monika_select
        "Bad End":
            $ set_scene = "_bad_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 06)", ok_action=Function(play_voice))
            call voice_monika_select
        "hny":
            $ set_scene = "_hny_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 10)", ok_action=Function(play_voice))
            call voice_monika_select
        "Special End":
            $ set_scene = "_happy_"
            $ renpy.show_screen("voice_num_input",message="Please enter voice number (01 to 09)", ok_action=Function(play_voice))
            call voice_monika_select
        "Previous":
            call voice_monika_select
        "Back":
            call voice_test