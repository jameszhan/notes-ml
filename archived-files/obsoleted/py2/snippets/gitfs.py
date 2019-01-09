#!/usr/bin/python

import os
import sys
import subprocess
import errno
import datetime
import stat
import fuse
from fuse import Fuse
from threading import Lock

fuse.fuse_python_api = (0, 2)

class Git():
    
    def __init__(self, repodir):
        self.repodir = repodir
        self.lock = Lock()

    def init(self):
        cmd = "git init "
        
        
        if ".git" in os.listdir(self.repodir):
            self.addAll()
            return;
        
        self.lock.acquire()        
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
            
        self.addAll()
        return
    
    def addAll(self):
    
        cmd = "git add ."
        self.lock.acquire()
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
        return
    
    def add(self, path):
        
        cmd = "git add " + path
        self.lock.acquire()         
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        self.lock.release()
        pipe.wait()
        return

    def commit(self):
        
        cmd = "git commit -m '" + str(datetime.datetime.now()) +"'"
        self.lock.acquire()        
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
        return
    
    def mv(self, old_path, new_path):

        cmd = "git mv " + old_path + " " + new_path
    
        self.lock.acquire()
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
        
        if self.repodir in new_path:
            self.add(new_path)
        
        self.commit()
        return
    
    def rm(self, path):
        cmd = "git rm " + path
        self.lock.acquire()
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
        self.commit()
        return
    
    def rmdir(self, path):
        cmd = "git rm -rf " + path
        self.lock.acquire()
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repodir)
        pipe.wait()
        self.lock.release()
        self.commit()
        return

class FileWrapper(fuse.FuseFileInfo):
       
       def __init__(self, fd):
            self.fd = fd
            self.direct_io = False;
            self.keep_cache = False;

class GitFS(Fuse):
    
    repo = ""
    git = ""
        
    def __init__(self, *args, **kw):
        
        self.repo = os.getcwd()
        Fuse.__init__(self, *args, **kw)        


        '''def mythread ( self ):
        print '*** mythread'
        return -errno.ENOSYS
                        '''
    def access(self, path, mode):
        path = os.path.normpath(self.repo + os.sep + path)
        if not os.access(path, mode):
            return -os.errno.EACCES
        
        return 0
    
    def getattr(self, path):
        
        if path == "/.git":
            return -errno.ENOENT             
        
        path = os.path.normpath(self.repo + os.sep + path)
        return os.stat(path)

    def readdir(self, path, offset):
        
        path = os.path.normpath(self.repo + os.sep + path)
         
        listings = os.listdir(path)
        listings.append(".")
        listings.append("..")
        
        if ".git" in listings:       
            listings.remove(".git")
      
        for e in listings: 
            yield fuse.Direntry(e)

    def chmod ( self, path, mode ):
        
        path = os.path.normpath(self.repo + os.sep + path)
        return os.chmod(path, mode)

    def chown ( self, path, uid, gid ):
        
        path = os.path.normpath(self.repo + os.sep + path)
        return os.chown(path, uid, gid)

    def link ( self, targetPath, linkPath ):
        
        return -errno.ENOSYS

    def mkdir ( self, path, mode ):
        
        path = os.path.normpath(self.repo + os.sep + path)
        return os.mkdir(path, mode)
    
    def readlink ( self, path ):

        return -errno.ENOSYS
     
    def rename ( self, oldPath, newPath ):

        oldPath = os.path.normpath(self.repo + os.sep + oldPath)
        newPath = os.path.normpath(self.repo + os.sep + newPath)
        
        'This raises an exception and will not continue on ENOENT'
        os.stat(oldPath)
        self.git.mv(oldPath, newPath)
        return 0

    def rmdir ( self, path ):
        
        path = os.path.normpath(self.repo + os.sep + path)

        stats = os.stat(path)
        if not stat.S_ISDIR(stats):
            return -os.errno.ENOENT
        
        self.git.rmdir(path)
        return 0

    def statfs ( self ):
        
        return os.statvfs(self.repo)

    def unlink ( self, path ):
        
        path = os.path.normpath(self.repo + os.sep + path)
        
        'This raises an exception and will not continue on ENOENT'
        os.stat(path)
        self.git.rm(path)
        return 0

    def utime ( self, path, times ):
        
        path = os.path.normpath(self.repo + os.sep + path)
        return os.utime(path, times)
    
    def truncate(self, path, len):
        path = os.path.normpath(self.repo + os.sep + path)
        f = open(path, "a")
        f.truncate(len)
        f.close()
        return 0
    
    '''These functions used to be in the File Class, but now the
    new fuse API lets you specify an arbitrary file handle. 
    But you cannot return an object of type int unless on an error so I had to use 
    a wrapper class'''
    
    def open(self, path, flags, *mode):
        
        path = os.path.normpath(self.repo + os.sep + path)
        print("Open called for " + path)
        return FileWrapper((os.open(path, flags, *mode)))
        
    def mknod(self, path, mode, dev):
        
        path = os.path.normpath(self.repo + os.sep + path)
        print("mknod for path " + path + "mode " + str(mode) + "dev " + str(dev))
        
        if (mode & (1 << 15)):
            print("mode being set to 666")
            mode = 0o666
        
        return os.mknod(path, mode, dev)
         
    def read(self, path, length, offset, file=None):
        
        fd = file.fd
        os.lseek(fd, offset, os.SEEK_SET)
        return os.read(fd, length)
    
    def write(self, path, buf, offset, file=None): 
        
        os.lseek(file.fd, offset, os.SEEK_SET)
        os.write(file.fd, buf) 
        return len(buf)
      
    def ftruncate(self, path, len, file=None): 
        
        return os.ftruncate(file.fd, len)

    def flush(self, path, file=None): 

        return os.fsync(file.fd)

    def release(self, path, flags, file=None):
        
        os.close(file.fd)
        path = os.path.normpath(self.repo + os.sep + path)
        self.git.add(path)
        self.git.commit()
        return 0
    
    def fsync(self, path, fdatasync, file=None):
        return os.fsync(file.fd) 

    
    def fgetattr(self, path, file=None):
        
        return os.fstat(file.fd)
 

if __name__ == "__main__":
        
    fs = GitFS()
    fs.parser.add_option(mountopt="repo", metavar="REPODIR", default=fs.repo,
                             help="Directory to/for Git Repository [default: Current Working directory on mount]")
    
    fs.parse(values=fs, errex=1)
    
    fs.flags = 0
    fs.multithreaded = True

    if not os.path.isdir(fs.repo):
        sys.exit(fs.repo + "is not a directory, create it first! ")
    
    '''Now that fuse hase parsed the options, instantiate your git object
       And initialize the repo'''
    fs.git = Git(fs.repo)
    fs.git.init()
    fs.main()
