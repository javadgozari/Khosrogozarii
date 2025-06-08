from pydub import AudioSegment
import os

class VoiceChanger:
    def change_voice(self, input_path, output_path="changed_voice.wav"):
        try:
            sound = AudioSegment.from_file(input_path)
            
            # تغییر pitch و سرعت
            changed = sound._spawn(sound.raw_data, overrides={
                "frame_rate": int(sound.frame_rate * 1.3)
            }).set_frame_rate(sound.frame_rate)
            
            changed.export(output_path, format="wav")
            return output_path
        except Exception as e:
            return f"❌ خطا در تغییر صدا: {str(e)}"
