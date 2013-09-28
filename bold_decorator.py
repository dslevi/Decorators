class bold(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        return "<b> " + self.f() + " </b>"

@bold
def something():
    return "something"

@bold
def x():
    return "this is not bold...yet"

print something()
print x()