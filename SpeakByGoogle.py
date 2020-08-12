from gtts import gTTS
import subprocess as s

voz = gTTS("Hello Chris", lang="pt")
voz.save("voz.mp3")

s.call(['wmplayer.exe', 'voz.mp3'])
