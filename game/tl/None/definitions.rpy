define q = DynamicCharacter('"???"', image='', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mcs = DynamicCharacter('mcs_name', image='', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define config.window_icon = "tl/None/gui/window_icon.png"
default mcs_name = "[player]&Sayori"
define audio.m1b = "<loop 0>tl/None/bgm/m1b.ogg"
define audio.t10s = "<loop 0>tl/None/bgm/10s.ogg"
define audio.t5nr = "<loop 0>tl/None/bgm/5nr.ogg"
define config.save_directory = "DDMC_v430"
#define config.name = "Doki Doki Murder Case! [v4.3.5]"
define audio.t5s = "<loop 4.444>bgm/5_sayori.ogg"
define audio.t5y = "<loop 4.444>bgm/5_yuri.ogg"
define audio.t5n = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.t5m = "<loop 4.444>bgm/5_monika.ogg"
define audio.t3d = "<loop 4.618>tl/None/bgm/3_delayed.ogg"
define audio.smad = "tl/None/bgm/sayori_mad.ogg"
define audio.t1b = "tl/None/bgm/1b.ogg"
define config.rollback_enabled = False
define config.has_voice = True
define ddmc_chapter = 1
define persistent.monikabirth = False
define chibi_title = False
define debug_mode = False
define quick_menu_limit = False
define server_version = ""
define server_version_num = 0
define ddmc_version = 435
define import_name = False
define check_path = ""
define save_path = ""
define rv = ""
define achievement_hint = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
define skip_reload = False
default persistent.normal_end = 0
default persistent.chapter = False
default persistent.chapter_sel = False
default persistent.newyear = False
default persistent.hideusername = False
default persistent.ddmcmod_uninstall = False
default persistent.jppatch_uninstall = False
default persistent.oncedeleted_ddmcmod = False
default persistent.oncedeleted_jppatch = False
default persistent.python_package = False
default persistent.change_name = ""
default persistent.change_language = False
default persistent.delete_pythonpack = False
default persistent.remove_pythonpack = False
default persistent.relaunch = False
default persistent.save_name = True
default persistent.new_name = False
default persistent.save_graphic = False
default persistent.horror_effects = True
default persistent.gamepad = True
default persistent.change_buttons = False
default persistent.chapter_seen = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
default persistent.achievement = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
default persistent.disable_voice = False
default preferences.music_volume = 0.70
default preferences.sfx_volume = 0.70
default preferences.voice_volume = 1.00
default persistent.debug_mode = False
default persistent.newver_skip = False
default persistent.autosave_mode = False
default persistent.cheat_detect = False
image bg stairs = "bg/stairs.jpg"
image bg rooftop = "bg/rooftop.jpg"
image red = "#ff0000"
default w_name = "Wallace"

image m_rectstatic2:
    RectStatic(im.FactorScale(im.Crop("tl/None/gui/logo.png", (100, 100, 128, 128)), 0.25), 2, 32, 32).sm
translate None python:
    mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style='window_mc')
    s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style='window_s', callback=speaker("sayori"))
    m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style='window_m', callback=speaker("monika"))
    n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style='window_n', callback=speaker("natsuki"))
    y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style='window_y', callback=speaker("yuri"))
    q = DynamicCharacter('"???"', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_q')
    mcs = DynamicCharacter('mcs_name', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_mc', callback=speaker("sayori"))

define wa = DynamicCharacter('w_name', image='wallace', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

init python:
    if ("steamapps" in config.basedir.lower()):
        if renpy.windows:
            config.name = "Doki Doki Murder Case! [v4.3.5] (using Steam:playing on Windows)"
        elif renpy.macintosh:
            config.name = "Doki Doki Murder Case! [v4.3.5] (using Steam:playing on Macintosh)"
        elif renpy.linux:
            config.name = "Doki Doki Murder Case! [v4.3.5] (using Steam:playing on Linux)"
        else:
            config.name = "Doki Doki Murder Case! [v4.3.5] (using Steam)"
    else:
        if renpy.windows:
            config.name = "Doki Doki Murder Case! [v4.3.5] (playing on Windows)"
        elif renpy.macintosh:
            config.name = "Doki Doki Murder Case! [v4.3.5] (playing on Macintosh)"
        elif renpy.linux:
            config.name = "Doki Doki Murder Case! [v4.3.5] (playing on Linux)"
        else:
            config.name = "Doki Doki Murder Case! [v4.3.5]"

init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    if persistent.gamepad:
        renpy.game.preferences.pad_enabled = True
    else:
        renpy.game.preferences.pad_enabled = False

image wallace 1:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/a.png")
    zoom 1.25
image wallace 1a:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/a.png")
    zoom 1.25
image wallace 1b:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/b.png")
    zoom 1.25
image wallace 1c:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "mages/wallace/c.png")
    zoom 1.25
image wallace 1d:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/d.png")
    zoom 1.25
image wallace 1e:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/e.png")
    zoom 1.25
image wallace 1f:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/f.png")
    zoom 1.25
image wallace 1g:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/g.png")
    zoom 1.25
image wallace 1h:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/h.png")
    zoom 1.25
image wallace 1i:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/i.png")
    zoom 1.25
image wallace 1j:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/j.png")
    zoom 1.25
image wallace 1k:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/k.png")
    zoom 1.25
image wallace 1l:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/l.png")
    zoom 1.25
image wallace 1m:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/m.png")
    zoom 1.25
image wallace 1n:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/n.png")
    zoom 1.25
image wallace 1o:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/o.png")
    zoom 1.25
image wallace 1p:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/p.png")
    zoom 1.25
image wallace 1q:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/q.png")
    zoom 1.25
image wallace 1s:
    im.Composite((720, 720), (0, -22), "images/wallace/1.png", (0, -22), "images/wallace/s.png")
    zoom 1.25

image sayori mad5 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad5.png")
image sayori mad7 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad7.png")
image sayori mad1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad1.png")
image sayori mad2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad2.png")
image sayori mad3 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad3.png")
image sayori mad4 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad4.png")
image sayori mad6 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad6.png")
image sayori mad8 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sayori_mad/s_mad8.png")

init python:
    def delete_all_savedata():
        delete_all_saves()
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        import os
        try: os.unlink(config.basedir + "/lang")
        except: pass
        try: os.unlink(config.gamedir + "/name")
        except: pass
        try: os.unlink(config.gamedir + "/verskip")
        except: pass
        try:
            print(discordrun)
        except NameError:
            pass
        else:
            import os
            os.popen('taskkill /f /im python.exe')
        renpy.quit()

    #def delete_all_data():
    #    delete_all_saves()
    #    UninstallMod()
    #    renpy.quit()

    def version_check(c_ver):
        import urllib2
        try:
            fp = urllib2.urlopen('http://ddmc.ddlc-jp.com/ddmc_version')
            ver = fp.read()
            fp.close()
            ver_num = int(ver)
        except urllib2.HTTPError, e:
            renpy.notify("Couldn't check for the latest version because the server could not be contacted.")
            ver_num = -999
        except:
            renpy.notify("The version check could not be performed because the server could not be accessed.")
            return True
        if ver_num == -999:
            ver_check = True
            return ver_check
        if c_ver < ver_num:
            ver_check = False
        else:
            ver_check = True
        return ver_check

    def version_check_menu():
        import urllib2
        try:
            fp = urllib2.urlopen('http://ddmc.ddlc-jp.com/ddmc_version')
            ver = fp.read()
            fp.close()
            ver_num = int(ver)
        except urllib2.HTTPError, e:
            ver_num = -999
            e_code = str(e.code)
            renpy.notify(e_code + ':' + e.reason)
        except:
            renpy.show_screen("dialog", message="Connection Error!\nThe version check could not be performed because the server could not be accessed.\nIf it does not improve even after waiting, please contact the creator's X.(@horizonmayone)", ok_action=Hide("dialog"))
            return
        if ver_num == -999:
            renpy.show_screen("dialog", message="Connection Error!\nIf it does not improve even after waiting, please contact the creator's X.(@horizonmayone)", ok_action=Hide("dialog"))
            return
        if ddmc_version < ver_num:
            ver_check = False
        else:
            ver_check = True
        if not ver_check:
            if renpy.windows:
                renpy.show_screen("confirm", message="New version was found! Would you like to download now?", yes_action=[Hide("confirm"), Show(screen="dialog", message="Do not close the game while it is downloading.",ok_action=Function(get_newversion_vbs))], no_action=Hide("confirm"))
            elif renpy.linux:
                renpy.show_screen("confirm", message="New version was found! Would you like to download now?", yes_action=[Hide("confirm"), Show(screen="dialog", message="Do not close the game while it is downloading.",ok_action=Function(get_newversion_shellscript))], no_action=Hide("confirm"))
            elif renpy.macintosh:
                renpy.show_screen("confirm", message="New version was found! Would you like to download now?", yes_action=[Hide("confirm"), Show(screen="dialog", message="Do not close the game while it is downloading.",ok_action=Function(get_newversion_shellscript_mac))], no_action=Hide("confirm"))
            else:
                renpy.show_screen("confirm", message="New version was found! Would you like to download now?", yes_action=[Function(get_newversion_data),Hide("confirm"),Show(screen="dialog", message="Quit the game. After downloading and updating the patch, please launch the game again.", ok_action=Quit(confirm=False))], no_action=Hide("confirm"))
        else:
            renpy.show_screen("dialog", message="This version is new!", ok_action=Hide("dialog"))

    def get_newversion_data():
        import urllib2
        fp = urllib2.urlopen('http://ddmc.ddlc-jp.com/download_new_num')
        num = fp.read()
        fp.close()
        download_url = "https://ddmc.ddlc-jp.com/download/download.php?download=" + num
        import webbrowser
        webbrowser.open(download_url)
    
    def get_newversion_vbs():
        #open(config.basedir + "/download.vbs", "w").write(renpy.file("download.vbs").read())
        open(config.basedir + "/download.ps1", "w").write(renpy.file("download.ps1").read())
        import os
        import subprocess
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        #cmd = "cscript " + config.basedir + "\\download.vbs"
        cmd = "powershell -ExecutionPolicy RemoteSigned -File \"" + config.basedir + "\\download.ps1\""
        subprocess.call(cmd, startupinfo=si, shell=True)
        #try: os.unlink(config.basedir + "/download.vbs")
        try: os.unlink(config.basedir + "/download.ps1")
        except: pass
        get_newversion_download_check()

    def get_newversion_shellscript():
        open(config.basedir + "/download.sh", "w").write(renpy.file("download.sh").read())
        import os
        import subprocess
        os.chmod(config.basedir + "/download.sh", 0777)
        cmd = config.basedir + "/download.sh > download_status"
        subprocess.call([cmd, "arguments"], shell=True)
        try: os.unlink(config.basedir + "/download.sh")
        except: pass
        get_newversion_download_check()

    def get_newversion_shellscript_mac():
        import os
        macuser = ""
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    macuser = user
        except:
            pass
        open("/Users/" + macuser + "/Desktop/download.sh", "w").write(renpy.file("download.sh").read())
        import subprocess
        os.chmod("/Users/" + macuser + "/Desktop/download.sh", 0777)
        cmd = "cd ~/Desktop && /Users/" + macuser + "/Desktop/download.sh > /Users/" + macuser + "/Desktop/download_status"
        subprocess.call([cmd, "arguments"], shell=True)
        try: os.unlink("/Users/" + macuser + "/Desktop/download.sh")
        except: pass
        get_newversion_download_check()

    def get_newversion_download_check():
        renpy.hide_screen("confirm")
        renpy.hide_screen("dialog")
        if renpy.macintosh:
            macuser = ""
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        macuser = user
            except:
                pass
            is_file = os.path.isfile("/Users/" + macuser + "/Desktop/download_status")
            if is_file:
                if open("/Users/" + macuser + "/Desktop/download_status", "r").read() == "200":
                    renpy.show_screen("dialog", message="Quit the game. After downloading and updating the patch, please launch the game again.\nSaved latest.zip to your desktop folder.", ok_action=Quit(confirm=False))
                else:
                    try: os.unlink("/Users/" + macuser + "/Desktop/latest.zip")
                    except: pass
                    renpy.notify("Error code:" + open("/Users/" + macuser + "/Desktop/download_status", "r").read())
                    renpy.show_screen("dialog", message="An error occurred while downloading.\nIf you can't do it again, please contact the creator's X(@horizonmayone).", ok_action=Hide("dialog"))
                try: os.unlink("/Users/" + macuser + "/Desktop/download_status")
                except: pass
            else:
                renpy.show_screen("dialog", message="An error occurred while downloading.\nIf you can't do it again, please contact the creator's X(@horizonmayone).", ok_action=Hide("dialog"))
        else:
            if renpy.loadable("../download_status"):
                import re
                status = re.sub(r"\D", "", open(renpy.config.basedir + '/download_status', "r").read())
                if status == "200":
                    renpy.show_screen("dialog", message="Quit the game. After downloading and updating the patch, please launch the game again.", ok_action=Quit(confirm=False))
                else:
                    try: os.unlink(config.basedir + "/latest.zip")
                    except: pass
                    renpy.notify("Error code:" + status)
                    renpy.show_screen("dialog", message="An error occurred while downloading.\nIf you can't do it again, please contact the creator's X(@horizonmayone).", ok_action=Hide("dialog"))
                try: os.unlink(config.basedir + "/download_status")
                except: pass
            else:
                renpy.show_screen("dialog", message="An error occurred while downloading.\nIf you can't do it again, please contact the creator's X(@horizonmayone).", ok_action=Hide("dialog"))

    #def import_ddlc_player_name():
    #    renpy.show_screen("confirm", message="Would you like to import DDLC's player name?", yes_action=[Hide("confirm"),Function(get_ddlc_player_name)], no_action=Hide("confirm"))

    def get_ddlc_player_name():
        from renpy.loadsave import dump, loads

        import glob


        if renpy.macintosh:
            rv = "~/Library/RenPy/"
            check_path = os.path.expanduser(rv)

        elif renpy.windows:
            if 'APPDATA' in os.environ:
                check_path =  os.environ['APPDATA'] + "/RenPy/"
            else:
                rv = "~/RenPy/"
                check_path = os.path.expanduser(rv)

        else:
            rv = "~/.renpy/"
            check_path = os.path.expanduser(rv)

        save_path=glob.glob(check_path + 'DDLC/persistent')
        if not save_path:
            save_path=glob.glob(check_path + 'DDLC-*/persistent')

        if save_path:
            save_path=save_path[0]
            from renpy.loadsave import dump, loads
            f=file(save_path,"rb")
            s=f.read().decode("zlib")
            f.close()

            ddlc_persistent=loads(s)

            if ddlc_persistent.playername != "":
                persistent.playername = ddlc_persistent.playername
                player = ddlc_persistent.playername
                renpy.save_persistent()
                if persistent.save_name:
                    SaveName()
                renpy.show_screen("dialog", message="Reload the game to reflect the player name.", ok_action=Function(restart_game_ddmc))
            else:
                renpy.show_screen("dialog", message="DDLC's player name was not found.", ok_action=Hide("dialog"))
        
        else:
            renpy.show_screen("dialog", message="DDLC's save data was not found.", ok_action=Hide("dialog"))

    def autoload_ddmc():
        if renpy.can_load('autosave'):
            renpy.load('autosave')
        else:
            renpy.show_screen("dialog", message="Autosave was not found.", ok_action=Hide("dialog"))
    
    def delete_autosave_ddmc():
        if renpy.can_load('autosave'):
            renpy.unlink_save('autosave')
            if not renpy.can_load('autosave'):
                renpy.show_screen("dialog", message="Autosave was deleted.", ok_action=Hide("dialog"))
            else:
                renpy.show_screen("dialog", message="Autosave was not deleted.", ok_action=Hide("dialog"))
        else:
            renpy.show_screen("dialog", message="Autosave was not found.", ok_action=Hide("dialog"))

# Sayori
# definitions of Sayori's expression parts
image s_eye_0:
    "mod_assets/s_animation/s_eye_a.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/s_animation/s_eye_q.png"
    0.1
    repeat
image s_eye_1:
    "mod_assets/s_animation/s_eye_k.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/s_animation/s_eye_q.png"
    0.1
    repeat
image s_eye_2:
    "mod_assets/s_animation/s_eye_m.png"
    choice:
        3.0
    choice:
        2.5
    choice:
        1.0
    "mod_assets/s_animation/s_eye_q.png"
    0.1
    repeat
image s_eye_3:
    "mod_assets/s_animation/s_eye_t.png"
    choice:
        5.5
    choice:
        2.5
    choice:
        1.5
    "mod_assets/s_animation/s_eye_q.png"
    0.1
    repeat
image s_eye_4:
    "mod_assets/s_animation/s_eye_3a.png"
    choice:
        4.5
    choice:
        2.5
    choice:
        1.5
    "mod_assets/s_animation/s_eye_3.png"
    0.1
    repeat
image s_eye_5:
    "mod_assets/s_animation/s_eye_3b.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.0
    "mod_assets/s_animation/s_eye_3.png"
    0.1
    repeat

image s_mouth_0:
    "mod_assets/s_animation/s_mouth_l.png"
    0.15
    "mod_assets/s_animation/s_mouth_a.png"
    0.15
    repeat
image s_mouth_1 = "mod_assets/s_animation/s_mouth_a.png"
image s_mouth_2 = "mod_assets/s_animation/s_mouth_b.png"
image s_mouth_3:
    "mod_assets/s_animation/s_mouth_c.png"
    0.15
    "mod_assets/s_animation/s_mouth_e.png"
    0.15
    repeat
image s_mouth_4:
    "mod_assets/s_animation/s_mouth_c.png"
    0.15
    "mod_assets/s_animation/s_mouth_e.png"
    0.15
    repeat
image s_mouth_5 = "mod_assets/s_animation/s_mouth_e.png"
image s_mouth_6 = "mod_assets/s_animation/s_mouth_f.png"
image s_mouth_7:
    "mod_assets/s_animation/s_mouth_m.png"
    0.15
    "mod_assets/s_animation/s_mouth_c.png"
    0.15
    repeat
image s_mouth_8 = "mod_assets/s_animation/s_mouth_m.png"
image s_mouth_9 = "mod_assets/s_animation/s_mouth_l.png"
image s_mouth_10:
    "mod_assets/s_animation/s_mouth_x.png"
    0.15
    "mod_assets/s_animation/s_mouth_a.png"
    0.15
    repeat
image s_mouth_11 = "mod_assets/s_animation/s_mouth_x.png"

image s_mouth_3a = "mod_assets/s_animation/s_mouth_3a.png"
image s_mouth_3b:
    "mod_assets/s_animation/s_mouth_3a.png"
    0.15
    "mod_assets/s_animation/s_mouth_3b.png"
    0.15
    repeat
image s_mouth_3c = "mod_assets/s_animation/s_mouth_3c.png"
image s_mouth_3d:
    "mod_assets/s_animation/s_mouth_3c.png"
    0.15
    "mod_assets/s_animation/s_mouth_3d.png"
    0.15
    repeat

# building Sayori's face animations
image sayori_a =LiveComposite((960,960),(0,1),"sayori/a.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_1"))
image sayori_b =LiveComposite((960,960),(0,1),"sayori/b.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_2"))
image sayori_c =LiveComposite((960,960),(0,1),"sayori/c.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_2"))
image sayori_d =LiveComposite((960,960),(0,1),"sayori/d.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_1"))
image sayori_e =LiveComposite((960,960),(0,1),"sayori/e.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_5"))
image sayori_f =LiveComposite((960,960),(0,1),"sayori/f.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_6"))
image sayori_g =LiveComposite((960,960),(0,1),"sayori/g.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_6"))
image sayori_h =LiveComposite((960,960),(0,1),"sayori/h.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_6"))
image sayori_i =LiveComposite((960,960),(0,1),"sayori/i.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_2"))
image sayori_j =LiveComposite((960,960),(0,1),"sayori/j.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_6"))
image sayori_k =LiveComposite((960,960),(0,1),"sayori/k.png",(0,1),"s_eye_1",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_6"))
image sayori_l =LiveComposite((960,960),(0,1),"sayori/l.png",(0,1),"s_eye_1",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_9"))
image sayori_m =LiveComposite((960,960),(0,1),"sayori/m.png",(0,1),"s_eye_2",(0,1),WhileSpeaking("sayori","s_mouth_7","s_mouth_8"))
image sayori_n =LiveComposite((960,960),(0,1),"sayori/n.png",(0,1),"s_eye_2",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_5"))
image sayori_o =LiveComposite((960,960),(0,1),"sayori/o.png",(0,1),"s_eye_2",(0,1),WhileSpeaking("sayori","s_mouth_3","s_mouth_5"))
image sayori_p =LiveComposite((960,960),(0,1),"sayori/p.png",(0,1),WhileSpeaking("sayori","s_mouth_7","s_mouth_8"))
image sayori_q =LiveComposite((960,960),(0,1),"sayori/q.png",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_1"))
image sayori_r =LiveComposite((960,960),(0,1),"sayori/r.png",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_9"))
image sayori_s =LiveComposite((960,960),(0,1),"sayori/s.png",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_9"))
image sayori_t =LiveComposite((960,960),(0,1),"sayori/t.png",(0,1),"s_eye_3",(0,1),WhileSpeaking("sayori","s_mouth_2","s_mouth_1"))
image sayori_u =LiveComposite((960,960),(0,1),"sayori/u.png",(0,1),"s_eye_3",(0,1),WhileSpeaking("sayori","s_mouth_2","s_mouth_6"))
image sayori_v =LiveComposite((960,960),(0,1),"sayori/v.png",(0,1),"s_eye_3",(0,1),WhileSpeaking("sayori","s_mouth_2","s_mouth_6"))
image sayori_w =LiveComposite((960,960),(0,1),"sayori/w.png",(0,1),"s_eye_3",(0,1),WhileSpeaking("sayori","s_mouth_7","s_mouth_8"))
image sayori_x =LiveComposite((960,960),(0,1),"sayori/x.png",(0,1),"s_eye_0",(0,1),WhileSpeaking("sayori","s_mouth_10","s_mouth_11"))
image sayori_y =LiveComposite((960,960),(0,1),"sayori/y.png",(0,1),"s_eye_1",(0,1),WhileSpeaking("sayori","s_mouth_0","s_mouth_1"))

image sayori 1 = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_a")
image sayori 1a = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_a")
image sayori 1b = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_b")
image sayori 1c = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_c")
image sayori 1d = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_d")
image sayori 1e = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_e")
image sayori 1f = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_f")
image sayori 1g = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_g")
image sayori 1h = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_h")
image sayori 1i = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_i")
image sayori 1j = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_j")
image sayori 1k = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_k")
image sayori 1l = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_l")
image sayori 1m = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_m")
image sayori 1n = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_n")
image sayori 1o = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_o")
image sayori 1p = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_p")
image sayori 1q = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_q")
image sayori 1r = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_r")
image sayori 1s = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_s")
image sayori 1t = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_t")
image sayori 1u = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_u")
image sayori 1v = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_v")
image sayori 1w = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_w")
image sayori 1x = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_x")
image sayori 1y = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_y")

image sayori 2 = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_a")
image sayori 2a = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_a")
image sayori 2b = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_b")
image sayori 2c = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_c")
image sayori 2d = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_d")
image sayori 2e = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_e")
image sayori 2f = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_f")
image sayori 2g = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_g")
image sayori 2h = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_h")
image sayori 2i = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_i")
image sayori 2j = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_j")
image sayori 2k = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_k")
image sayori 2l = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_l")
image sayori 2m = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_m")
image sayori 2n = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_n")
image sayori 2o = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_o")
image sayori 2p = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_p")
image sayori 2q = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_q")
image sayori 2r = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_r")
image sayori 2s = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_s")
image sayori 2t = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_t")
image sayori 2u = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_u")
image sayori 2v = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_v")
image sayori 2w = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_w")
image sayori 2x = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_x")
image sayori 2y = LiveComposite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_y")

image sayori 3 = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_a")
image sayori 3a = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_a")
image sayori 3b = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_b")
image sayori 3c = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_c")
image sayori 3d = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_d")
image sayori 3e = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_e")
image sayori 3f = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_f")
image sayori 3g = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_g")
image sayori 3h = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_h")
image sayori 3i = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_i")
image sayori 3j = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_j")
image sayori 3k = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_k")
image sayori 3l = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_l")
image sayori 3m = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_m")
image sayori 3n = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_n")
image sayori 3o = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_o")
image sayori 3p = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_p")
image sayori 3q = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_q")
image sayori 3r = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_r")
image sayori 3s = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_s")
image sayori 3t = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_t")
image sayori 3u = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_u")
image sayori 3v = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_v")
image sayori 3w = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_w")
image sayori 3x = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_x")
image sayori 3y = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori_y")

image sayori 4 = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_a")
image sayori 4a = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_a")
image sayori 4b = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_b")
image sayori 4c = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_c")
image sayori 4d = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_d")
image sayori 4e = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_e")
image sayori 4f = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_f")
image sayori 4g = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_g")
image sayori 4h = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_h")
image sayori 4i = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_i")
image sayori 4j = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_j")
image sayori 4k = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_k")
image sayori 4l = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_l")
image sayori 4m = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_m")
image sayori 4n = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_n")
image sayori 4o = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_o")
image sayori 4p = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_p")
image sayori 4q = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_q")
image sayori 4r = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_r")
image sayori 4s = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_s")
image sayori 4t = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_t")
image sayori 4u = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_u")
image sayori 4v = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_v")
image sayori 4w = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_w")
image sayori 4x = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_x")
image sayori 4y = LiveComposite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori_y")

image sayori 5 = LiveComposite((960, 960), (0, 0), "sayori/3a.png",(0,0),"s_eye_4",(0,0),WhileSpeaking("sayori","s_mouth_3b","s_mouth_3a"))
image sayori 5a = LiveComposite((960, 960), (0, 0), "sayori/3a.png",(0,0),"s_eye_4",(0,0),WhileSpeaking("sayori","s_mouth_3b","s_mouth_3a"))
image sayori 5b = LiveComposite((960, 960), (0, 0), "sayori/3b.png",(0,0),"s_eye_5",(0,0),WhileSpeaking("sayori","s_mouth_3b","s_mouth_3a"))
image sayori 5c = LiveComposite((960, 960), (0, 0), "sayori/3c.png",(0,0),"s_eye_4",(0,0),WhileSpeaking("sayori","s_mouth_3d","s_mouth_3c"))
image sayori 5d = LiveComposite((960, 960), (0, 0), "sayori/3d.png",(0,0),"s_eye_5",(0,0),WhileSpeaking("sayori","s_mouth_3d","s_mouth_3c"))

image sayori 1ba = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_a")
image sayori 1bb = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_b")
image sayori 1bc = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_c")
image sayori 1bd = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_d")
image sayori 1be = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_e")
image sayori 1bf = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_f")
image sayori 1bg = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_g")
image sayori 1bh = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_h")
image sayori 1bi = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_i")
image sayori 1bj = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_j")
image sayori 1bk = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_k")
image sayori 1bl = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_l")
image sayori 1bm = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_m")
image sayori 1bn = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_n")
image sayori 1bo = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_o")
image sayori 1bp = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_p")
image sayori 1bq = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_q")
image sayori 1br = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_r")
image sayori 1bs = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_s")
image sayori 1bt = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_t")
image sayori 1bu = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_u")
image sayori 1bv = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_v")
image sayori 1bw = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_w")
image sayori 1bx = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_x")
image sayori 1by = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_y")

image sayori 2ba = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_a")
image sayori 2bb = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_b")
image sayori 2bc = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_c")
image sayori 2bd = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_d")
image sayori 2be = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_e")
image sayori 2bf = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_f")
image sayori 2bg = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_g")
image sayori 2bh = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_h")
image sayori 2bi = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_i")
image sayori 2bj = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_j")
image sayori 2bk = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_k")
image sayori 2bl = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_l")
image sayori 2bm = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_m")
image sayori 2bn = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_n")
image sayori 2bo = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_o")
image sayori 2bp = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_p")
image sayori 2bq = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_q")
image sayori 2br = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_r")
image sayori 2bs = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_s")
image sayori 2bt = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_t")
image sayori 2bu = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_u")
image sayori 2bv = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_v")
image sayori 2bw = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_w")
image sayori 2bx = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_x")
image sayori 2by = LiveComposite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_y")

image sayori 3ba = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_a")
image sayori 3bb = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_b")
image sayori 3bc = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_c")
image sayori 3bd = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_d")
image sayori 3be = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_e")
image sayori 3bf = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_f")
image sayori 3bg = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_g")
image sayori 3bh = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_h")
image sayori 3bi = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_i")
image sayori 3bj = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_j")
image sayori 3bk = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_k")
image sayori 3bl = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_l")
image sayori 3bm = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_m")
image sayori 3bn = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_n")
image sayori 3bo = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_o")
image sayori 3bp = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_p")
image sayori 3bq = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_q")
image sayori 3br = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_r")
image sayori 3bs = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_s")
image sayori 3bt = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_t")
image sayori 3bu = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_u")
image sayori 3bv = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_v")
image sayori 3bw = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_w")
image sayori 3bx = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_x")
image sayori 3by = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori_y")

image sayori 4ba = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_a")
image sayori 4bb = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_b")
image sayori 4bc = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_c")
image sayori 4bd = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_d")
image sayori 4be = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_e")
image sayori 4bf = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_f")
image sayori 4bg = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_g")
image sayori 4bh = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_h")
image sayori 4bi = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_i")
image sayori 4bj = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_j")
image sayori 4bk = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_k")
image sayori 4bl = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_l")
image sayori 4bm = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_m")
image sayori 4bn = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_n")
image sayori 4bo = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_o")
image sayori 4bp = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_p")
image sayori 4bq = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_q")
image sayori 4br = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_r")
image sayori 4bs = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_s")
image sayori 4bt = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_t")
image sayori 4bu = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_u")
image sayori 4bv = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_v")
image sayori 4bw = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_w")
image sayori 4bx = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_x")
image sayori 4by = LiveComposite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori_y")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat


# Natsuki
# Natsuki's face expressions
image n_eye_0:
    "mod_assets/n_animation/n_eye_a.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/n_animation/n_eye_w.png"
    0.1
    repeat
image n_eye_1:
    "mod_assets/n_animation/n_eye_o.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/n_animation/n_eye_w'.png"
    0.1
    repeat
image n_eye_2:
    "mod_assets/n_animation/n_eye_q.png"
    choice:
        3.0
    choice:
        2.5
    choice:
        1.0
    "mod_assets/n_animation/n_eye_w''.png"
    0.1
    repeat
image n_eye_3:
    "mod_assets/n_animation/n_eye_2bt.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/n_animation/n_eye_2btc.png"
    0.1
    repeat
image n_eye_4:
    "mod_assets/n_animation/n_eye_2btg.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/n_animation/n_eye_2btd.png"
    0.1
    repeat
image n_eye_5:
    "mod_assets/n_animation/n_eye_2bth.png"
    choice:
        5.0
    choice:
        4.0
    choice:
        3.0
    "mod_assets/n_animation/n_eye_2btf.png"
    0.1
    repeat

image n_mouth_0 = "mod_assets/n_animation/n_mouth_a.png"
image n_mouth_1 = "mod_assets/n_animation/n_mouth_b.png"
image n_mouth_2 = "mod_assets/n_animation/n_mouth_c.png"
image n_mouth_3 = "mod_assets/n_animation/n_mouth_d.png"
image n_mouth_4 = "mod_assets/n_animation/n_mouth_f.png"
image n_mouth_5 = "mod_assets/n_animation/n_mouth_g.png"
image n_mouth_6 = "mod_assets/n_animation/n_mouth_p.png"
image n_mouth_7 = "mod_assets/n_animation/n_mouth_z.png"
image n_mouth_8:
    "mod_assets/n_animation/n_mouth_b.png"
    0.15
    "mod_assets/n_animation/n_mouth_c.png"
    0.15
    repeat
image n_mouth_9:
    "mod_assets/n_animation/n_mouth_d.png"
    0.15
    "mod_assets/n_animation/n_mouth_a.png"
    0.15
    repeat
image n_mouth_10:
    "mod_assets/n_animation/n_mouth_p.png"
    0.15
    "mod_assets/n_animation/n_mouth_c.png"
    0.15
    repeat
image n_mouth_11:
    "mod_assets/n_animation/n_mouth_c.png"
    0.15
    "mod_assets/n_animation/n_mouth_g.png"
    0.15
    repeat
image n_mouth_12 = "mod_assets/n_animation/n_mouth_2bt.png"
image n_mouth_13 = "mod_assets/n_animation/n_mouth_2btd.png"
image n_mouth_14:
    "mod_assets/n_animation/n_mouth_2btc.png"
    0.15
    "mod_assets/n_animation/n_mouth_2bt.png"
    0.15
    repeat
image n_mouth_scream:
    "mod_assets/n_animation/n_mouth_scream.png"
    0.15
    "mod_assets/n_animation/n_mouth_f.png"
    0.15
    repeat


# building Natsuki's face animations
image natsuki_2bt =LiveComposite((960,960),(0,1),"natsuki/2bt.png",(0,1),"n_eye_3",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2bta=LiveComposite((960,960),(0,1),"natsuki/2bta.png",(0,1),"n_eye_3",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2btb=LiveComposite((960,960),(0,1),"natsuki/2btb.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2btc=LiveComposite((960,960),(0,1),"natsuki/2btc.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2btd=LiveComposite((960,960),(0,1),"natsuki/2btd.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2bte=LiveComposite((960,960),(0,1),"natsuki/2bte.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2btf=LiveComposite((960,960),(0,1),"natsuki/2btf.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2btg=LiveComposite((960,960),(0,1),"natsuki/2btg.png",(0,1),"n_eye_4",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2bth=LiveComposite((960,960),(0,1),"natsuki/2bth.png",(0,1),"n_eye_5",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2bti=LiveComposite((960,960),(0,1),"natsuki/2bti.png",(0,1),"n_eye_5",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2t  =LiveComposite((960,960),(0,1),"natsuki/2t.png",(0,1),"n_eye_3",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2ta =LiveComposite((960,960),(0,1),"natsuki/2ta.png",(0,1),"n_eye_3",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2tb =LiveComposite((960,960),(0,1),"natsuki/2tb.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2tc =LiveComposite((960,960),(0,1),"natsuki/2tc.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2td =LiveComposite((960,960),(0,1),"natsuki/2td.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2te =LiveComposite((960,960),(0,1),"natsuki/2te.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_2tf =LiveComposite((960,960),(0,1),"natsuki/2tf.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2tg =LiveComposite((960,960),(0,1),"natsuki/2tg.png",(0,1),"n_eye_4",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2th =LiveComposite((960,960),(0,1),"natsuki/2th.png",(0,1),"n_eye_5",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_13"))
image natsuki_2ti =LiveComposite((960,960),(0,1),"natsuki/2ti.png",(0,1),"n_eye_5",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_14","n_mouth_12"))
image natsuki_a =LiveComposite((960,960),(0,1),"natsuki/a.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_0"))
image natsuki_b =LiveComposite((960,960),(0,1),"natsuki/b.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_1"))
image natsuki_c =LiveComposite((960,960),(0,1),"natsuki/c.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_2"))
image natsuki_d =LiveComposite((960,960),(0,1),"natsuki/d.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_9","n_mouth_3"))
image natsuki_e =LiveComposite((960,960),(0,1),"natsuki/e.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_1"))
image natsuki_f =LiveComposite((960,960),(0,1),"natsuki/f.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_4"))
image natsuki_g =LiveComposite((960,960),(0,1),"natsuki/g.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_11","n_mouth_5"))
image natsuki_h =LiveComposite((960,960),(0,1),"natsuki/h.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_2"))
image natsuki_i =LiveComposite((960,960),(0,1),"natsuki/i.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_11","n_mouth_5"))
image natsuki_j =LiveComposite((960,960),(0,1),"natsuki/j.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_0"))
image natsuki_k =LiveComposite((960,960),(0,1),"natsuki/k.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_2"))
image natsuki_l =LiveComposite((960,960),(0,1),"natsuki/l.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_9","n_mouth_3"))
image natsuki_m =LiveComposite((960,960),(0,1),"natsuki/m.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_2"))
image natsuki_n =LiveComposite((960,960),(0,1),"natsuki/n.png",(0,1),"n_eye_0",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_11","n_mouth_5"))
image natsuki_o =LiveComposite((960,960),(0,1),"natsuki/o.png",(0,1),"n_eye_1",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_4"))
image natsuki_p =LiveComposite((960,960),(0,1),"natsuki/p.png",(0,1),"n_eye_1",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_6"))
image natsuki_q =LiveComposite((960,960),(0,1),"natsuki/q.png",(0,1),"n_eye_2",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_2"))
image natsuki_r =LiveComposite((960,960),(0,1),"natsuki/r.png",(0,1),"n_eye_2",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_4"))
image natsuki_s =LiveComposite((960,960),(0,1),"natsuki/s.png",(0,1),"n_eye_2",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_11","n_mouth_5"))
image natsuki_t =LiveComposite((960,960),(0,1),"natsuki/t.png",(0,1),"n_eye_2",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_9","n_mouth_3"))
image natsuki_u =LiveComposite((960,960),(0,1),"natsuki/u.png",(0,1),"n_eye_2",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_11","n_mouth_5"))
image natsuki_v =LiveComposite((960,960),(0,1),"natsuki/v.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_6"))
image natsuki_w =LiveComposite((960,960),(0,1),"natsuki/w.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_8","n_mouth_1"))
image natsuki_x =LiveComposite((960,960),(0,1),"natsuki/x.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_10","n_mouth_4"))
image natsuki_y =LiveComposite((960,960),(0,1),"natsuki/y.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_9","n_mouth_3"))
image natsuki_z =LiveComposite((960,960),(0,1),"natsuki/z.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_9","n_mouth_7"))
image natsuki_1t= "natsuki_a"
image natsuki_4t= "natsuki/old2/4t.png"
image natsuki_scream =LiveComposite((960,960),(0,1),"natsuki/scream.png",(0,1),WhileSpeaking("natsuki" or "nat&yuri","n_mouth_scream","n_mouth_4"))

image natsuki 11 = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_1t")
image natsuki 1a = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_a")
image natsuki 1b = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_b")
image natsuki 1c = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_c")
image natsuki 1d = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_d")
image natsuki 1e = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_e")
image natsuki 1f = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_f")
image natsuki 1g = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_g")
image natsuki 1h = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_h")
image natsuki 1i = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_i")
image natsuki 1j = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_j")
image natsuki 1k = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_k")
image natsuki 1l = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_l")
image natsuki 1m = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_m")
image natsuki 1n = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_n")
image natsuki 1o = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_o")
image natsuki 1p = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_p")
image natsuki 1q = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_q")
image natsuki 1r = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_r")
image natsuki 1s = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_s")
image natsuki 1t = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_t")
image natsuki 1u = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_u")
image natsuki 1v = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_v")
image natsuki 1w = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_w")
image natsuki 1x = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_x")
image natsuki 1y = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_y")
image natsuki 1z = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_z")

image natsuki 21 = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_1t")
image natsuki 2a = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_a")
image natsuki 2b = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_b")
image natsuki 2c = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_c")
image natsuki 2d = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_d")
image natsuki 2e = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_e")
image natsuki 2f = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_f")
image natsuki 2g = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_g")
image natsuki 2h = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_h")
image natsuki 2i = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_i")
image natsuki 2j = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_j")
image natsuki 2k = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_k")
image natsuki 2l = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_l")
image natsuki 2m = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_m")
image natsuki 2n = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_n")
image natsuki 2o = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_o")
image natsuki 2p = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_p")
image natsuki 2q = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_q")
image natsuki 2r = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_r")
image natsuki 2s = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_s")
image natsuki 2t = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_t")
image natsuki 2u = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_u")
image natsuki 2v = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_v")
image natsuki 2w = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_w")
image natsuki 2x = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_x")
image natsuki 2y = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_y")
image natsuki 2z = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_z")

image natsuki 31 = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_1t")
image natsuki 3a = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_a")
image natsuki 3b = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_b")
image natsuki 3c = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_c")
image natsuki 3d = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_d")
image natsuki 3e = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_e")
image natsuki 3f = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_f")
image natsuki 3g = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_g")
image natsuki 3h = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_h")
image natsuki 3i = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_i")
image natsuki 3j = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_j")
image natsuki 3k = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_k")
image natsuki 3l = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_l")
image natsuki 3m = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_m")
image natsuki 3n = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_n")
image natsuki 3o = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_o")
image natsuki 3p = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_p")
image natsuki 3q = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_q")
image natsuki 3r = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_r")
image natsuki 3s = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_s")
image natsuki 3t = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_t")
image natsuki 3u = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_u")
image natsuki 3v = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_v")
image natsuki 3w = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_w")
image natsuki 3x = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_x")
image natsuki 3y = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_y")
image natsuki 3z = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_z")

image natsuki 41 = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_1t")
image natsuki 4a = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_a")
image natsuki 4b = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_b")
image natsuki 4c = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_c")
image natsuki 4d = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_d")
image natsuki 4e = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_e")
image natsuki 4f = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_f")
image natsuki 4g = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_g")
image natsuki 4h = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_h")
image natsuki 4i = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_i")
image natsuki 4j = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_j")
image natsuki 4k = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_k")
image natsuki 4l = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_l")
image natsuki 4m = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_m")
image natsuki 4n = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_n")
image natsuki 4o = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_o")
image natsuki 4p = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_p")
image natsuki 4q = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_q")
image natsuki 4r = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_r")
image natsuki 4s = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_s")
image natsuki 4t = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_t")
image natsuki 4u = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_u")
image natsuki 4v = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_v")
image natsuki 4w = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_w")
image natsuki 4x = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_x")
image natsuki 4y = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_y")
image natsuki 4z = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_z")

image natsuki 12 = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2t")
image natsuki 12a = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2ta")
image natsuki 12b = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2tb")
image natsuki 12c = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2tc")
image natsuki 12d = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2td")
image natsuki 12e = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2te")
image natsuki 12f = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2tf")
image natsuki 12g = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2tg")
image natsuki 12h = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2th")
image natsuki 12i = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_2ti")

image natsuki 42 = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2t")
image natsuki 42a = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2ta")
image natsuki 42b = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2tb")
image natsuki 42c = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2tc")
image natsuki 42d = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2td")
image natsuki 42e = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2te")
image natsuki 42f = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2tf")
image natsuki 42g = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2tg")
image natsuki 42h = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2th")
image natsuki 42i = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_2ti")

image natsuki 51 = LiveComposite((960, 960), (18, 22), "natsuki_1t", (0, 0), "natsuki/3.png")
image natsuki 5a = LiveComposite((960, 960), (18, 22), "natsuki_a", (0, 0), "natsuki/3.png")
image natsuki 5b = LiveComposite((960, 960), (18, 22), "natsuki_b", (0, 0), "natsuki/3.png")
image natsuki 5c = LiveComposite((960, 960), (18, 22), "natsuki_c", (0, 0), "natsuki/3.png")
image natsuki 5d = LiveComposite((960, 960), (18, 22), "natsuki_d", (0, 0), "natsuki/3.png")
image natsuki 5e = LiveComposite((960, 960), (18, 22), "natsuki_e", (0, 0), "natsuki/3.png")
image natsuki 5f = LiveComposite((960, 960), (18, 22), "natsuki_f", (0, 0), "natsuki/3.png")
image natsuki 5g = LiveComposite((960, 960), (18, 22), "natsuki_g", (0, 0), "natsuki/3.png")
image natsuki 5h = LiveComposite((960, 960), (18, 22), "natsuki_h", (0, 0), "natsuki/3.png")
image natsuki 5i = LiveComposite((960, 960), (18, 22), "natsuki_i", (0, 0), "natsuki/3.png")
image natsuki 5j = LiveComposite((960, 960), (18, 22), "natsuki_j", (0, 0), "natsuki/3.png")
image natsuki 5k = LiveComposite((960, 960), (18, 22), "natsuki_k", (0, 0), "natsuki/3.png")
image natsuki 5l = LiveComposite((960, 960), (18, 22), "natsuki_l", (0, 0), "natsuki/3.png")
image natsuki 5m = LiveComposite((960, 960), (18, 22), "natsuki_m", (0, 0), "natsuki/3.png")
image natsuki 5n = LiveComposite((960, 960), (18, 22), "natsuki_n", (0, 0), "natsuki/3.png")
image natsuki 5o = LiveComposite((960, 960), (18, 22), "natsuki_o", (0, 0), "natsuki/3.png")
image natsuki 5p = LiveComposite((960, 960), (18, 22), "natsuki_p", (0, 0), "natsuki/3.png")
image natsuki 5q = LiveComposite((960, 960), (18, 22), "natsuki_q", (0, 0), "natsuki/3.png")
image natsuki 5r = LiveComposite((960, 960), (18, 22), "natsuki_r", (0, 0), "natsuki/3.png")
image natsuki 5s = LiveComposite((960, 960), (18, 22), "natsuki_s", (0, 0), "natsuki/3.png")
image natsuki 5t = LiveComposite((960, 960), (18, 22), "natsuki_t", (0, 0), "natsuki/3.png")
image natsuki 5u = LiveComposite((960, 960), (18, 22), "natsuki_u", (0, 0), "natsuki/3.png")
image natsuki 5v = LiveComposite((960, 960), (18, 22), "natsuki_v", (0, 0), "natsuki/3.png")
image natsuki 5w = LiveComposite((960, 960), (18, 22), "natsuki_w", (0, 0), "natsuki/3.png")
image natsuki 5x = LiveComposite((960, 960), (18, 22), "natsuki_x", (0, 0), "natsuki/3.png")
image natsuki 5y = LiveComposite((960, 960), (18, 22), "natsuki_y", (0, 0), "natsuki/3.png")
image natsuki 5z = LiveComposite((960, 960), (18, 22), "natsuki_z", (0, 0), "natsuki/3.png")
image natsuki 52 = LiveComposite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki_4t")


image natsuki 1ba = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_a")
image natsuki 1bb = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_b")
image natsuki 1bc = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_c")
image natsuki 1bd = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_d")
image natsuki 1be = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_e")
image natsuki 1bf = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_f")
image natsuki 1bg = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_g")
image natsuki 1bh = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_h")
image natsuki 1bi = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_i")
image natsuki 1bj = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_j")
image natsuki 1bk = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_k")
image natsuki 1bl = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_l")
image natsuki 1bm = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_m")
image natsuki 1bn = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_n")
image natsuki 1bo = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_o")
image natsuki 1bp = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_p")
image natsuki 1bq = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_q")
image natsuki 1br = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_r")
image natsuki 1bs = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_s")
image natsuki 1bt = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_t")
image natsuki 1bu = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_u")
image natsuki 1bv = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_v")
image natsuki 1bw = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_w")
image natsuki 1bx = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_x")
image natsuki 1by = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_y")
image natsuki 1bz = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_z")

image natsuki 2ba = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_a")
image natsuki 2bb = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_b")
image natsuki 2bc = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_c")
image natsuki 2bd = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_d")
image natsuki 2be = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_e")
image natsuki 2bf = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_f")
image natsuki 2bg = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_g")
image natsuki 2bh = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_h")
image natsuki 2bi = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_i")
image natsuki 2bj = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_j")
image natsuki 2bk = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_k")
image natsuki 2bl = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_l")
image natsuki 2bm = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_m")
image natsuki 2bn = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_n")
image natsuki 2bo = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_o")
image natsuki 2bp = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_p")
image natsuki 2bq = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_q")
image natsuki 2br = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_r")
image natsuki 2bs = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_s")
image natsuki 2bt = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_t")
image natsuki 2bu = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_u")
image natsuki 2bv = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_v")
image natsuki 2bw = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_w")
image natsuki 2bx = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_x")
image natsuki 2by = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_y")
image natsuki 2bz = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_z")

image natsuki 3ba = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_a")
image natsuki 3bb = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_b")
image natsuki 3bc = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_c")
image natsuki 3bd = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_d")
image natsuki 3be = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_e")
image natsuki 3bf = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_f")
image natsuki 3bg = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_g")
image natsuki 3bh = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_h")
image natsuki 3bi = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_i")
image natsuki 3bj = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_j")
image natsuki 3bk = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_k")
image natsuki 3bl = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_l")
image natsuki 3bm = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_m")
image natsuki 3bn = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_n")
image natsuki 3bo = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_o")
image natsuki 3bp = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_p")
image natsuki 3bq = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_q")
image natsuki 3br = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_r")
image natsuki 3bs = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_s")
image natsuki 3bt = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_t")
image natsuki 3bu = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_u")
image natsuki 3bv = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_v")
image natsuki 3bw = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_w")
image natsuki 3bx = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_x")
image natsuki 3by = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_y")
image natsuki 3bz = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_z")

image natsuki 4ba = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_a")
image natsuki 4bb = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_b")
image natsuki 4bc = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_c")
image natsuki 4bd = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_d")
image natsuki 4be = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_e")
image natsuki 4bf = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_f")
image natsuki 4bg = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_g")
image natsuki 4bh = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_h")
image natsuki 4bi = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_i")
image natsuki 4bj = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_j")
image natsuki 4bk = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_k")
image natsuki 4bl = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_l")
image natsuki 4bm = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_m")
image natsuki 4bn = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_n")
image natsuki 4bo = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_o")
image natsuki 4bp = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_p")
image natsuki 4bq = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_q")
image natsuki 4br = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_r")
image natsuki 4bs = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_s")
image natsuki 4bt = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_t")
image natsuki 4bu = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_u")
image natsuki 4bv = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_v")
image natsuki 4bw = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_w")
image natsuki 4bx = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_x")
image natsuki 4by = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_y")
image natsuki 4bz = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_z")

image natsuki 12ba = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2bta")
image natsuki 12bb = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2btb")
image natsuki 12bc = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2btc")
image natsuki 12bd = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2btd")
image natsuki 12be = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2bte")
image natsuki 12bf = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2btf")
image natsuki 12bg = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2btg")
image natsuki 12bh = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2bth")
image natsuki 12bi = LiveComposite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki_2bti")

image natsuki 42ba = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2bta")
image natsuki 42bb = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2btb")
image natsuki 42bc = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2btc")
image natsuki 42bd = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2btd")
image natsuki 42be = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2bte")
image natsuki 42bf = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2btf")
image natsuki 42bg = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2btg")
image natsuki 42bh = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2bth")
image natsuki 42bi = LiveComposite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki_2bti")

image natsuki 5ba = LiveComposite((960, 960), (18, 22), "natsuki_a", (0, 0), "natsuki/3b.png")
image natsuki 5bb = LiveComposite((960, 960), (18, 22), "natsuki_b", (0, 0), "natsuki/3b.png")
image natsuki 5bc = LiveComposite((960, 960), (18, 22), "natsuki_c", (0, 0), "natsuki/3b.png")
image natsuki 5bd = LiveComposite((960, 960), (18, 22), "natsuki_d", (0, 0), "natsuki/3b.png")
image natsuki 5be = LiveComposite((960, 960), (18, 22), "natsuki_e", (0, 0), "natsuki/3b.png")
image natsuki 5bf = LiveComposite((960, 960), (18, 22), "natsuki_f", (0, 0), "natsuki/3b.png")
image natsuki 5bg = LiveComposite((960, 960), (18, 22), "natsuki_g", (0, 0), "natsuki/3b.png")
image natsuki 5bh = LiveComposite((960, 960), (18, 22), "natsuki_h", (0, 0), "natsuki/3b.png")
image natsuki 5bi = LiveComposite((960, 960), (18, 22), "natsuki_i", (0, 0), "natsuki/3b.png")
image natsuki 5bj = LiveComposite((960, 960), (18, 22), "natsuki_j", (0, 0), "natsuki/3b.png")
image natsuki 5bk = LiveComposite((960, 960), (18, 22), "natsuki_k", (0, 0), "natsuki/3b.png")
image natsuki 5bl = LiveComposite((960, 960), (18, 22), "natsuki_l", (0, 0), "natsuki/3b.png")
image natsuki 5bm = LiveComposite((960, 960), (18, 22), "natsuki_m", (0, 0), "natsuki/3b.png")
image natsuki 5bn = LiveComposite((960, 960), (18, 22), "natsuki_n", (0, 0), "natsuki/3b.png")
image natsuki 5bo = LiveComposite((960, 960), (18, 22), "natsuki_o", (0, 0), "natsuki/3b.png")
image natsuki 5bp = LiveComposite((960, 960), (18, 22), "natsuki_p", (0, 0), "natsuki/3b.png")
image natsuki 5bq = LiveComposite((960, 960), (18, 22), "natsuki_q", (0, 0), "natsuki/3b.png")
image natsuki 5br = LiveComposite((960, 960), (18, 22), "natsuki_r", (0, 0), "natsuki/3b.png")
image natsuki 5bs = LiveComposite((960, 960), (18, 22), "natsuki_s", (0, 0), "natsuki/3b.png")
image natsuki 5bt = LiveComposite((960, 960), (18, 22), "natsuki_t", (0, 0), "natsuki/3b.png")
image natsuki 5bu = LiveComposite((960, 960), (18, 22), "natsuki_u", (0, 0), "natsuki/3b.png")
image natsuki 5bv = LiveComposite((960, 960), (18, 22), "natsuki_v", (0, 0), "natsuki/3b.png")
image natsuki 5bw = LiveComposite((960, 960), (18, 22), "natsuki_w", (0, 0), "natsuki/3b.png")
image natsuki 5bx = LiveComposite((960, 960), (18, 22), "natsuki_x", (0, 0), "natsuki/3b.png")
image natsuki 5by = LiveComposite((960, 960), (18, 22), "natsuki_y", (0, 0), "natsuki/3b.png")
image natsuki 5bz = LiveComposite((960, 960), (18, 22), "natsuki_z", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_1t")
image natsuki 2 = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_1t")
image natsuki 3 = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_1t")
image natsuki 4 = LiveComposite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki_1t")
image natsuki 5 = LiveComposite((960, 960), (18, 22), "natsuki_1t", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = LiveComposite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki_scream")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
# Yuri's face expressions
image y_eye_0:
    "mod_assets/y_animation/y_eye_a.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_1:
    "mod_assets/y_animation/y_eye_e.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_2:
    "mod_assets/y_animation/y_eye_g.png"
    choice:
        3.0
    choice:
        2.5
    choice:
        1.0
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_3:
    "mod_assets/y_animation/y_eye_n.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_4:
    "mod_assets/y_animation/y_eye_o.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_5:
    "mod_assets/y_animation/y_eye_r.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_6:
    "mod_assets/y_animation/y_eye_u.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_k.png"
    0.1
    repeat
image y_eye_7:
    "mod_assets/y_animation/y_eye_a2.png"
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_2.png"
    0.1
    repeat
image y_eye_8:
    "mod_assets/y_animation/y_eye_b2.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/y_animation/y_eye_2.png"
    0.1
    repeat
image y_eye_9:
    "mod_assets/y_animation/y_eye_d2.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/y_animation/y_eye_2.png"
    0.1
    repeat
image y_mouth_0:
    "mod_assets/y_animation/y_mouth_b.png"
    0.15
    "mod_assets/y_animation/y_mouth_f.png"
    0.15
    repeat
image y_mouth_1 = "mod_assets/y_animation/y_mouth_a.png"
image y_mouth_2 = "mod_assets/y_animation/y_mouth_b.png"
image y_mouth_3:
    "mod_assets/y_animation/y_mouth_f.png"
    0.15
    "mod_assets/y_animation/y_mouth_e.png"
    0.15
    repeat
image y_mouth_4 = "mod_assets/y_animation/y_mouth_e.png"
image y_mouth_5 = "mod_assets/y_animation/y_mouth_f.png"
image y_mouth_6:
    "mod_assets/y_animation/y_mouth_n.png"
    0.15
    "mod_assets/y_animation/y_mouth_y2.png"
    0.15
    repeat
image y_mouth_7 = "mod_assets/y_animation/y_mouth_n.png"
image y_mouth_8 = "mod_assets/y_animation/y_mouth_y2.png"
image y_mouth_9:
    "mod_assets/y_animation/y_mouth_r.png"
    0.15
    "mod_assets/y_animation/y_mouth_f.png"
    0.15
    repeat
image y_mouth_10 = "mod_assets/y_animation/y_mouth_r.png"
image y_mouth_11:
    "mod_assets/y_animation/y_mouth_y1.png"
    0.15
    "mod_assets/y_animation/y_mouth_b.png"
    0.15
    repeat
image y_mouth_12 = "mod_assets/y_animation/y_mouth_y1.png"
image y_mouth_13:
    "mod_assets/y_animation/y_mouth_y3.png"
    0.15
    "mod_assets/y_animation/y_mouth_y7.png"
    0.15
    repeat
image y_mouth_14 = "mod_assets/y_animation/y_mouth_y3.png"
image y_mouth_15 = "mod_assets/y_animation/y_mouth_y7.png"
image y_mouth_16:
    "mod_assets/y_animation/y_mouth_a2.png"
    0.15
    "mod_assets/y_animation/y_mouth_d2'.png"
    0.15
    repeat
image y_mouth_17 = "mod_assets/y_animation/y_mouth_a2.png"
image y_mouth_18 = "mod_assets/y_animation/y_mouth_c2.png"
image y_mouth_19:
    "mod_assets/y_animation/y_mouth_d2.png"
    0.15
    "mod_assets/y_animation/y_mouth_a2.png"
    0.15
    repeat
image y_mouth_20 = "mod_assets/y_animation/y_mouth_d2.png"


# building Yuri's face animations
image yuri_a = LiveComposite((960,960),(0,1),"yuri/a.png", (0,1),"y_eye_0",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_a2 =LiveComposite((960,960),(0,1),"yuri/a2.png",(0,1),"y_eye_7",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_16","y_mouth_17"))
image yuri_b = LiveComposite((960,960),(0,1),"yuri/b.png", (0,1),"y_eye_0",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_2"))
image yuri_b2 =LiveComposite((960,960),(0,1),"yuri/b2.png",(0,1),"y_eye_8",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_16","y_mouth_17"))
image yuri_c = LiveComposite((960,960),(0,1),"yuri/c.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_c2 =LiveComposite((960,960),(0,1),"yuri/c2.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_16","y_mouth_18"))
image yuri_d = LiveComposite((960,960),(0,1),"yuri/d.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_2"))
image yuri_d2 =LiveComposite((960,960),(0,1),"yuri/d2.png",(0,1),"y_eye_9",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_19","y_mouth_20"))
image yuri_e = LiveComposite((960,960),(0,1),"yuri/e.png", (0,1),"y_eye_1",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_4"))
image yuri_e2 =LiveComposite((960,960),(0,1),"yuri/e2.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_16","y_mouth_17"))
image yuri_f = LiveComposite((960,960),(0,1),"yuri/f.png", (0,1),"y_eye_1",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_g = LiveComposite((960,960),(0,1),"yuri/g.png", (0,1),"y_eye_2",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_4"))
image yuri_h = LiveComposite((960,960),(0,1),"yuri/h.png", (0,1),"y_eye_2",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_i = LiveComposite((960,960),(0,1),"yuri/i.png", (0,1),"y_eye_2",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_j = LiveComposite((960,960),(0,1),"yuri/j.png", (0,1),"y_eye_2",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_2"))
image yuri_k = LiveComposite((960,960),(0,1),"yuri/k.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_l = LiveComposite((960,960),(0,1),"yuri/l.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_m = LiveComposite((960,960),(0,1),"yuri/m.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_n = LiveComposite((960,960),(0,1),"yuri/n.png", (0,1),"y_eye_3",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_6","y_mouth_7"))
image yuri_o = LiveComposite((960,960),(0,1),"yuri/o.png", (0,1),"y_eye_4",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_6","y_mouth_7"))
image yuri_p = LiveComposite((960,960),(0,1),"yuri/p.png", (0,1),"y_eye_3",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_6","y_mouth_8"))
image yuri_q = LiveComposite((960,960),(0,1),"yuri/q.png", (0,1),"y_eye_4",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_2"))
image yuri_r = LiveComposite((960,960),(0,1),"yuri/r.png", (0,1),"y_eye_5",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_9","y_mouth_10"))
image yuri_s = LiveComposite((960,960),(0,1),"yuri/s.png", (0,1),"y_eye_0",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_t = LiveComposite((960,960),(0,1),"yuri/t.png", (0,1),"y_eye_0",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_u = LiveComposite((960,960),(0,1),"yuri/u.png", (0,1),"y_eye_6",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_0","y_mouth_1"))
image yuri_v = LiveComposite((960,960),(0,1),"yuri/v.png", (0,1),"y_eye_6",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_w = LiveComposite((960,960),(0,1),"yuri/w.png", (0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_y1 =LiveComposite((960,960),(0,1),"yuri/y1.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_11","y_mouth_12"))
image yuri_y2 =LiveComposite((960,960),(0,1),"yuri/y2.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_6","y_mouth_8"))
image yuri_y3 =LiveComposite((960,960),(0,1),"yuri/y3.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_13","y_mouth_14"))
image yuri_y4 =LiveComposite((960,960),(0,1),"yuri/y4.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_10","y_mouth_5"))
image yuri_y5 =LiveComposite((960,960),(0,1),"yuri/y5.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_11","y_mouth_12"))
image yuri_y6 =LiveComposite((960,960),(0,1),"yuri/y6.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_3","y_mouth_5"))
image yuri_y7 =LiveComposite((960,960),(0,1),"yuri/y7.png",(0,1),WhileSpeaking("yuri" or "nat&yuri","y_mouth_13","y_mouth_15"))

image yuri 1 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_a")
image yuri 2 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_a")
image yuri 3 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_a")
image yuri 4 = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_a2")

image yuri 1a = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_a")
image yuri 1b = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_b")
image yuri 1c = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_c")
image yuri 1d = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_d")
image yuri 1e = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_e")
image yuri 1f = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_f")
image yuri 1g = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_g")
image yuri 1h = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_h")
image yuri 1i = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_i")
image yuri 1j = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_j")
image yuri 1k = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_k")
image yuri 1l = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_l")
image yuri 1m = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_m")
image yuri 1n = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_n")
image yuri 1o = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_o")
image yuri 1p = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_p")
image yuri 1q = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_q")
image yuri 1r = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_r")
image yuri 1s = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_s")
image yuri 1t = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_t")
image yuri 1u = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_u")
image yuri 1v = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_v")
image yuri 1w = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_w")

image yuri 1y1 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y1")
image yuri 1y2 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y2")
image yuri 1y3 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y3")
image yuri 1y4 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y4")
image yuri 1y5 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y5")
image yuri 1y6 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y6")
image yuri 1y7 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri_y7")

image yuri 2a = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_a")
image yuri 2b = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_b")
image yuri 2c = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_c")
image yuri 2d = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_d")
image yuri 2e = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_e")
image yuri 2f = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_f")
image yuri 2g = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_g")
image yuri 2h = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_h")
image yuri 2i = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_i")
image yuri 2j = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_j")
image yuri 2k = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_k")
image yuri 2l = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_l")
image yuri 2m = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_m")
image yuri 2n = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_n")
image yuri 2o = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_o")
image yuri 2p = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_p")
image yuri 2q = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_q")
image yuri 2r = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_r")
image yuri 2s = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_s")
image yuri 2t = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_t")
image yuri 2u = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_u")
image yuri 2v = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_v")
image yuri 2w = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_w")

image yuri 2y1 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y1")
image yuri 2y2 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y2")
image yuri 2y3 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y3")
image yuri 2y4 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y4")
image yuri 2y5 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y5")
image yuri 2y6 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y6")
image yuri 2y7 = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y7")

image yuri 3a = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_a")
image yuri 3b = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_b")
image yuri 3c = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_c")
image yuri 3d = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_d")
image yuri 3e = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_e")
image yuri 3f = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_f")
image yuri 3g = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_g")
image yuri 3h = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_h")
image yuri 3i = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_i")
image yuri 3j = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_j")
image yuri 3k = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_k")
image yuri 3l = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_l")
image yuri 3m = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_m")
image yuri 3n = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_n")
image yuri 3o = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_o")
image yuri 3p = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_p")
image yuri 3q = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_q")
image yuri 3r = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_r")
image yuri 3s = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_s")
image yuri 3t = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_t")
image yuri 3u = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_u")
image yuri 3v = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_v")
image yuri 3w = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_w")

image yuri 3y1 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y1")
image yuri 3y2 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y2")
image yuri 3y3 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y3")
image yuri 3y4 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y4")
image yuri 3y5 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y5")
image yuri 3y6 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y6")
image yuri 3y7 = LiveComposite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri_y7")

image yuri 4a = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_a2")
image yuri 4b = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_b2")
image yuri 4c = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_c2")
image yuri 4d = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_d2")
image yuri 4e = LiveComposite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri_e2")

image yuri 1ba = LiveComposite((960, 960), (0, 0), "yuri_a", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = LiveComposite((960, 960), (0, 0), "yuri_b", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = LiveComposite((960, 960), (0, 0), "yuri_c", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = LiveComposite((960, 960), (0, 0), "yuri_d", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = LiveComposite((960, 960), (0, 0), "yuri_e", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = LiveComposite((960, 960), (0, 0), "yuri_f", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = LiveComposite((960, 960), (0, 0), "yuri_g", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = LiveComposite((960, 960), (0, 0), "yuri_h", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = LiveComposite((960, 960), (0, 0), "yuri_i", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = LiveComposite((960, 960), (0, 0), "yuri_j", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = LiveComposite((960, 960), (0, 0), "yuri_k", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = LiveComposite((960, 960), (0, 0), "yuri_l", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = LiveComposite((960, 960), (0, 0), "yuri_m", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = LiveComposite((960, 960), (0, 0), "yuri_n", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = LiveComposite((960, 960), (0, 0), "yuri_o", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = LiveComposite((960, 960), (0, 0), "yuri_p", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = LiveComposite((960, 960), (0, 0), "yuri_q", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = LiveComposite((960, 960), (0, 0), "yuri_r", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = LiveComposite((960, 960), (0, 0), "yuri_s", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = LiveComposite((960, 960), (0, 0), "yuri_t", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = LiveComposite((960, 960), (0, 0), "yuri_u", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = LiveComposite((960, 960), (0, 0), "yuri_v", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = LiveComposite((960, 960), (0, 0), "yuri_w", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = LiveComposite((960, 960), (0, 0), "yuri_a", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = LiveComposite((960, 960), (0, 0), "yuri_b", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = LiveComposite((960, 960), (0, 0), "yuri_c", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = LiveComposite((960, 960), (0, 0), "yuri_d", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = LiveComposite((960, 960), (0, 0), "yuri_e", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = LiveComposite((960, 960), (0, 0), "yuri_f", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = LiveComposite((960, 960), (0, 0), "yuri_g", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = LiveComposite((960, 960), (0, 0), "yuri_h", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = LiveComposite((960, 960), (0, 0), "yuri_i", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = LiveComposite((960, 960), (0, 0), "yuri_j", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = LiveComposite((960, 960), (0, 0), "yuri_k", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = LiveComposite((960, 960), (0, 0), "yuri_l", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = LiveComposite((960, 960), (0, 0), "yuri_m", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = LiveComposite((960, 960), (0, 0), "yuri_n", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = LiveComposite((960, 960), (0, 0), "yuri_o", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = LiveComposite((960, 960), (0, 0), "yuri_p", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = LiveComposite((960, 960), (0, 0), "yuri_q", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = LiveComposite((960, 960), (0, 0), "yuri_r", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = LiveComposite((960, 960), (0, 0), "yuri_s", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = LiveComposite((960, 960), (0, 0), "yuri_t", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = LiveComposite((960, 960), (0, 0), "yuri_u", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = LiveComposite((960, 960), (0, 0), "yuri_v", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = LiveComposite((960, 960), (0, 0), "yuri_w", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = LiveComposite((960, 960), (0, 0), "yuri_a", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = LiveComposite((960, 960), (0, 0), "yuri_b", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = LiveComposite((960, 960), (0, 0), "yuri_c", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = LiveComposite((960, 960), (0, 0), "yuri_d", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = LiveComposite((960, 960), (0, 0), "yuri_e", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = LiveComposite((960, 960), (0, 0), "yuri_f", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = LiveComposite((960, 960), (0, 0), "yuri_g", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = LiveComposite((960, 960), (0, 0), "yuri_h", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = LiveComposite((960, 960), (0, 0), "yuri_i", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = LiveComposite((960, 960), (0, 0), "yuri_j", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = LiveComposite((960, 960), (0, 0), "yuri_k", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = LiveComposite((960, 960), (0, 0), "yuri_l", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = LiveComposite((960, 960), (0, 0), "yuri_m", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = LiveComposite((960, 960), (0, 0), "yuri_n", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = LiveComposite((960, 960), (0, 0), "yuri_o", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = LiveComposite((960, 960), (0, 0), "yuri_p", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = LiveComposite((960, 960), (0, 0), "yuri_q", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = LiveComposite((960, 960), (0, 0), "yuri_r", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = LiveComposite((960, 960), (0, 0), "yuri_s", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = LiveComposite((960, 960), (0, 0), "yuri_t", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = LiveComposite((960, 960), (0, 0), "yuri_u", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = LiveComposite((960, 960), (0, 0), "yuri_v", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = LiveComposite((960, 960), (0, 0), "yuri_w", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = LiveComposite((960, 960), (0, 0), "yuri_a2", (0, 0), "yuri/3b.png")
image yuri 4bb = LiveComposite((960, 960), (0, 0), "yuri_b2", (0, 0), "yuri/3b.png")
image yuri 4bc = LiveComposite((960, 960), (0, 0), "yuri_c2", (0, 0), "yuri/3b.png")
image yuri 4bd = LiveComposite((960, 960), (0, 0), "yuri_d2", (0, 0), "yuri/3b.png")
image yuri 4be = LiveComposite((960, 960), (0, 0), "yuri_e2", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika
# Monika's face expressions
image m_eye_0:
    "mod_assets/m_animation/m_eye_a.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "mod_assets/m_animation/m_eye_j.png"
    0.1
    repeat
image m_eye_1:
    "mod_assets/m_animation/m_eye_a.png"
    choice:
        4.0
    choice:
        2.0
    choice:
        1.0
    "mod_assets/m_animation/m_eye_q'.png"
    0.1
    repeat
image m_eye_2:
    "mod_assets/m_animation/m_eye_m.png"
    choice:
        5.5
    choice:
        2.5
    choice:
        1.5
    "mod_assets/m_animation/m_eye_q'.png"
    0.1
    repeat
image m_eye_3:
    "mod_assets/m_animation/m_eye_3a.png"
    choice:
        4.5
    choice:
        3.0
    choice:
        1.5
    "mod_assets/m_animation/m_eye_3.png"
    0.1
    repeat

image m_mouth_0:
    "mod_assets/m_animation/m_mouth_b.png"
    0.15
    "mod_assets/m_animation/m_mouth_a.png"
    0.15
    repeat
image m_mouth_1:
    "mod_assets/m_animation/m_mouth_d.png"
    0.15
    "mod_assets/m_animation/m_mouth_d'.png"
    0.15
    repeat

image m_mouth_2 = "mod_assets/m_animation/m_mouth_a.png"
image m_mouth_3 = "mod_assets/m_animation/m_mouth_c.png"

image m_mouth_4:
    "mod_assets/m_animation/m_mouth_3d.png"
    0.15
    "mod_assets/m_animation/m_mouth_3a.png"
    0.15
    repeat
image m_mouth_5:
    "mod_assets/m_animation/m_mouth_3c.png"
    0.15
    "mod_assets/m_animation/m_mouth_3b.png"
    0.15
    repeat
image m_mouth_6 = "mod_assets/m_animation/m_mouth_3a.png"
image m_mouth_7 = "mod_assets/m_animation/m_mouth_3b.png"
image m_mouth_8 = "mod_assets/m_animation/m_mouth_b.png"
image m_mouth_9 = "mod_assets/m_animation/m_mouth_d.png"



# building Monika's face animations
image monika_a =LiveComposite((960,960),(0,1),"monika/a.png",(0,1),"m_eye_0",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_2"))
image monika_b =LiveComposite((960,960),(0,1),"monika/b.png",(0,1),"m_eye_0",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_8"))
image monika_c =LiveComposite((960,960),(0,1),"monika/c.png",(0,1),"m_eye_0",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_3"))
image monika_d =LiveComposite((960,960),(0,1),"monika/d.png",(0,1),"m_eye_0",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_9"))
image monika_e =LiveComposite((960,960),(0,1),"monika/e.png",(0,1),"m_eye_1",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_2"))
image monika_f =LiveComposite((960,960),(0,1),"monika/f.png",(0,1),"m_eye_1",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_3"))
image monika_g =LiveComposite((960,960),(0,1),"monika/g.png",(0,1),"m_eye_1",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_9"))
image monika_h =LiveComposite((960,960),(0,1),"monika/h.png",(0,1),"m_eye_1",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_3"))
image monika_i =LiveComposite((960,960),(0,1),"monika/i.png",(0,1),"m_eye_1",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_9"))
image monika_j =LiveComposite((960,960),(0,1),"monika/j.png",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_2"))
image monika_k =LiveComposite((960,960),(0,1),"monika/k.png",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_8"))
image monika_l =LiveComposite((960,960),(0,1),"monika/l.png",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_8"))
image monika_m =LiveComposite((960,960),(0,1),"monika/m.png",(0,1),"m_eye_2",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_2"))
image monika_n =LiveComposite((960,960),(0,1),"monika/n.png",(0,1),"m_eye_2",(0,1),WhileSpeaking("monika","m_mouth_0","m_mouth_8"))
image monika_o =LiveComposite((960,960),(0,1),"monika/o.png",(0,1),"m_eye_2",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_3"))
image monika_p =LiveComposite((960,960),(0,1),"monika/p.png",(0,1),"m_eye_2",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_9"))
image monika_q =LiveComposite((960,960),(0,1),"monika/q.png",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_3"))
image monika_r =LiveComposite((960,960),(0,1),"monika/r.png",(0,1),WhileSpeaking("monika","m_mouth_1","m_mouth_9"))

image monika 1 = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_a")
image monika 2 = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_a")
image monika 3 = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_a")
image monika 4 = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_a")
image monika 5 = LiveComposite((960, 960), (0, 0), "monika/3a.png", (0, 0), "m_eye_3", (0 ,0), WhileSpeaking("monika","m_mouth_4","m_mouth_6"))

image monika 1a = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_a")
image monika 1b = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_b")
image monika 1c = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_c")
image monika 1d = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_d")
image monika 1e = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_e")
image monika 1f = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_f")
image monika 1g = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_g")
image monika 1h = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_h")
image monika 1i = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_i")
image monika 1j = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_j")
image monika 1k = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_k")
image monika 1l = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_l")
image monika 1m = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_m")
image monika 1n = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_n")
image monika 1o = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_o")
image monika 1p = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_p")
image monika 1q = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_q")
image monika 1r = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika_r")

image monika 2a = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_a")
image monika 2b = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_b")
image monika 2c = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_c")
image monika 2d = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_d")
image monika 2e = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_e")
image monika 2f = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_f")
image monika 2g = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_g")
image monika 2h = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_h")
image monika 2i = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_i")
image monika 2j = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_j")
image monika 2k = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_k")
image monika 2l = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_l")
image monika 2m = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_m")
image monika 2n = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_n")
image monika 2o = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_o")
image monika 2p = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_p")
image monika 2q = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_q")
image monika 2r = LiveComposite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika_r")

image monika 3a = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_a")
image monika 3b = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_b")
image monika 3c = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_c")
image monika 3d = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_d")
image monika 3e = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_e")
image monika 3f = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_f")
image monika 3g = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_g")
image monika 3h = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_h")
image monika 3i = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_i")
image monika 3j = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_j")
image monika 3k = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_k")
image monika 3l = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_l")
image monika 3m = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_m")
image monika 3n = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_n")
image monika 3o = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_o")
image monika 3p = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_p")
image monika 3q = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_q")
image monika 3r = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika_r")

image monika 4a = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_a")
image monika 4b = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_b")
image monika 4c = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_c")
image monika 4d = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_d")
image monika 4e = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_e")
image monika 4f = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_f")
image monika 4g = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_g")
image monika 4h = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_h")
image monika 4i = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_i")
image monika 4j = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_j")
image monika 4k = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_k")
image monika 4l = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_l")
image monika 4m = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_m")
image monika 4n = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_n")
image monika 4o = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_o")
image monika 4p = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_p")
image monika 4q = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_q")
image monika 4r = LiveComposite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika_r")

image monika 5a = LiveComposite((960, 960), (0, 0), "monika/3a.png", (0, 0), "m_eye_3", (0, 0), WhileSpeaking("monika","m_mouth_4","m_mouth_6"))
image monika 5b = LiveComposite((960, 960), (0, 0), "monika/3b.png", (0, 0), "m_eye_3", (0, 0), WhileSpeaking("monika","m_mouth_5","m_mouth_7"))

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

## If a dialogue matches one of the following, stop mouth animation.
define not_lip_sync = ['...', '...?', '「……」', '「……？」', '......', '「………」', '「…………」']

# This is set to the name of the character that is speaking, or
# None if no character is currently speaking.
# It's not a constant, but it's defined as "define"
# because we don't want to include it in the save data.
define speaking = None

# Holds the currently displayed dialogue.
# It's not a constant, but it's defined as "define"
# because we don't want to include it in the save data.
define current_dialogue = None

# Mouth-flapping algorithm
init python:
    # Re-set the callback to the ADVCharacter replaced by the translation.
    def set_character_callback():
        s.display_args["callback"] = speaker("sayori")
        m.display_args["callback"] = speaker("monika")
        n.display_args["callback"] = speaker("natsuki")
        y.display_args["callback"] = speaker("yuri")
        ny.display_args["callback"] = speaker("nat&yuri")
    config.change_language_callbacks.append(set_character_callback)

    # This returns speaking if the character is speaking,
    # and done if the character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # Get the current conversation and save it global
    def get_current_dialogue(what):
        global current_dialogue
        current_dialogue = what
        return what
    config.say_menu_text_filter = get_current_dialogue

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show" and not current_dialogue in not_lip_sync:
            speaking = name
        elif event == "slow_done" or event == "end":
            speaking = None
    speaker = renpy.curry(speaker_callback)
