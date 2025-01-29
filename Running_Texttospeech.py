import pyttsx3

#
#engine.say("good morning , bonjour $ ù , %")
#engine.runAndWait()
#engine = pyttsx3.init()
#engine.save_to_file('Hello World' , 'test.mp3')
#engine.runAndWait()

class Running_Texttospeech():

    def __init__(self):
        self.engine = pyttsx3.init()
        

    def entry_check(self,entry=False):
        return False if len(entry)==0 else True
    
    def language(self,language):
        pass
    
    def listen(self,entry,HF,scale,speakingrate):
        if self.entry_check(entry):
            voices = self.engine.getProperty('voices')
            rate = self.engine.getProperty('rate')
            volume = self.engine.getProperty('volume')

            self.engine.getProperty('voice',voices[HF].id)
            self.engine.getProperty('rate',speakingrate)
            self.engine.getProperty('volume',scale)
            self.engine.say(entry)
        else:
            pass

    def save(self,entry):
        pass

    
a = print(Running_Texttospeech().entry_check("$"))