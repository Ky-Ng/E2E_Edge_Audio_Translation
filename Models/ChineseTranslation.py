# # Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("translation_zh_to_en", model="google-t5/t5-small")

# translation = pipe("我是你的好朋友")
# print(translation)

# Use a pipeline as a high-level helper
from transformers import pipeline
from transformers import AutoModel

pipe_zh_en = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
pipe_en_zh = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")

to_translate = "already in english"
if not to_translate.isascii():
    translation = pipe_zh_en(to_translate)
    
else:
    # print(f"the string, {to_translate}, is already in english")
    translation = pipe_en_zh(to_translate)
print(translation)
model = AutoModel.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
print(f"Chinese to English model has {model.num_parameters()} parameters")

model2 = AutoModel.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
print(f"English to Chinese model has {model2.num_parameters()} parameters")