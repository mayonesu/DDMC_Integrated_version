# �_�E�����[�h�t�@�C����URL
$url = "https://ddmc.ddlc-jp.com/download/mod_data/latest.zip"

# �A�Z���u���̓ǂݍ���
Add-Type -Assembly System.Windows.Forms

# �X�e�[�^�X�t�@�C���̃p�X
$statusFile = ".\download_status"

# �_�E�����[�h����
try {
    $response = $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri $url -OutFile ".\latest.zip" -UseBasicParsing

    #�G���[�Ȃ��_�E�����[�h�ł����ꍇ�̓X�e�[�^�X�R�[�h200�Ȃ̂ŁA�X�e�[�^�X�t�@�C����200������
    "200" | Out-File -NoNewline -FilePath $statusFile -Encoding UTF8

    [System.Windows.Forms.MessageBox]::Show("�_�E�����[�h���������܂����B", "DDMC MOD DOWNLOADER", "OK", "Information")
}
catch {
    #HTTP�G���[�ɂȂ����ꍇ�́A�X�e�[�^�X�R�[�h���X�e�[�^�X�t�@�C���ɏ�������
    if ($_.Exception.Response.StatusCode.Value__ -ne "") {
        $_.Exception.Response.StatusCode.Value__ | Out-File -NoNewline -FilePath $statusFile  -Encoding UTF8
    }
    else{
        "Error" | Out-File -NoNewline -FilePath $statusFile -Encoding UTF8
    }

    [System.Windows.Forms.MessageBox]::Show("�_�E�����[�h���ɃG���[���������܂����B", "DDMC MOD DOWNLOADER", "OK", "Error")
}
