# -*- coding: utf-8 -*-
import platform
import os
import sys
import ctypes

root_path = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_path)

print("Current Python Version: {}".format(platform.python_version()))

mod = __import__('lib_syscall_map_{}'.format(platform.machine()))

SYSCALL_MAP = mod.SYSCALL_MAP

libc = ctypes.CDLL("libc.so.6")

def syscall(entry, *args):
    return libc.syscall(SYSCALL_MAP[entry], *args)

def do_op(name, *args):
    print(name, end=': ')
    if len(args) > 1:
        print(syscall(args[0], *args[1:]))
    elif len(args) > 0:
        print(syscall(args[0]))
    else:
        print("Please type entry for ", name)

s = b"Hello World!\n"

do_op('write', 'write', 2, s, len(s))
do_op('PID', 'getpid')
do_op('Thread ID', 'gettid')
do_op('UID', 'getuid')
do_op('GID', 'getgid')

pid = syscall('fork')
if pid == 0:
    print("In Child pid is {}".format(syscall("getpid")))
else:
    print("In parent {} and child pid is {}.".format(syscall("getpid"), pid))




