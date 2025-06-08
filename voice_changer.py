from pydub import AudioSegment
from pydub.effects import speedup, pitch_shift
import os

class VoiceChanger:
    def change_voice(self, audio_path, output_path="output_changed.wav"):
        sound = AudioSegment.from_file(audio_path)
        # مثال: تغییر سرعت و پچ صدا
        faster = speedup(sound, playback_speed=1.2)
        shifted = faster._spawn(faster.raw_data, overrides={
            "frame_rate": int(faster.frame_rate * 1.1)
        }).set_frame_rate(faster.frame_rate)
        shifted.export(output_path, format="wav")
        return output_path
