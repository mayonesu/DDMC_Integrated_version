translate None image:
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

    # defining blinking
    image Act3_eye:
        "mod_assets/m_animation/Act3_eye_1.png"
        choice:
            8.0
        choice:
            5.5
        choice:
            2.5
        "mod_assets/m_animation/Act3_eye_0.png"
        0.1
        repeat

    # defining mouth-flapping
    image Act3_mouth_0:
        "mod_assets/m_animation/Act3_mouth0_1.png"
        0.12
        "mod_assets/m_animation/Act3_mouth0_2.png"
        0.1
        "mod_assets/m_animation/Act3_mouth0_0.png"
        0.12
        "mod_assets/m_animation/Act3_mouth0_2.png"
        0.1
        repeat

    image Act3_mouth_1:
        "mod_assets/m_animation/Act3_mouth1_1.png"
        0.12
        "mod_assets/m_animation/Act3_mouth1_2.png"
        0.1
        "mod_assets/m_animation/Act3_mouth1_0.png"
        0.12
        "mod_assets/m_animation/Act3_mouth1_2.png"
        0.1
        repeat

    # setting face animations to Just Monika CG
    image monika_bg = LiveComposite((1280,720),(0,0),"images/cg/monika/monika_bg.png",(0,0),"Act3_eye",(0,0),WhileSpeaking("monika","Act3_mouth_0","mod_assets/m_animation/Act3_mouth0_0.png"))
    image monika_bg_highlight:
        LiveComposite((1280,720),(0,0),"images/cg/monika/monika_bg_highlight.png",(0,0),"Act3_eye",(0,0),WhileSpeaking("monika","Act3_mouth_0","mod_assets/m_animation/Act3_mouth0_0.png"))
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

