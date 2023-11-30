import time

from transformers import AutoProcessor, BarkModel
import scipy
# from TTS.tts.configs.bark_config import BarkConfig
# from TTS.tts.models.bark import Bark
from scipy.io.wavfile import write as write_wav

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
# config = BarkConfig()
# model = Bark.init_from_config(config)
# model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)
# model.to("cuda")
# text = "Please subscribe to my channel"
#
# output_dict = model.synthesize(
#     text,
#     config,
#     speaker_id="speaker",
#     voice_dirs="bark_voices",
#     temperature=0.95
# )

# write_wav("output.wav", 24000, output_dict["wav"])



def generate_audio(text, preset, output):
    inputs = processor(text, voice_preset=preset)
    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()
    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)

curr = time.time()
print(curr)

voice_preset = "v2/hi_speaker_6"
text = " हेलो दोस्तों, यदि आपके पास पूरी किताब पढ़ने का समय नहीं है, तो आप Free Book Summary in Hindi को पढ़ सकते हैं| आप यहां पर 10 मिनट में पूरी बुक का नॉलेज ले सकते हैं| ये Hindi Book Summary वास्तव में सरल शब्दों में हैं ताकि आपको पुस्तक के प्रमुख सिद्धांतों को जल्द से जल्द समझने में कोई समस्या न हो। हमने Book Summary के साथ-साथ उसकी Review भी की है, जिससे आपको किताब के बारे में जानने और यह स्पष्ट करने में मदद मिलेगी कि आप उस किताब को खरीदना चाहते हैं या नहीं।"
output = 'output/sample.wav'

generate_audio(text, voice_preset, output)

print(time.time() - curr)






