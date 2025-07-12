Add-Type -Assembly System.Windows.Forms
# Display a message box with an information icon
$arg1 = $args[0]
$arg2 = $args[1]
[System.Windows.Forms.MessageBox]::Show("$arg1", "$arg2", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)