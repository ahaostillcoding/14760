Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"
$RepoPath = Split-Path -Parent $MyInvocation.MyCommand.Path

function Invoke-RepoCommand {
    param(
        [Parameter(Mandatory = $true)][string]$FileName,
        [Parameter(Mandatory = $true)][string[]]$Arguments
    )

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FileName
    foreach ($arg in $Arguments) {
        [void]$psi.ArgumentList.Add($arg)
    }
    $psi.WorkingDirectory = $RepoPath
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $psi
    [void]$process.Start()
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()

    [PSCustomObject]@{
        ExitCode = $process.ExitCode
        Output = ($stdout + $stderr).Trim()
    }
}

function Test-CommandAvailable {
    param([string]$Name)
    try {
        $null = Get-Command $Name -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

function Get-GitStatusText {
    $result = Invoke-RepoCommand -FileName "git" -Arguments @("status", "--short", "--branch")
    if ($result.ExitCode -ne 0) {
        return "Git status failed:`r`n$($result.Output)"
    }
    if ([string]::IsNullOrWhiteSpace($result.Output)) {
        return "No changes."
    }
    return $result.Output
}

function Get-PageUrl {
    try {
        $remote = Invoke-RepoCommand -FileName "git" -Arguments @("remote", "get-url", "origin")
        if ($remote.ExitCode -ne 0) { return "" }
        if ($remote.Output -match "github\.com[:/](?<owner>[^/]+)/(?<repo>[^/.]+)(\.git)?$") {
            return "https://$($matches.owner).github.io/$($matches.repo)/"
        }
    }
    catch {}
    return ""
}

function Set-IndexRedirect {
    param([Parameter(Mandatory = $true)][string]$HtmlFileName)

    $encoded = [uri]::EscapeDataString($HtmlFileName)
    $html = @"
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=./$encoded">
  <title>GitHub Pages Site</title>
</head>
<body>
  <p>Opening page. If it does not redirect, click <a href="./$encoded">$HtmlFileName</a>.</p>
</body>
</html>
"@
    Set-Content -LiteralPath (Join-Path $RepoPath "index.html") -Value $html -Encoding UTF8
}

function New-CommitMessage {
    $time = Get-Date -Format "yyyy-MM-dd HH:mm"
    return "Update GitHub Pages site $time"
}

$form = New-Object System.Windows.Forms.Form
$form.Text = "GitHub Pages Publish Tool"
$form.Size = New-Object System.Drawing.Size(900, 680)
$form.MinimumSize = New-Object System.Drawing.Size(820, 580)
$form.StartPosition = "CenterScreen"
$form.Font = New-Object System.Drawing.Font("Microsoft YaHei UI", 9)

$title = New-Object System.Windows.Forms.Label
$title.Text = "Drop HTML/images/PDF files into this folder, then click Publish."
$title.AutoSize = $true
$title.Location = New-Object System.Drawing.Point(16, 14)
$title.Font = New-Object System.Drawing.Font("Microsoft YaHei UI", 10, [System.Drawing.FontStyle]::Bold)
$form.Controls.Add($title)

$pathLabel = New-Object System.Windows.Forms.TextBox
$pathLabel.Location = New-Object System.Drawing.Point(16, 44)
$pathLabel.Size = New-Object System.Drawing.Size(740, 26)
$pathLabel.Text = $RepoPath
$pathLabel.ReadOnly = $true
$form.Controls.Add($pathLabel)

$openFolderButton = New-Object System.Windows.Forms.Button
$openFolderButton.Text = "Open Folder"
$openFolderButton.Location = New-Object System.Drawing.Point(765, 42)
$openFolderButton.Size = New-Object System.Drawing.Size(100, 30)
$openFolderButton.Add_Click({ Start-Process explorer.exe -ArgumentList "`"$RepoPath`"" })
$form.Controls.Add($openFolderButton)

$statusLabel = New-Object System.Windows.Forms.Label
$statusLabel.Text = "Pending changes"
$statusLabel.Location = New-Object System.Drawing.Point(16, 84)
$statusLabel.AutoSize = $true
$statusLabel.Font = New-Object System.Drawing.Font("Microsoft YaHei UI", 9, [System.Drawing.FontStyle]::Bold)
$form.Controls.Add($statusLabel)

$statusBox = New-Object System.Windows.Forms.TextBox
$statusBox.Location = New-Object System.Drawing.Point(16, 108)
$statusBox.Size = New-Object System.Drawing.Size(850, 230)
$statusBox.Multiline = $true
$statusBox.ScrollBars = "Vertical"
$statusBox.ReadOnly = $true
$statusBox.Font = New-Object System.Drawing.Font("Consolas", 9)
$form.Controls.Add($statusBox)

$commitLabel = New-Object System.Windows.Forms.Label
$commitLabel.Text = "Commit note"
$commitLabel.Location = New-Object System.Drawing.Point(16, 356)
$commitLabel.AutoSize = $true
$form.Controls.Add($commitLabel)

$commitBox = New-Object System.Windows.Forms.TextBox
$commitBox.Location = New-Object System.Drawing.Point(100, 352)
$commitBox.Size = New-Object System.Drawing.Size(590, 26)
$commitBox.Text = New-CommitMessage
$form.Controls.Add($commitBox)

$refreshMessageButton = New-Object System.Windows.Forms.Button
$refreshMessageButton.Text = "New Note"
$refreshMessageButton.Location = New-Object System.Drawing.Point(705, 350)
$refreshMessageButton.Size = New-Object System.Drawing.Size(100, 30)
$refreshMessageButton.Add_Click({ $commitBox.Text = New-CommitMessage })
$form.Controls.Add($refreshMessageButton)

$htmlLabel = New-Object System.Windows.Forms.Label
$htmlLabel.Text = "Home HTML"
$htmlLabel.Location = New-Object System.Drawing.Point(16, 399)
$htmlLabel.AutoSize = $true
$form.Controls.Add($htmlLabel)

$htmlCombo = New-Object System.Windows.Forms.ComboBox
$htmlCombo.Location = New-Object System.Drawing.Point(100, 395)
$htmlCombo.Size = New-Object System.Drawing.Size(360, 28)
$htmlCombo.DropDownStyle = "DropDownList"
$form.Controls.Add($htmlCombo)

$setIndexCheck = New-Object System.Windows.Forms.CheckBox
$setIndexCheck.Text = "Use selected HTML as home page"
$setIndexCheck.Location = New-Object System.Drawing.Point(480, 397)
$setIndexCheck.Size = New-Object System.Drawing.Size(240, 24)
$setIndexCheck.Checked = $true
$form.Controls.Add($setIndexCheck)

$logLabel = New-Object System.Windows.Forms.Label
$logLabel.Text = "Environment and publish log"
$logLabel.Location = New-Object System.Drawing.Point(16, 448)
$logLabel.AutoSize = $true
$logLabel.Font = New-Object System.Drawing.Font("Microsoft YaHei UI", 9, [System.Drawing.FontStyle]::Bold)
$form.Controls.Add($logLabel)

$envBox = New-Object System.Windows.Forms.TextBox
$envBox.Location = New-Object System.Drawing.Point(16, 472)
$envBox.Size = New-Object System.Drawing.Size(850, 95)
$envBox.Multiline = $true
$envBox.ScrollBars = "Vertical"
$envBox.ReadOnly = $true
$envBox.Font = New-Object System.Drawing.Font("Consolas", 9)
$form.Controls.Add($envBox)

$refreshButton = New-Object System.Windows.Forms.Button
$refreshButton.Text = "Refresh"
$refreshButton.Location = New-Object System.Drawing.Point(16, 590)
$refreshButton.Size = New-Object System.Drawing.Size(100, 34)
$form.Controls.Add($refreshButton)

$checkButton = New-Object System.Windows.Forms.Button
$checkButton.Text = "Check Env"
$checkButton.Location = New-Object System.Drawing.Point(130, 590)
$checkButton.Size = New-Object System.Drawing.Size(110, 34)
$form.Controls.Add($checkButton)

$publishButton = New-Object System.Windows.Forms.Button
$publishButton.Text = "Publish"
$publishButton.Location = New-Object System.Drawing.Point(255, 590)
$publishButton.Size = New-Object System.Drawing.Size(130, 34)
$publishButton.BackColor = [System.Drawing.Color]::FromArgb(15, 139, 111)
$publishButton.ForeColor = [System.Drawing.Color]::White
$form.Controls.Add($publishButton)

$openSiteButton = New-Object System.Windows.Forms.Button
$openSiteButton.Text = "Open Site"
$openSiteButton.Location = New-Object System.Drawing.Point(400, 590)
$openSiteButton.Size = New-Object System.Drawing.Size(110, 34)
$form.Controls.Add($openSiteButton)

$closeButton = New-Object System.Windows.Forms.Button
$closeButton.Text = "Close"
$closeButton.Location = New-Object System.Drawing.Point(765, 590)
$closeButton.Size = New-Object System.Drawing.Size(100, 34)
$closeButton.Add_Click({ $form.Close() })
$form.Controls.Add($closeButton)

function Refresh-HtmlList {
    $selected = $htmlCombo.SelectedItem
    $htmlCombo.Items.Clear()
    Get-ChildItem -LiteralPath $RepoPath -Filter "*.html" -File |
        Where-Object { $_.Name -ne "index.html" } |
        Sort-Object LastWriteTime -Descending |
        ForEach-Object { [void]$htmlCombo.Items.Add($_.Name) }

    if ($selected -and $htmlCombo.Items.Contains($selected)) {
        $htmlCombo.SelectedItem = $selected
    }
    elseif ($htmlCombo.Items.Count -gt 0) {
        $htmlCombo.SelectedIndex = 0
    }
}

function Refresh-Status {
    try {
        Refresh-HtmlList
        $statusBox.Text = Get-GitStatusText
    }
    catch {
        $statusBox.Text = $_.Exception.Message
    }
}

function Check-Environment {
    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add("Repo: $RepoPath")
    if (Test-CommandAvailable "git") {
        $lines.Add("Git: " + (Invoke-RepoCommand -FileName "git" -Arguments @("--version")).Output)
    }
    else {
        $lines.Add("Git: not found")
    }

    if (Test-CommandAvailable "gh") {
        $ghVersion = (Invoke-RepoCommand -FileName "gh" -Arguments @("--version")).Output.Split("`n")[0]
        $lines.Add("GitHub CLI: $ghVersion")
        $auth = Invoke-RepoCommand -FileName "gh" -Arguments @("auth", "status")
        $lines.Add("gh auth status:")
        $lines.Add($auth.Output)
    }
    else {
        $lines.Add("GitHub CLI: not found in PATH")
    }

    $branch = Invoke-RepoCommand -FileName "git" -Arguments @("branch", "--show-current")
    $remote = Invoke-RepoCommand -FileName "git" -Arguments @("remote", "-v")
    $lines.Add("Branch: $($branch.Output)")
    $lines.Add("Remote:")
    $lines.Add($remote.Output)
    $envBox.Text = ($lines -join "`r`n")
}

$refreshButton.Add_Click({ Refresh-Status })
$checkButton.Add_Click({ Check-Environment })
$openSiteButton.Add_Click({
    $url = Get-PageUrl
    if ([string]::IsNullOrWhiteSpace($url)) {
        [System.Windows.Forms.MessageBox]::Show("Could not detect GitHub Pages URL.", "Notice") | Out-Null
    }
    else {
        Start-Process $url
    }
})

$publishButton.Add_Click({
    try {
        $publishButton.Enabled = $false
        $envBox.Text = "Preparing commit..."

        if ($setIndexCheck.Checked -and $htmlCombo.SelectedItem) {
            Set-IndexRedirect -HtmlFileName ([string]$htmlCombo.SelectedItem)
        }

        $statusBefore = Get-GitStatusText
        if ($statusBefore -eq "No changes.") {
            $envBox.Text = "No changes to publish."
            Refresh-Status
            return
        }

        $message = $commitBox.Text.Trim()
        if ([string]::IsNullOrWhiteSpace($message)) {
            $message = New-CommitMessage
        }

        $log = New-Object System.Collections.Generic.List[string]

        $log.Add("git add .")
        $add = Invoke-RepoCommand -FileName "git" -Arguments @("add", ".")
        if ($add.ExitCode -ne 0) { throw $add.Output }

        $log.Add("git commit")
        $commit = Invoke-RepoCommand -FileName "git" -Arguments @("commit", "-m", $message)
        $log.Add($commit.Output)
        if ($commit.ExitCode -ne 0) { throw $commit.Output }

        $log.Add("git push")
        $push = Invoke-RepoCommand -FileName "git" -Arguments @("push")
        $log.Add($push.Output)
        if ($push.ExitCode -ne 0) { throw $push.Output }

        $url = Get-PageUrl
        $log.Add("")
        if ([string]::IsNullOrWhiteSpace($url)) {
            $log.Add("Publish complete.")
        }
        else {
            $log.Add("Publish complete. Site: $url")
        }

        $envBox.Text = ($log -join "`r`n")
        Refresh-Status
    }
    catch {
        $envBox.Text = "Publish failed:`r`n$($_.Exception.Message)"
    }
    finally {
        $publishButton.Enabled = $true
    }
})

$form.Add_Shown({
    Refresh-Status
    Check-Environment
})

[void]$form.ShowDialog()
