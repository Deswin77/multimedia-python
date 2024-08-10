from PIL import Image

# Memuat gambar
image = Image.open('google.jpg')

# Menyimpan gambar
image.save('result.jpg')

#crop
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

#size
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

#filter
from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')


from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('audio1.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

#pemotongan
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')


#penggabungan
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

#konversi format
audio.export('result.wav', format='wav')


#Pengaturan Volume

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')
