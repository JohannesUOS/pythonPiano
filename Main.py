#General first test
import simpleaudio as sa

#import file as wave object
wave_obj = sa.WaveObject.from_wave_file("piano_samples/1A.wav")

#starting playback
play_obj = wave_obj.play()

#waiting for the playback to finish before exiting script
play_obj.wait_done()

print("FINISHED PLAYBACK")

