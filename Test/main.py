import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import pyaudio
import wave
import os

NUMFRAMES = 1024

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORDSECONDS = 10

#plays every file in dirName
def playDirectory(dirName, pie, index):
    dirlist = os.listdir(dirName)
    for f in dirlist:
        inFileName = ('%s/%s' % (dirName, f))
        waveFile = wave.open(inFileName, 'r')
        chip = pie.open(rate = waveFile.getframerate(),
                          channels = waveFile.getnchannels(),
                          format = pie.get_format_from_width(waveFile.getsampwidth()),
                          output = True,
                          output_device_index = index)
        frames = waveFile.readframes(NUMFRAMES)
        while(len(frames) > 0):
            chip.write(frames)
            frames = waveFile.readframes(NUMFRAMES)
        waveFile.close()
    chip.stop_stream()
    chip.close()

def record(name, pie, index):
    chip = pie.open(rate = RATE,
                    channels = CHANNELS,
                    format = FORMAT,
                    input = True,
                    frames_per_buffer = NUMFRAMES,
                    input_device_index = index)
    song = []
    print('recording')
    for i in (range(0, int(RATE/NUMFRAMES * RECORDSECONDS))):
        frames = chip.read(NUMFRAMES)
        song.append(frames)
    print('done recording')
    fileDes = os.open(name, os.O_CREAT)
    waveFile = wave.open(name, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(pie.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(song))
    os.close(fileDes)

#  
# def getIndex(device, pie):
#     info = pie.get_host_api_info_by_index(0)
#     n = pie.get_device_count
#     for i in range(0, n):
#         if pie.get_device_info_by_host_api_device_index(0, i).get('name') = 
    
    
               
#main
pie = pyaudio.PyAudio()
#playDirectory('waves', pie, 2)

record("recordings/new.wav", pie, 2)
playDirectory('recordings', pie, 2)

