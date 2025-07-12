# ダウンロードファイルのURL
$url = "https://ddmc.ddlc-jp.com/download/mod_data/latest.zip"

# アセンブリの読み込み
Add-Type -Assembly System.Windows.Forms

# ステータスファイルのパス
$statusFile = ".\download_status"

# ダウンロード処理
try {
    $response = $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $url -OutFile ".\latest.zip" -UseBasicParsing

    #エラーなくダウンロードできた場合はステータスコード200なので、ステータスファイルに200を入れる
    "200" | Out-File -NoNewline -FilePath $statusFile -Encoding UTF8

    [System.Windows.Forms.MessageBox]::Show("ダウンロードが完了しました。", "DDMC MOD DOWNLOADER", "OK", "Information")
}
catch {
    #HTTPエラーになった場合は、ステータスコードをステータスファイルに書き込む
    if ($_.Exception.Response.StatusCode.Value__ -ne "") {
        $_.Exception.Response.StatusCode.Value__ | Out-File -NoNewline -FilePath $statusFile  -Encoding UTF8
    }
    else{
        "Error" | Out-File -NoNewline -FilePath $statusFile -Encoding UTF8
    }

    [System.Windows.Forms.MessageBox]::Show("ダウンロード中にエラーが発生しました。", "DDMC MOD DOWNLOADER", "OK", "Error")
}
