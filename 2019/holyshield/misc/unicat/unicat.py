#!/usr/bin/python3.7

import sys, random
from typing import List


stdin = sys.stdin
stdout = sys.stdout

def set_stdin(buffer):
    global stdin
    stdin = buffer

def set_stdout(buffer):
    global stdout
    stdout = buffer


class RunException(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

class Memory:
    def __init__(self, size):
        self.size = size
        self.mem = [0 for _ in range(size)]
        

    def __getitem__(self, idx):
        if idx >= self.size:
            raise RunException("Memory Error")
        return self.mem[idx]

    def __setitem__(self, idx, value):
        self.mem[idx] = value

    def setip(self, ip):
        self.mem[-1] = ip
    
    def ip(self):
        return self[-1]

    def nextip(self, size=1):
        self.setip(self.ip() + size)


class CommandFetcher:
    def __init__(self, code):
        self.code = code

    def next(self, ip):
        try:
            cmd = self.code[ip:ip+2]
            if cmd == [3,1]:
                args, size = self.parseargs(ip+2, 2)
                return SetCommand(args, size+2)
            if cmd == [5,4]:
                args, size = self.parseargs(ip+2, 1)
                return EchoCharCommand(args, size+2)
            if cmd == [4,4]:
                args, size = self.parseargs(ip+2, 1)
                return EchoNumCommand(args, size+2)
            if cmd == [2,4]:
                args, size = self.parseargs(ip+2, 1)
                return InputCommand(args, size+2)
            if cmd == [5,7]:
                args, size = self.parseargs(ip+2, 2)
                return JgzCommand(args, size+2)
            if cmd == [4,6]:
                args, size = self.parseargs(ip+2, 1)
                return PointerCommand(args, size+2)
            if cmd == [8,3]:
                args, size = self.parseargs(ip+2, 1)
                return RandomCommand(args, size+2)
            if cmd == [8,8]:
                return HltCommand([],2)
            if cmd == [7,8]:
                flag = self.code[ip+2]
                args, size = self.parseargs(ip+3, 2)

                if flag == 1:
                    func = lambda a,b:a+b
                elif flag == 2:
                    func = lambda a,b:a-b
                elif flag == 8:
                    func = lambda a,b:a*b
                elif flag == 7:
                    func = lambda a,b:a//b
                else:
                    func = lambda a,b:a+b
                return CalcCommand(args, size+3, func)

        except IndexError:
            raise RunException("Invalid Operation")
        raise RunException("Invalid Command")



    def isend(self, ip):
        return len(self.code) <= ip;

    def readint(self, ip):
        try:
            o = ""
            while not (o.endswith("88") or o.endswith("87")):
                o += str(self.code[ip])
                ip+=1
            r = int(o[:-2], 8)
            if o.endswith("87"):
                r = -r;
            val = r
        except:
            raise RunException("Invalid Operation")
        return (val, len(o))
    
    def parseargs(self, ip, count):
        args = []
        nip = ip
        for i in range(count):
            arg, size = self.readint(nip)
            args.append(arg)
            nip += size
        return (args, nip-ip)




class Command:
    def __init__(self, args, size):
        self.args = args
        self._size = size

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, str(self.args))

    def size(self):
        return self._size

    def execute(self, mem: Memory):
        return 2


class SetCommand(Command):
    def execute(self, mem: Memory):
        mem[self.args[0]] = self.args[1]
        return 1

class EchoCharCommand(Command):
    def execute(self, mem: Memory):
        stdout.write(chr(mem[self.args[0]]))
        return 1

class EchoNumCommand(Command):
    def execute(self, mem: Memory):
        stdout.write(str(mem[self.args[0]]))
        return 1

class InputCommand(Command):
    def execute(self, mem: Memory):
        buf = stdin.readline()
        for i in range(len(buf)):
            mem[self.args[0] + i] = ord(buf[i])
        return 1

class CalcCommand(Command):
    def __init__(self, args, size, func=lambda a,b:0):
        super().__init__(args,size)
        self.func = func
    def execute(self, mem: Memory):
        mem[self.args[0]] = self.func(mem[self.args[0]], mem[self.args[1]])
        return 1

class JgzCommand(Command):
    def execute(self, mem: Memory):
        if mem[self.args[0]] > 0:
            mem.setip(self.args[1])
        return 1

class PointerCommand(Command):
    def execute(self, mem: Memory):
        mem[self.args[0]] = mem[mem[self.args[0]]]
        return 1

class RandomCommand(Command):
    def execute(self, mem: Memory):
        mem[self.args[0]] = random.randint(0,1)
        return 1

class HltCommand(Command):
    def execute(self, mem: Memory):
        return 0




MEM_SIZE = 0xffff

def preprocess(raw: str):
    output = []
    
    for c in raw:
        if c == '\n' or c == ' ' or c == '\t' or c == '\r':
            continue
        t = ord(c) - 0x1f638
        if t < 0 or t > 8:
            return None
        output.append(t)

    return output


def run(code: List[int], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stdout):

    set_stdin(stdin)
    set_stdout(stdout)


    mem = Memory(MEM_SIZE)
    
    mem.setip(0)
    pos=0

    cf = CommandFetcher(code)
    cmds : List[Command] = []
    
    try:
        while not cf.isend(pos):
            cmd = cf.next(pos)
            pos += cmd.size()
            cmds.append(cmd)

    
        while mem.ip() < len(cmds):
            cmd = cmds[mem.ip()]
            msg = cmd.execute(mem)
            mem.nextip()
            if msg == 0:
                break
    except RunException as e:
        stderr.write("\n"+str(e))
        return False
    return True


if __name__ == "__main__":

    if len(sys.argv) == 1:
        raw = input()
    elif len(sys.argv) == 2:
        try:
            filename = sys.argv[1]
            with open(filename, 'rb') as fp:
                data = fp.read()
                raw = data.decode('utf-8')
        except:
            print("No such file '%s' or unreadable." % sys.argv[1])
            exit(1)
    else:
        print("Usage: {} [FILENAME]".format(sys.argv[0]))


    code = preprocess(raw)
    if code == None:
        print("Invalid Character")
        exit(1)
    run(code)
