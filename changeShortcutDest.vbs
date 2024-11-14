' Get the path of the script itself
Dim fso, shell, folderPath
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

' Set folderPath to the folder where the script is located
folderPath = fso.GetParentFolderName(WScript.ScriptFullName)

Dim targetString
targetString = InputBox("Enter the new target path for all shortcuts in this folder (leave empty for rick rolls):", "Set Shortcut Target")

' Exit if no input was provided
If targetString = "" Then
    targetString = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1"
End If

' Get the folder
Dim folder
Set folder = fso.GetFolder(folderPath)

' Loop through each file in the folder
Dim file
For Each file In folder.Files
    ' Check if the file has a .lnk extension (indicating it's a shortcut)
    If LCase(fso.GetExtensionName(file.Name)) = "lnk" Then
        On Error Resume Next
        ' Try to change the shortcut target
        Dim shortcut
        Set shortcut = shell.CreateShortcut(file.Path)
        
        If Err.Number = 0 Then
            shortcut.TargetPath = targetString
            shortcut.Save
'            WScript.Echo "Shortcut updated: " & file.Name
'        Else
'            WScript.Echo "Could not update shortcut (access denied or other error): " & file.Name
        End If
        
        ' Clear any error and reset shortcut object
        Err.Clear
        Set shortcut = Nothing
        On Error GoTo 0
'    Else
'        WScript.Echo "Not a shortcut: " & file.Name
    End If
Next

' Clean up
Set fso = Nothing
Set shell = Nothing
