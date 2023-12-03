translate Japanese python:
    style.ruby_text.size = 12 #文字を小さくする
    style.ruby_text.yoffset = -26 #20ピクセル上にずらして表示

translate Japanese style yuri_text:
    font "gui/font/851tegaki_zatsu_normal.ttf"
    size 28

translate Japanese style yuri_text_2:
    font "gui/font/gatasosyo.ttf"
    size 36

translate Japanese style yuri_text_3:
    font "gui/font/gatasosyo.ttf"
    size 27
    kerning -12
    language "western"

translate Japanese style natsuki_text:
    font "gui/font/SNsanafonP.ttf"
    size 30

translate Japanese style sayori_text:
    font "gui/font/HolidayMDJP.otf"
    size 30

translate Japanese style monika_text:
    font "gui/font/Ruriiro_font.ttf"
    size 30

translate Japanese python:
    mc = DynamicCharacter('player + "{w}"', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_mc')
    s = DynamicCharacter('s_name', image='sayori', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_s', callback=speaker("sayori"))
    m = DynamicCharacter('m_name', image='monika', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_m', callback=speaker("monika"))
    n = DynamicCharacter('n_name', image='natsuki', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_n', callback=speaker("natsuki"))
    y = DynamicCharacter('y_name', image='yuri', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_y', callback=speaker("yuri"))
    q = DynamicCharacter('"？？？"', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_q')
    mcs = DynamicCharacter('mcs_name', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_mc', callback=speaker("sayori"))
    w = DynamicCharacter('w_name', image='wallace', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")

translate Japanese strings:
    old "Sayori"
    new "サヨリ"

    old "Monika"
    new "モニカ"

    old "Natsuki"
    new "ナツキ"

    old "Yuri"
    new "ユリ"

    old "???"
    new "？？？"

    old "Girl 1"
    new "女子Ａ"

    old "Girl 2"
    new "女子Ｂ"

    old "Girl 3"
    new "女子Ｃ"

    old "[player]&Sayori"
    new "[player]&サヨリ"

    old "Which scene would you like to start?"
    new "どのシーンから始めますか？"

    old "Connection Error!\nIf it does not improve even after waiting, please contact the creator's Twitter.(@horizonmayone)"
    new "接続エラーが発生しました！\n待っても改善されなければ、制作者のTwitterへご連絡ください。(@horizonmayone)"

    old "Couldn't check for the latest version because the server could not be contacted."
    new "サーバーに接続できなかったため、最新のバージョンを確認できませんでした。"

    old "I turned off the automatic confirmation feature."
    new "自動確認の機能をオフにしました。"

    old "Do not close the game while it is downloading."
    new "ダウンロード中はゲームを閉じないでください。"

    old "An error occurred while downloading.\nIf you can't do it again, please contact the creator's Twitter(@horizonmayone)."
    new "ダウンロード中にエラーが発生しました。\n再度実行してもダウンロードできない場合、製作者のTwitter(@horizonmayone)までご連絡ください。"

    old "Would you like to import DDLC's player name?"
    new "DDLCの主人公名を引き継ぎますか？"

    old "DDLC's player name was not found."
    new "DDLCの主人公名が取得できませんでした。"

    old "DDLC's save data was not found."
    new "DDLCのセーブデータが見つかりませんでした。"

    old "Quit the game. After downloading and updating the patch, please launch the game again.\nSaved latest.zip to your desktop folder."
    new "ゲームを終了します。ダウンロードとパッチ更新後、再度ゲームを起動してください。\nlatest.zipをデスクトップフォルダに保存しました。"

    old "Autosave was not found."
    new "オートセーブが見つかりませんでした。"

    old "Autosave was deleted."
    new "オートセーブを削除しました。"

    old "Autosave was not deleted."
    new "オートセーブが削除されませんでした。"

    old "autosaved."
    new "オートセーブしました。"

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
