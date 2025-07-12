Add-Type -Assembly System.Windows.Forms
# Display a message box with an information icon
[System.Windows.Forms.MessageBox]::Show("みんなオッケー？", "DDLC.exe", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)