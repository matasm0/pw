# The program for encrypting/decrypting files for all of my programs that need it.

from cryptography.fernet import Fernet
from os.path import normpath
from os import sep
import pyperclip

# For now, we are going to be reading the entire contents of a file into memory. This...
# is not ideal. I am not able or willing to fully learn a good streaming encryption method,
# and thus for now we will ignore it. In the future tho, either look into using Fernet with
# blocks (ie we split the file into blocks and append/read by block into/from a file) or
# look into like AES-GCM/AES-NI or XChaCha20-Poly1305 https://soatok.blog/2020/05/13/why-aes-gcm-sucks/

# We put the original extension of the file at the start of the file itself, separated from the rest
# of the contents by... this. Yea sure I could've just used a newline but that's... too intelligent.
extSeparator = "bananasplit"

# Encrypts the given file with the given key. Key must be a Fernet compatible
# base-64 32 byte key. 
# Can take in either a file path or the contents of the file. If both are given, the contents are used.
# Can take an output path or return the encrypted contents.
# A filetype can be provided (if say only contents are provided), but not required.
# If hideOutputFileType is True, the encrypted file will have the ".enc" extension.
def encryptFile(key, inPath = None, outPath = None, contents = None, fileType = None, hideOutputFileType = True, returnFile = False):
    if not contents and not inPath: raise Exception("No data to encrypt")
    if fileType and fileType[0] == ".": fileType = fileType[1:]
    if contents:
        if type(contents) is not bytes:
            contents = contents.encode()
    if not contents:
        with open(inPath, 'rb') as f:
            contents = f.read()

    if not fileType:
        fileType = ""
        if inPath:
            temp = inPath.split(".")
            if len(temp) != 1:
                fileType = temp[-1]
    
    contents = fileType.encode() + extSeparator.encode() + contents
    e = Fernet(key)
    eData = e.encrypt(contents)
    if outPath:
        outPath = normpath(outPath)
        if hideOutputFileType:
            if len(newPath := outPath.split(".")) > 1:
                newPath[-1] = "enc"
            else:
                newPath.append("enc")
            outPath = ".".join(newPath)
        with open(outPath, 'wb') as f:
            f.write(eData)
        
    if returnFile:
        return eData

# Returns a tuple containing the (contents, fileType). Contents are returned as bytes
def decryptFile(key, inPath = None, outPath = None, contents = None, fileType = None, returnFile = False):
    if not inPath and not contents: raise Exception("No data to decrypt")
    if fileType and fileType[0] == ".": fileType = fileType[1:]
    if not contents:
        with open(inPath, 'rb') as f:
            contents = f.read()
    if len(contents) == 0:
        return (contents, "")

    d = Fernet(key)
    dData = d.decrypt(contents)

    # Find the splitter
    l, r = 0, len(extSeparator)
    while dData[l:r] != extSeparator.encode():
        l += 1
        r += 1
        if l == 10: break
    else:
        if not fileType and l > 0:
            fileType = dData[:l].decode()
        dData = dData[r:]    

    if outPath:
        if fileType and len(outPath.split('.')) == 1:
            outPath += "." + fileType
        outPath = normpath(outPath)
        with open(outPath, "wb") as f:
            f.write(dData)

    # User may not know fileType of file they put in. Give it to them if we have it.
    if returnFile: return (dData, fileType)


# Take an encrypted file and unencrypt then reencrypt with a different key
def reEncrypt(oldKey, newKey, inPath = None, outPath = None, contents = None, returnFile = False):
    dData = decryptFile(oldKey, inPath, outPath, contents, returnFile = True)
    eData = encryptFile(newKey, contents=dData[0], fileType=dData[1], returnFile=True)

    if outPath:
        outPath = normpath(outPath)
        # if outPath.split(".")[-1] not in ["e", "enc", "encrypted"]: outPath += ".enc"
        with open(outPath, 'wb') as f:
            f.write(eData)
        
    if returnFile:
        return eData

# Debugging
def generateKey():
    key = Fernet.generate_key().decode()
    pyperclip.copy(key)
    return key