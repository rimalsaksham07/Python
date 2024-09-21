def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        reply = input(prompt)
        if reply in {'y','yep','yes'}:
            return True
        if reply in {'n','no','nop','nope'}:
            return False
        if retries < 0 :
            raise ValueError('Invlaid user response')
        print(reminder)
