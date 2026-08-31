' AItutor: open the project folder in File Explorer
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")
folder = fso.GetParentFolderName(WScript.ScriptFullName)
shell.Run "explorer.exe """ & folder & """", 1, False
