init -1 python:
    def chapter_all_seen():
        for i in range(0,16):
            persistent.chapter_seen[i] = True
        
    def chapter_all_not_seen():
        for i in range(0,16):
            persistent.chapter_seen[i] = False

define config.console = True