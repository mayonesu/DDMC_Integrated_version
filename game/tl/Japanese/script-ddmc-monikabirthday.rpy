image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

label monika_birthday:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    scene black
    stop music fadeout 1.0
    with dissolve_scene_full
    pause 2.0
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    window show(None)
    $ style.say_dialogue = style.normal
    m "「やっほー、[player]君！」"
    m "「今日は何の日かわかる？」"
    mc "「今日はDDLCがリリース2周年か」"
    m "「それもそうだけど、他にもあるでしょ？」"
    mc "「あぁ、モニカの誕生日でもあるのか」"
    m "「ご名答！」"
    m "「って、本当に覚えてたの？」"
    m "「まさか、今知ったってことないよね？」"
    mc "「そ、そりゃ前から知ってたよ…」"
    m "「それならよかった！」"
    "今日調べて知っただなんて言えない…"
    mc "「というか、なんでここに来てるんだ？」"
    m "「[player]君がちゃんと私の誕生日覚えてるかどうか試したかっただけよ」"
    mc "「まさか、たったそれだけで…」"
    window hide(None)
    play sound "sfx/Cell_Phone-Notification01-3.ogg"
    pause 2.0
    mc "「ん？サヨリからメールが…」"
    m "「あら、どんな内容かしら？」"
    mc "「『[player]！今どこにいる？モニカちゃんもいるなら今すぐ部室に来て！！』だってさ」"
    m "「何かあったのかしら…」"
    m "「今すぐ部室に行かなきゃ！」"
    mc "「そ、そうだな…」"
    stop music fadeout 1.0
    scene black
    with dissolve_scene_full
    "そうして俺たちは部室に向かった"
    "まあこうなるのは最初からわかっていた"
    "なぜなら…"
    window hide(None)
    scene bg club_day
    with dissolve_scene_half
    show sayori 1r at t31
    show yuri 1d at t32
    show natsuki 4z at t33
    play music t2
    s "「モニカちゃん！お誕生日おめでとう！！」"
    show monika 1g at t41
    show sayori at t42
    show yuri at t43
    show natsuki at t44
    m "「ど、どういうことなの…？」"
    mc "「今日はモニカの誕生日だからみんなでお祝いしたいって思って」"
    y 1b "「みんなでどういうサプライズにするか考えたんです」"
    show yuri 1a
    n 4d "「たまにはこういうのもありでしょ？」"
    show natsuki 4a
    s 4s "「一度こういうのやってみたかったから、成功してよかった！」"
    show sayori 4q
    m 1k "「みんな…ありがとう…！」"
    m 1i "「そういえば、[player]君は知っていたのかしら？」"
    mc "「うん、まあ…」"
    s 4s "「[player]も手伝ってもらったよ！」"
    show sayori 4q
    m  1l "「なるほど、そういうことね」"
    n  4z "「まぁ、ちょっと不器用なところはあったけどね」"
    mc "「お、おい…やめろって…」"
    mc "「むしろ、ユリのおかげでなんとかなったからな」"
    y 4d "「わ、私は…その…」"
    y "「[player]さんが困ってたのでどうしても手伝いたくなって…」"
    mc "「ありがとう、ユリ」"
    y 4c "「///」"
    m 1k "「みんながこうやって用意してくれただけでも嬉しいわ！」"
    m "「こうしてもあれだから、早速始めましょう！」"
    show yuri 1c
    show natsuki 4z
    s 4s "「そうだね！」"
    "こうしてモニカの誕生日パーティーが始まった"
    window hide(None)
    scene black
    stop music fadeout 1.0
    with dissolve_scene_full
    "そういえばそっちはどうなんだ？"
    "たぶんDDLCリリース2周年でもあるけど、"
    "君はどんなお祝いをするんだい？"
    window hide(None)
    call endgame
    return

