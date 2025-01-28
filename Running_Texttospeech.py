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
    
    def listen(self,entry):
        self.engine.say(entry)

    def save(self,entry):
        pass

    
a = print(Running_Texttospeech().entry_check("$"))