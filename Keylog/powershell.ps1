Param ( [string]$Att,
        [string]$Subj,
        [string]$Body
        )

Function Send-Email
{
        Param( 
                [Parameter(`
                Mandatory=$true)]
                [string]$To,
                [Parameter(`
                 Mandatory=$true)]
                [string]$From,
                [Parameter(`
                 Mandatory=$true)]
                 [string]$Password,
                [Parameter(`
                 Mandatory=$true)]
                 [string]$Subject,
                [Parameter(`
                 Mandatory=$true)]
                 [string]$Body,
                [Parameter(`
                 Mandatory=$true)]
                 [string]$attachment
                 )
            
    try
    {
        $Msg =New-Object System.Net.Mail.MailMessage($From, $To, $Subject,$Body)
        $Srv = "smtp.gmail.com"
        if($attachment -ne $null)
        {
            try
            {
                $Attachments = $attachment -split ("\:\:");
                ForEach($val in $Attachments)
                {
                    $attch = New-Object System.Net.Mail.Attachment($val)
                    $Msg.Attachments.Add($attch)
                }
            }
            catch
            {
                exit 2;
            }
            $Client = New-Object Net.Mail.SmtpClient($Srv, 587)
            $Client.EnableSsl = $true
            $Client.Credentials = New-Object System.Net.NetworkCredential($From.Split("@")[0],$Password);
            $Client.Send($Msg)
            Remove-Variable -Name Client
            Remove-Variable -Name Password
            exit 7;
        }
    }
    catch
    {
        exit 3;
    }          
  
    try
    {
        Send-Email
            -attachment $Att
            -To "Address of the recipient"
            -Body $Body
            -Subject $Subj
            -password "rasdasd"
            -From "Address of the sender"

    } 
    catch
    {
    exit 4;
    }
            
            
}