translate Japanese strings:
    old "{#monika_birthday_f5c7a68f}"
    new "「やっほー、[player]君！」"

    old "{#monika_birthday_e9642e06}"
    new "「今日は何の日かわかる？」"

    old "{#monika_birthday_d49c6667}"
    new "「今日はDDLCがリリース2周年か」"

    old "{#monika_birthday_e49aca1a}"
    new "「それもそうだけど、他にもあるでしょ？」"

    old "{#monika_birthday_4065ade9}"
    new "「あぁ、モニカの誕生日でもあるのか」"

    old "{#monika_birthday_efd3c2ba}"
    new "「ご名答！」"

    old "{#monika_birthday_3955f312}"
    new "「って、本当に覚えてたの？」"

    old "{#monika_birthday_ca7ea58c}"
    new "「まさか、今知ったってことないよね？」"

    old "{#monika_birthday_ad033d9f}"
    new "「そ、そりゃ前から知ってたよ…」"

    old "{#monika_birthday_278ab192}"
    new "「それならよかった！」"

    old "{#monika_birthday_23558cf4}"
    new "今日調べて知っただなんて言えない…"

    old "{#monika_birthday_1dae21f6}"
    new "「というか、なんでここに来てるんだ？」"

    old "{#monika_birthday_c89e0106}"
    new "「[player]君がちゃんと私の誕生日覚えてるかどうか試したかっただけよ」"

    old "{#monika_birthday_c6a16f36}"
    new "「まさか、たったそれだけで…」"

    old "{#monika_birthday_4998ea21}"
    new "「ん？サヨリからメールが…」"

    old "{#monika_birthday_0231bb3c}"
    new "「あら、どんな内容かしら？」"

    old "{#monika_birthday_f8ea07c5}"
    new "「『[player]！今どこにいる？モニカちゃんもいるなら今すぐ部室に来て！！』だってさ」"

    old "{#monika_birthday_44b03828}"
    new "「何かあったのかしら…」"

    old "{#monika_birthday_251f3404}"
    new "「今すぐ部室に行かなきゃ！」"

    old "{#monika_birthday_a4a8a2ed}"
    new "「そ、そうだな…」"

    old "{#monika_birthday_649c4418}"
    new "そうして俺たちは部室に向かった"

    old "{#monika_birthday_ff16b47f}"
    new "まあこうなるのは最初からわかっていた"

    old "{#monika_birthday_e608381d}"
    new "なぜなら…"

    old "{#monika_birthday_305e8c28}"
    new "「モニカちゃん！お誕生日おめでとう！！」"

    old "{#monika_birthday_34e36471}"
    new "「ど、どういうことなの…？」"

    old "{#monika_birthday_5c84039e}"
    new "「今日はモニカの誕生日だからみんなでお祝いしたいって思って」"

    old "{#monika_birthday_6725bb76}"
    new "「みんなでどういうサプライズにするか考えたんです」"

    old "{#monika_birthday_5d544220}"
    new "「たまにはこういうのもありでしょ？」"

    old "{#monika_birthday_54f9f0fb}"
    new "「一度こういうのやってみたかったから、成功してよかった！」"

    old "{#monika_birthday_20c7529a}"
    new "「みんな…ありがとう…！」"

    old "{#monika_birthday_98604fe4}"
    new "「そういえば、[player]君は知っていたのかしら？」"

    old "{#monika_birthday_864789d6}"
    new "「うん、まあ…」"

    old "{#monika_birthday_a07373d7}"
    new "「[player]も手伝ってもらったよ！」"

    old "{#monika_birthday_f41f1652}"
    new "「なるほど、そういうことね」"

    old "{#monika_birthday_b63fc140}"
    new "「まぁ、ちょっと不器用なところはあったけどね」"

    old "{#monika_birthday_33017009}"
    new "「お、おい…やめろって…」"

    old "{#monika_birthday_e1497c74}"
    new "「むしろ、ユリのおかげでなんとかなったからな」"

    old "{#monika_birthday_28ae3895}"
    new "「わ、私は…その…」"

    old "{#monika_birthday_993e62a9}"
    new "「[player]さんが困ってたのでどうしても手伝いたくなって…」"

    old "{#monika_birthday_abafe1d5}"
    new "「ありがとう、ユリ」"

    old "{#monika_birthday_27161ffc}"
    new "「///」"

    old "{#monika_birthday_2b2f30c7}"
    new "「みんながこうやって用意してくれただけでも嬉しいわ！」"

    old "{#monika_birthday_148324d7}"
    new "「こうしてもあれだから、早速始めましょう！」"

    old "{#monika_birthday_4aafc95e}"
    new "「そうだね！」"

    old "{#monika_birthday_49fb685f}"
    new "こうしてモニカの誕生日パーティーが始まった"

    old "{#monika_birthday_74ce6aae}"
    new "そういえばそっちはどうなんだ？"

    old "{#monika_birthday_919253e2}"
    new "たぶんDDLCリリース2周年でもあるけど、"

    old "{#monika_birthday_21be6ee2}"
    new "君はどんなお祝いをするんだい？"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
