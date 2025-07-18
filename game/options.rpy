﻿













define config.name = "Doki Doki Murder Case!"





define gui.show_name = False




define config.version = "1.1.1"





define gui.about = _("")






define build.name = "DDMC"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)



define build.include_update = True












define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
















define config.save_directory = "DDMC"







define config.window_icon = "gui/window_icon.png"



define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"
#define config.console = True


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    build.archive("none_ddmc", "all")
    build.archive("jp_ddmc", "all")
    build.archive("scripts_ddmc", "all")
    build.archive("debug_ddmc", "all")
    build.archive("scripts_discord", "all")

    build.classify("game/script-**.rpyc", "scripts_ddmc")
    build.classify("game/sound_test.rpyc", "scripts_ddmc")
    build.classify("game/**.vbs", "scripts_ddmc")
    build.classify("game/**.ps1", "scripts_ddmc")
    build.classify("game/**.sh", "scripts_ddmc")
    build.classify("game/ddmm_sdk.rpyc", "scripts_ddmc")
    build.classify("game/**.txt", "scripts_ddmc")
    build.classify("game/setupRPC.rpyc", "scripts_discord")
    build.classify("game/splash_additional.rpyc", "scripts_discord")

    build.classify("game/tl/None/**.rpyc", "none_ddmc")
    build.classify("game/tl/None/bgm/**.ogg", "none_ddmc")
    build.classify("game/tl/None/sfx/**.ogg", "none_ddmc")
    build.classify("game/tl/None/gui/**.png", "none_ddmc")
    build.classify("game/images/**.png", "none_ddmc")
    build.classify("game/images/**.webm", "none_ddmc")
    build.classify("game/images/mc.chr", "none_ddmc")
    build.classify("game/bg/**.jpg", "none_ddmc")
    build.classify("game/bg/**.png", "none_ddmc")
    build.classify("game/gui/**.png", "none_ddmc")
    build.classify("game/voice/**", "none_ddmc")
    build.classify("game/mod_assets/**", "none_ddmc")

    build.classify("game/tl/Japanese/**.rpyc", "jp_ddmc")
    build.classify("game/tl/Japanese/gui/**.png", "jp_ddmc")
    build.classify("game/tl/Japanese/gui/overlay/**.png", "jp_ddmc")
    build.classify("game/tl/Japanese/images/bg/**.png", "jp_ddmc")
    build.classify("game/tl/Japanese/images/poem_special/**.png", "jp_ddmc")
    build.classify("game/tl/Japanese/images/**.png", "jp_ddmc")
    build.classify("game/tl/Japanese/bg/**.jpg", "jp_ddmc")
    build.classify("game/**.pdf", "jp_ddmc")
    build.classify("game/tl/Japanese/**.chr", "jp_ddmc")
    build.classify("game/gui/font/**.ttf", "jp_ddmc")
    build.classify("game/gui/font/**.otf", "jp_ddmc")
    build.classify("game/tl/Japanese/sfx/**.ogg", "jp_ddmc")

    build.classify("game/debug", "debug_ddmc")
    build.classify("game/debug.rpyc", "debug_ddmc")
    build.classify("game/chapter_all.rpyc", "debug_ddmc")
    build.classify("game/tl/Japaneswe/debug.rpyc", "debug_ddmc")


    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
