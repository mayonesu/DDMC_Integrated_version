label specialend:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ persistent.autoload = "specialend"
    $ persistent.normal_end = -1
    $ quick_menu_limit = True
    $ style.say_dialogue = style.normal
    $ renpy.save_persistent()
    scene black
    stop music
    pause 3.0
    scene bg bedroom
    show image "#000000b0"
    with dissolve_scene_full
    "……"
    "……あれ？"
    "ここは俺の部屋だな……"
    "ということは今のは夢だったのか……？"
    "……目の前に誰かいる。"
    scene bg bedroom
    with open_eyes
    show sayori 4j zorder 1 at t11
    play music t2
    voice "voice/sayori/sayori_happy_01.ogg"
    s "「もう！いつまで寝てるの！！」"
    mc "「さ、サヨリ！？」"
    voice "voice/sayori/sayori_happy_02.ogg"
    s "「早く起きないと遅刻しちゃうよ！！」"
    show sayori 4i
    mc "「お、おう……」"
    "時計を見ると7時50分になっていた。"
    "なんでかわからないが、謎の安心感がある。"
    "これは現実なのか……？"
    "俺は急いで支度を済ませた。"
    scene bg house
    with wipeleft_scene
    show monika 5a zorder 1 at t11
    voice "voice/monika/monika_happy_01.ogg"
    m "「[player]君！おはよう！」"
    mc "「おう、おはよう……」"
    show monika 5a at t22
    show yuri 1b zorder 1 at t21
    voice "voice/yuri/yuri_happy_01.ogg"
    y "「[player]さん、おはようございます」"
    show monika 5a at t33
    show yuri 1a at t32
    show natsuki 4e zorder 1 at t31
    voice "voice/natsuki/natsuki_happy_01.ogg"
    n "「もう！遅いじゃない！」"
    show natsuki 4g
    mc "「ご、ごめん……」"
    show monika 5a at t44
    show yuri 1a at t43
    show natsuki 4g at t42
    show sayori 1r zorder 1 at t41
    voice "voice/sayori/sayori_happy_03.ogg"
    s "「おまたせ！」"
    show sayori 1q
    voice "voice/monika/monika_happy_02.ogg"
    m 2k "「よし！これでみんな揃ったね！」"
    mc "「なんでみんないるんだ……？」"
    voice "voice/monika/monika_happy_03.ogg"
    m "「せっかくの文化祭なんだからみんなで一緒に行こうってサヨリが言ったじゃない」"
    mc "「そ、そうだったか……」"
    voice "voice/sayori/sayori_happy_04.ogg"
    s 1r "「たまにはこういうのもありだよね！」"
    show sayori 1q
    voice "voice/yuri/yuri_happy_02.ogg"
    y 3d "「私はすごくいいことだと思います」"
    show yuri 3c
    voice "voice/natsuki/natsuki_happy_02.ogg"
    n 5w "「ま、まああたしは別に一緒じゃなくてもよかったんだけどね！」"
    voice "voice/yuri/yuri_happy_03.ogg"
    y 3d "「ナツキちゃんとても楽しみにしてるって言ってたじゃないですか」"
    show yuri 3c
    voice "voice/natsuki/natsuki_happy_03.ogg"
    n 1v "「ちょっと！！それ言わないでって言ったでしょ！！」"
    voice "voice/monika/monika_happy_04.ogg"
    m 1k "「アハハ！確かにそうだったわね！」"
    voice "voice/monika/monika_happy_05.ogg"
    m 3g "「あ、そろそろ行かないと遅刻するわよ」"
    show monika 1e
    voice "voice/sayori/sayori_happy_05.ogg"
    s 4m "「あっ！ほんとだ！！急がなきゃ！！」"
    show sayori 4m zorder 1 at lfhide
    hide sayori
    voice "voice/natsuki/natsuki_happy_04.ogg"
    n 4w "「ちょっと！待ちなさいよ！！」"
    show natsuki 4w zorder 1 at lfhide
    hide natsuki
    voice "voice/yuri/yuri_happy_04.ogg"
    y 2w "「もう、サヨリちゃんったら……」"
    show yuri 2w zorder 1 at thide
    hide yuri
    show monika 4b at t11
    voice "voice/monika/monika_happy_06.ogg"
    m 4b "「さあ、行きましょ[player]君」"
    voice "voice/monika/monika_happy_07.ogg"
    m "「もしかしたらこういうのを望んでいたのかな？」"
    show monika 4a
    mc "「ど、どういうことだ……？」"
    voice "voice/monika/monika_happy_08.ogg"
    m 4b "「さて、どうなんだろうね」"
    voice "voice/monika/monika_happy_09.ogg"
    m "「早く来ないと遅刻するよ！」"
    show monika 4b zorder 1 at thide
    hide monika
    "どういうことだ……？"
    "ま、まさか……。"
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
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
            "画面の前にいる[currentuser]が俺を導いてくれたのか？"
        else:
            "画面の前にいるもう一人の[player]が俺を導いてくれたのか？"
    else:
        "画面の前にいるもう一人の[player]が俺を導いてくれたのか？"
    "お前がみんなを助けたのか……？"
    "もしそうだとしたら……。"
    pause 2.0
    "救ってくれてありがとう。"
    "お前が導いてくれたこのルートを俺が維持してみせる。"
    "だからお前はこの世界を見守っていてくれないか？"
    "それだけでいい。"
    "他は何も望まない。"
    "ただ俺は……。"
    pause 2.0
    "みんなが幸せでいるのを見ていたいからだ。"
    window hide(None)
    pause 2.0
    if not persistent.achievement[14]:
        $ renpy.notify(achievement_notify + achievement_name_15)
        $ persistent.achievement[14] = True
        play sound "tl/None/sfx/achievement.ogg"
    jump credits
    return