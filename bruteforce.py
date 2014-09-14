# ------------------------------------------------------------
# ----------------Woodpecker hash bruteforce------------------
#
# This software is used to perform bruteforce of hashes of various types.
# This software was created JUST FOR FUN, it is NOT a tool for hackers!
# I cannot stop you from doing this, but this tool was made to perform
# LEGAL penteration-testing, not for hacking. This programme is completely free and
# opensource, so you can modify the code as you want.

# If you are interested in bruteforce, visit  http://brute.heliohost.org 

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------
import sys,time,hashlib,shelve,multiprocessing

from PyQt4 import QtCore, QtGui
from brute_gui import Ui_GroupBox
from Crypto.Hash import MD2, MD4
from itertools import product,islice

class BruteStoppedEx(Exception):
    def __init__(self,data):
        pass

def Grouper(n,dict,length):
    i=iter(dict)
    res=[]
    if n==1:
        res.append(dict)
        return res
    cont=(length)//n
    oldNDX=0
    for ndx in xrange(1,length+1,cont):
        res.append(islice(dict,oldNDX,ndx))
        oldNDX=ndx
    if oldNDX!=length:
        res.append(islice(dict,oldNDX,length))
    return res

class gui(QtGui.QGroupBox):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.Settings_md2= QtGui.QAction('MD2', self)
        self.ui.settings_hashType.addAction(self.Settings_md2)
        self.Settings_md4= QtGui.QAction('MD4', self)
        self.ui.settings_hashType.addAction(self.Settings_md4)
        self.Settings_md5= QtGui.QAction('MD5', self)
        self.ui.settings_hashType.addAction(self.Settings_md5)
        self.Settings_sha1= QtGui.QAction('SHA-1', self)
        self.ui.settings_hashType.addAction(self.Settings_sha1)
        self.Settings_sha224= QtGui.QAction('SHA-224', self)
        self.ui.settings_hashType.addAction(self.Settings_sha224)
        self.Settings_sha256= QtGui.QAction('SHA-256', self)
        self.ui.settings_hashType.addAction(self.Settings_sha256)
        self.Settings_sha384= QtGui.QAction('SHA-384', self)
        self.ui.settings_hashType.addAction(self.Settings_sha384)
        self.Settings_sha512= QtGui.QAction('SHA-512', self)
        self.ui.settings_hashType.addAction(self.Settings_sha512)



        QtCore.QObject.connect(self.ui.start,QtCore.SIGNAL("clicked()"), self.start_brute)
        QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_brute)
        QtCore.QObject.connect(self.ui.Hash,QtCore.SIGNAL("returnPressed()"), self.start_brute)
        QtCore.QObject.connect(self.Settings_md2, QtCore.SIGNAL('triggered()'), self.setMD2)
        QtCore.QObject.connect(self.Settings_md4, QtCore.SIGNAL('triggered()'), self.setMD4)
        QtCore.QObject.connect(self.Settings_md5, QtCore.SIGNAL('triggered()'), self.setMD5)
        QtCore.QObject.connect(self.Settings_sha1, QtCore.SIGNAL('triggered()'), self.setSHA1)
        QtCore.QObject.connect(self.Settings_sha256, QtCore.SIGNAL('triggered()'), self.setSHA256)
        QtCore.QObject.connect(self.Settings_sha224, QtCore.SIGNAL('triggered()'), self.setSHA224)
        QtCore.QObject.connect(self.Settings_sha384, QtCore.SIGNAL('triggered()'), self.setSHA384)
        QtCore.QObject.connect(self.Settings_sha512, QtCore.SIGNAL('triggered()'), self.setSHA512)

        try:
            self.set=shelve.open("config",writeback=True)
        except:
            self.ui.results.setText("WARNING! Unable to save your settings!")
        try:
            self.htype=self.set["hash_type"]
        except:
            self.htype="md5"
        self.set["hash_type"]=self.htype
        self.set.sync()
        self.htype=self.set["hash_type"]
        self.ha=self.ui.Hash.text()
        self.wordLength=self.ui.word_len_spin.value()
        self.min_wordLength=self.ui.word_len_min_spin.value()
        self.thread1=Worker(self.ha,self.htype,self.wordLength,self.min_wordLength)
        self.connect(self.thread1, QtCore.SIGNAL('test(const QString)'), self.ui.results.setText)
    def stop_brute(self):
        self.thread1.stopped=True
        self.ui.results.setText("Stopped")
    def setMD2(self):
        self.htype="md2"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: MD2")
        self.set.sync()
    def setMD4(self):
        self.htype="md4"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: MD4")
        self.set.sync()
    def setMD5(self):
        self.htype="md5"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: MD5")
        self.set.sync()
    def setSHA1(self):
        self.htype="sha1"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: SHA-1")
        self.set.sync()
    def setSHA224(self):
        self.htype="sha224"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: SHA-224")
        self.set.sync()
    def setSHA256(self):
        self.htype="sha256"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: SHA-256")
        self.set.sync()
    def setSHA384(self):
        self.htype="sha384"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: SHA-384")
        self.set.sync()
    def setSHA512(self):
        self.htype="sha512"
        self.set["hash_type"]=self.htype
        self.ui.results.setText("Hashing algorythm: SHA-512")
        self.set.sync()
    def ShowMore(self):
        pass
    def ProcessData(self,data):
        self.ui.results.setText(data)
    def start_brute(self):
        self.ha=str(self.ui.Hash.text())
        self.wordLength=int(self.ui.word_len_spin.value())
        self.min_wordLength=int(self.ui.word_len_min_spin.value())

        THREADS=xrange(2)
        
        # TODO: tried to add parallel processing, but failed...

