import zipfile
import subprocess
from os.path import exists
import os

def IS_PROTOC_INSTALLED():
    try:
        bashCommand = f"protoc"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    except:
        return False
    
    return True

def install():

    # if IS_PROTOC_INSTALLED(): 
    #     print("'protoc' is already installed, yay!")
    #     return

    # assert exists("protobuf.zip"), """protobuf.zip MISSING!!!"""
    # assert os.name == "posix", """Not on unix, will not run!!!"""

    '''below is deprecated, zip is too large for github'''
    # print("  [-] *** Unzipping protobuf.zip ***")
    # print("  [-] This will take awhile, please wait...")
    # zip = zipfile.ZipFile("protobuf.zip")
    # zip.extractall()
    # print("  [-] done.")

    bashCommand = '''
        sudo apt-get install autoconf automake libtool curl make g++ unzip;  # get all unix requirements
        # git clone https://github.com/protocolbuffers/protobuf.git;         # old and deprecated
        cd protobuf;                                               # move into "protobuf" installation folder
        git submodule update --init --recursive;                             # update modules
        ./autogen.sh;                                                        # Run installation cript from google
        ./configure;                                                         # ...
        make -j$(nproc) ;                                                    # $(nproc) ensures it uses all cores for compilation
        make check;                                                          # validate files
        sudo make install;                                                   # protobuf installed here
        sudo ldconfig ;                                                      # refresh shared library cache.
        cd ..;                                                               # cd back into outer directory (project directory)                                                              # ...
        '''
    # process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    # output, error = process.communicate()

    process = subprocess.Popen(
        bashCommand,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        encoding='utf-8',
        errors='replace'
    )

    while True:
        realtime_output = process.stdout.readline()

        if realtime_output == '' and process.poll() is not None:
            break

        if realtime_output:
            print(realtime_output.strip(), flush=True)



