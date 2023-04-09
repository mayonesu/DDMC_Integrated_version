init python:
    def recreate_character(name):
        try:
            renpy.file("../characters/" + name + ".chr")
            delete_character(name)
            open(config.basedir + "/characters/" + name + ".chr", "wb").write(renpy.file(name + ".chr").read())
        except: pass

init 1 python:
    if renpy.loadable("name"):
        import codecs
        playername = codecs.open(config.gamedir + "/name", "r", "utf-8").read()
        persistent.playername = playername
        player = persistent.player

translate None python:
    recreate_character('sayori')
    recreate_character('monika')
    recreate_character('natsuki')
    recreate_character('yuri')
    player = persistent.playername
    persistent.change_name = ""

