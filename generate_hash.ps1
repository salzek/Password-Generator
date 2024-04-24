$filename="C:\Tools\hashcat-6.2.6\pass.txt"

$passwords=Get-Content $filename

cat $filename | ForEach-Object {

echo $_
$random= Get-Random -Maximum 100
$user="test$random"
$pass = $_
net user $user $pass /add
$pass=ConvertTo-SecureString $pass -AsPlainText -Force
$str = "/c dir \\lkasd$random\dxxc"
$Credentials = New-Object -Typename System.Management.Automation.PSCredential -ArgumentList $user, $pass
Start-Process -FilePath "cmd.exe" -ArgumentList $str -Credential $Credentials
net user $user /delete
}