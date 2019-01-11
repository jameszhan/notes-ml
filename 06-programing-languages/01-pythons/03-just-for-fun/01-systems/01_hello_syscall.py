# -*- coding: utf-8 -*-
import ctypes

libc = ctypes.CDLL(None)
syscall = libc.syscall

print("Pid: ", syscall(39))
