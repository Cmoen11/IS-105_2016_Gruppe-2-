import speech_recognition as sr
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 100)
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()
m = sr.Microphone()

def input_voice() :
    
    try :
        with m as source: r.adjust_for_ambient_noise(source)
        while True:
            print("Say something")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
    
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes: # this version of Python uses bytes for strings (Python 2)
                    print(u"You said {}".format(value).encode("utf-8"))
                    return format(value).encode("utf-8")
                else: # this version of Python uses unicode for strings (Python 3+)
                    return format(value)
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                
    except KeyboardInterrupt:
        pass



# Clean up the input, so it is easier to handle.
def redefineAnswer(answer) :
    input_answer = str(answer)
    return input_answer.upper()

# Find out an answer
def output_answer(input_answer) :
    
    if "HELLO" in input_answer :
        print '!'
        input_hello()
        
    elif "COUNT" in input_answer :
        engine.say("1 2 3 4 5 6 7 8 9 10")
        engine.runAndWait()
        
    else : 
        engine.say("Please try again")
        
        engine.runAndWait()
    

# if the first setence is 'hello'
def input_hello():
    engine.say('hi, how are you?')
    engine.runAndWait()
    answer = input_voice()
    answer = redefineAnswer(answer)
    
    goodAnswers = ['GREAT',"OK", 'GOOD', 'FINE', 'HAPPY']
    badAnswers = ['BAD', 'SAD', 'UNHAPPY']
    
    # For good answers
    for answers in goodAnswers:
        if (answers in answer) :
            engine.say('Nice! ' + 'I like when you\'re '+answers)
            engine.runAndWait()
            return True
    
    # For bas answers        
    for answers in badAnswers:
        if (answers in answer) :
            engine.say("I am sorry to hear that.. I do not like when you're "+answers)
            engine.runAndWait()
            return False
    
    # if the question was not answered correctly
    engine.say("Didn't catch that")
    engine.runAndWait()
    input_hello()
        


while(True) :
    answer = redefineAnswer(input_voice())
    output_answer(answer)