translate None strings:
    old "{#ch7_main_53a54a5b}"
    new "Uh,can you hear me?"

    old "{#ch7_main_505126da}"
    new "...Is it working?"

    old "{#ch7_main_3f0344b2}"
    new "Yay, there you are!"

    old "{#ch7_main_a0b81240}"
    new "Hi again,[player]."

    old "{#ch7_main_b7419acb}"
    new "Um...welcome to the Literature Club!"

    old "{#ch7_main_f31c2d15}"
    new "Of course,we already know each other,because we were in the same class last year,and...um..."

    old "{#ch7_main_a7c3c599}"
    new "Ahaha..."

    old "{#ch7_main_e612037c}"
    new "..."

    old "{#ch7_main_d1ecd4f2}"
    new "Again. Welcome to the Literature Club."

    old "{#ch7_main_69d7b4c7}"
    new "Where...what...is here?"

    old "{#ch7_main_90a881ca}"
    new "As I once thought,am I still dreaming?"

    old "{#ch7_main_7ba4fe34}"
    new "I am now too tired to think about it."

    old "{#ch7_main_097b8e39}"
    new "Hmm... you think you are in your dream,right?"

    old "{#ch7_main_14fd324b}"
    new "Or this is the reality...which do you think is correct?"

    old "{#ch7_main_8760dde0}"
    new "Enough is Enough."

    old "{#ch7_main_d46a1acb}"
    new "I don't understand what she says."

    old "{#ch7_main_440abc10}"
    new "I glare at her."

    old "{#ch7_main_51ea30e0}"
    new "I don't care which I'm in a dream or not anymore."

    old "{#ch7_main_93a20d7a}"
    new "This is my reality as long as I'm trapped in this nightmare."

    old "{#ch7_main_4ce87eac}"
    new "I will put an end to this mess."

    old "{#ch7_main_fd527593}"
    new "Ooh [player]... you scare me."

    old "{#ch7_main_886873ea}"
    new "I had a linkling as to it."

    old "{#ch7_main_64850d50}"
    new "That she knew something."

    old "{#ch7_main_324ca856}"
    new "When She said she knew the exchange among Sayori and me,"

    old "{#ch7_main_bb2d1aec}"
    new "I felt a chill down my spine. That was the answer."

    old "{#ch7_main_0cae724e}"
    new "She said she knew a lot more than I thought."

    old "{#ch7_main_4f89ba43}"
    new "That means,she already knew that Sayori had gone away."

    old "{#ch7_main_8a31a1da}"
    new "Even though she knew it...she let me go..."

    old "{#ch7_main_04709ff7}"
    new "When I was back,she smiled sadly."

    old "{#ch7_main_8eb76cdf}"
    new "I was back...because of...my temporary...amnesia..."

    old "{#ch7_main_a20cefa7}"
    new "..."

    old "{#ch7_main_a0bb9f4e}"
    new "Anyway,I was back. It made her disappointed."

    old "{#ch7_main_642b4918}"
    new "Why? Was she disappointed with my serenity?"

    old "{#ch7_main_938deb84}"
    new "Serenity...no. Now I rememver everything. Every moment I think of Sayori..."

    old "{#ch7_main_2128a17f}"
    new "It drives me really crazy."

    old "{#ch7_main_3cad5e25}"
    new "You won,Monika. I am crazy as you intended."

    old "{#ch7_main_24e380ca}"
    new "I hold the fist with anger and sadness."

    old "{#ch7_main_bb939862}"
    new "Nevertheless,I control not to lost myself,and begin to talk quietly."

    old "{#ch7_main_f8d01863}"
    new "Tell me Monika,you knew that Sayori was dead at that time,didn't you?"

    old "{#ch7_main_e612037c_1}"
    new "..."

    old "{#ch7_main_5cbc56fb}"
    new "Don't tell me a lie. I just want to know everything."

    old "{#ch7_main_71ddf57a}"
    new "I knew...maybe. Yes,at least I knew it might be going to."

    old "{#ch7_1_main_aebe527b}"
    new "The anger in me disappeared befor I knew it."

    old "{#ch7_1_main_ac96fc37}"
    new "Well,it doesn't completely but,"

    old "{#ch7_1_main_03d6c223}"
    new "More than that,I want to know the truth."

    old "{#ch7_1_main_7de7a1e7}"
    new "She said she knew it."

    old "{#ch7_1_main_79025ce5}"
    new "That Sayori was dead. Why did she know it?"

    old "{#ch7_1_main_52096b87}"
    new "The answer is simple. She killed Sayori."

    old "{#ch7_1_main_dc0fe61b}"
    new "Monika killed Sayori."

    old "{#ch7_1_main_a20cefa7}"
    new "..."

    old "{#ch7_1_main_543ce512}"
    new "No doubt Sayori commited suicide. At least it seemed so."

    old "{#ch7_1_main_bde999e0}"
    new "Her rainclouds did't go away,either."

    old "{#ch7_1_main_56584a6f}"
    new "Still,I don't believe she committed it."

    old "{#ch7_1_main_0ff962ee}"
    new "I believe she was forced to."

    old "{#ch7_1_main_fdc608f4}"
    new "By Monika."

    old "{#ch7_1_main_a20cefa7_1}"
    new "..."

    old "{#ch7_1_main_610c7865}"
    new "Monika,I don't understand."

    old "{#ch7_1_main_60c64baa}"
    new "I say quietly."

    old "{#ch7_1_main_9d6b46bf}"
    new "Why you did......that thing."

    old "{#ch7_1_main_51c3547e}"
    new "That thing? I didn't do anything."

    old "{#ch7_1_main_6c276aa4}"
    new "She says,smiling."

    old "{#ch7_1_main_60f8a34e}"
    new "Yeah,you didn't."

    old "{#ch7_1_main_449f1550}"
    new "You didn't get your hands dirty."

    old "{#ch7_1_main_4ad68193}"
    new "You just implanted something dirty into Sayori."

    old "{#ch7_1_main_f7121171}"
    new "With smiling,as same as now."

    old "{#ch7_1_main_c0508ea8}"
    new "Thinking back of it,YOU left Yuri and me alone in the classroom."

    old "{#ch7_1_main_e612037c}"
    new "..."

    old "{#ch7_1_main_aa13a5b5}"
    new "She lost her mind suddenly,because someone inplanted something into her."

    old "{#ch7_1_main_34982121}"
    new "Someone who knows Yuri carries a knife with her and she might use it."

    old "{#ch7_1_main_825b986f}"
    new "I stop talking and watch her."

    old "{#ch7_1_main_6fdc6a0b}"
    new "She's smirking as always."

    old "{#ch7_1_main_6659ebb5}"
    new "YOU GODDAMN BASTARD !"

    old "{#ch7_1_main_879418d3}"
    new "Natsuki...yes,she..."

    old "{#ch7_1_main_145b0109}"
    new "She was back alone,though she went out with YOU."

    old "{#ch7_1_main_83e83a0d}"
    new "Because you,you planned it."

    old "{#ch7_1_main_822a7416}"
    new "She said something random,it was also because of your..."

    old "{#ch7_1_main_96d62b71}"
    new "I talk on and on,fast and furious."

    old "{#ch7_1_main_ce0a8d82}"
    new "But Monika doesn't turn her face pale or anything."

    old "{#ch7_1_main_25e0b8e7}"
    new "My anger rises up again."

    old "{#ch7_1_main_21c833c0}"
    new "Monika,you..."

    old "{#ch7_1_main_592c300e}"
    new "You've done it all? You've..."

    old "{#ch7_1_main_c1b6d07a}"
    new "Killed them all !?"

    old "{#ch7_1_main_e7d73ec9}"
    new "I scream. I can't stand it anymore."

    old "{#ch7_1_main_e612037c_1}"
    new "..."

    old "{#ch7_1_main_d1e7779a}"
    new "Say,say something to me! You..."
    old "だってこれは、"
    new "Because this is..."