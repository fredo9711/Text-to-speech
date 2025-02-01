import pyttsx3
from tkinter import filedialog # if i want choose by myself the file location



class Running_Texttospeech():

    def __init__(self):
        self.engine = pyttsx3.init()
        
    def size_check(self,entry=0):
        return False if len(entry)==0 else True
    

    def entry_check(self,entry=''):
        if  self.size_check(entry):
            return True
        return False
        
        
        
    
    def language(self,language):
        pass
    def initialisation_sound(self,HF,scale,speakingrate):
            voices = self.engine.getProperty('voices')
            rate = self.engine.getProperty('rate')
            volume = self.engine.getProperty('volume')

            self.engine.setProperty('voice',voices[HF].id)
            self.engine.setProperty('rate',speakingrate)
            self.engine.setProperty('volume',scale)


    def listen(self,entry,HF,scale,speakingrate):
        
        if self.entry_check(entry):
            self.initialisation_sound(HF,scale,speakingrate)
            self.engine.say(entry)
            self.engine.runAndWait()
        else:
            pass

    def save(self,entry,HF,scale,speakingrate):
        if self.entry_check(entry):
            self.initialisation_sound(HF,scale,speakingrate)
            
            self.engine.save_to_file(entry,entry[0]+".mp3")
            self.engine.runAndWait()

    