#a=StartWorkers(self,THREADS)
#a.run()

        #print self.ha,self.htype

#th_list=[]
#for thread in THREADS:
#     	th_list.append(Worker(self.ha,self.htype,self.wordLength,self.min_wordLength,thread))
#   for th in th_list:
#       	self.connect(th, QtCore.SIGNAL('test(const QString)'), self.ProcessData)
#       	self.connect(th, QtCore.SIGNAL('Important(const QString)'),self.ui.results.setText)
#       	th.start()

        self.thread1=Worker(self.ha,self.htype,self.wordLength,self.min_wordLength)
        self.connect(self.thread1, QtCore.SIGNAL('test(const QString)'), self.ProcessData)#self.ui.results.setText)
        self.connect(self.thread1, QtCore.SIGNAL('Important(const QString)'),self.ui.results.setText)
        self.thread1.start()

class StartWorkers(QtCore.QThread):
    def __init__(self,Parent,Threads):
        QtCore.QThread.__init__(self)
        self.Threads=Threads
        self.Parent=Parent
    def run(self):
        th_list=[]
        for thread in self.Threads:
            th_list.append(Worker(self.Parent.ha,self.Parent.htype,self.Parent.wordLength,self.Parent.min_wordLength,thread))
        for th in th_list:
            self.Parent.connect(th, QtCore.SIGNAL('test(const QString)'), self.Parent.ProcessData)
            self.Parent.connect(th, QtCore.SIGNAL('Important(const QString)'),self.Parent.ui.results.setText)
            th.start()

class Data:
    RES=False

class Worker(QtCore.QThread):
    def __init__(self,Hash,htype,WordLen,min_WordLen):
        QtCore.QThread.__init__(self)
        self.htype=str(htype)
        try:
            self.hash = str(Hash)
        except:
            self.hash=""
        self.min_WordLen=int(min_WordLen)
        self.WordLen=int(WordLen)
            
    def __del__(self):
        self.wait()

    def Setup(self):
        self.refresh=QtGui.QApplication.processEvents
        self.stopped=False
        self.err_sig=""
        algos={"md5":32,"sha1":40,"sha224":56,"sha256":64,"sha384":96,"sha512":128}
        hashing_functions={"md5":hashlib.md5,"sha1":hashlib.sha1,"sha224":hashlib.sha224,"sha256":hashlib.sha256,"sha384":hashlib.sha384,"sha512":hashlib.sha512}
        try:
            assert len(self.hash)==algos[self.htype]
            self.mk_hash=hashing_functions[self.htype]
        except:
            self.err_sig="Stopped: this hash is NOT of type: "+self.htype
            return 0
        return 1

    def run(self):
        if not self.Setup():
            self.stopped=True
            self.emit(QtCore.SIGNAL('Important(const QString)'),"Something went wrong.\nCheck your hash")
        numb=range(48,58)
        cap=range(65,91)
        low=range(97,123)
        dig=range(33,65)
        #other=range(90,97)+range(122,128)
        count=l=signal=0
        bigList=[]
        MIN=self.min_WordLen
        if self.WordLen:
            MAX=self.WordLen
        else:
            MAX=10
        if MAX==MIN or MAX<MIN:
            MIN=2
            MAX=10
            self.emit(QtCore.SIGNAL('Important(const QString)'), "WARNING: invalid minimum/maximum word length!")
        poss=low+cap+numb+dig
        for i in poss:
            bigList.append(str(chr(i)))
        HOW_OFTEN_CHECK=250000
        if not self.hash:
            self.emit(QtCore.SIGNAL('Important(const QString)'), "Stopped: no hash")
            self.stopped=True
        
        START_TIME=time.time()
        self.emit(QtCore.SIGNAL('Important(const QString)'), "Starting bruteforce...\nHashing algorythm: "+self.htype.upper()+"\nMin word length: "+str(MIN)+"  Max word length: "+str(MAX))
        time.sleep(2)
        self.refresh()
        try:
            for i in xrange(MIN,MAX):
                for s in product(bigList,repeat=i):
                    if self.stopped==True or Data.RES==True:
                        raise BruteStoppedEx("stopped")
                    count+=1
                    l+=1
                    if self.mk_hash("".join(s)).hexdigest()==self.hash:
                        elapsed=time.time()-START_TIME
                        speed=int(l/elapsed)
                        tests="PASSWORD FOUND: "+"".join(s)+"\n"+"{:,}".format(speed)+" combinations/sec"+"\nDone in "+str(int(elapsed))+" seconds"

                        self.emit(QtCore.SIGNAL('Important(const QString)'), tests)
                        signal='done'
                        self.refresh()
                        raise BruteStoppedEx("done")

                    if count>=HOW_OFTEN_CHECK:
                        count=0
                        elapsed=time.time()-START_TIME
                        speed=int(l/elapsed)
                        res="{:,}".format(l)+" words generated. Current: "+"".join(s)+"\nSpeed: "+"{:,}".format(speed)+" combinations/sec"+"\nTime spent: "+str(round(elapsed/60,1))+" min. "+"Word length: "+str(i)
                        self.emit(QtCore.SIGNAL('test(const QString)'), res)
                        time.sleep(0.002)
            self.emit(QtCore.SIGNAL('Important(const QString)'), "All combinations tested.\nPassword NOT found!")
            raise BruteStoppedEx("endOfDict")
        except:
            if not signal:
                self.emit(QtCore.SIGNAL('Important(const QString)'), "Stopped")
                Data.RES=True
            if "hash is NOT" in self.err_sig:
                self.emit(QtCore.SIGNAL('Important(const QString)'), self.err_sig)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=gui()
    myapp.show()
    sys.exit(app.exec_())
