import subprocess
ps = "C:/Windows/syswow64/windowspowershell/v1.0/powershell.exe"
subprocess.call(ps + " Get-Process Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))", shell=True)
subprocess.call(ps + " choco install openssh /SSHServerFeature")
subprocess.call(ps + " choco install ngrok")
