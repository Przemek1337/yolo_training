import os
import shutil
import random

# Ścieżki
img_dir = r'C:\Users\przem\Desktop\tuto_dataset\out_img'  # Katalog z obrazami
label_dir = r'C:\Users\przem\Desktop\tuto_dataset\labels'  # Katalog z etykietami
train_img_dir = r'C:\Users\przem\Desktop\tuto_dataset\img_train'
val_img_dir = r'C:\Users\przem\Desktop\tuto_dataset\img_val'
train_label_dir = r'C:\Users\przem\Desktop\tuto_dataset\labels_train'
val_label_dir = r'C:\Users\przem\Desktop\tuto_dataset\labels_val'

# Tworzenie katalogów wyjściowych
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Lista wszystkich obrazów i ich etykiet
images = os.listdir(img_dir)
random.shuffle(images)

# Ustaw proporcje (np. 80% dla treningu, 20% dla walidacji)
split_ratio = 0.8
split_index = int(len(images) * split_ratio)

# Podziel dane na treningowe i walidacyjne
train_images = images[:split_index]
val_images = images[split_index:]

# Kopiowanie obrazów i etykiet do odpowiednich katalogów
for img in train_images:
    img_path = os.path.join(img_dir, img)
    label_path = os.path.join(label_dir, os.path.splitext(img)[0] + '.png.txt')
    shutil.copy(img_path, os.path.join(train_img_dir, img))
    shutil.copy(label_path, os.path.join(train_label_dir, os.path.basename(label_path)))

for img in val_images:
    img_path = os.path.join(img_dir, img)
    label_path = os.path.join(label_dir, os.path.splitext(img)[0] + '.png.txt')
    shutil.copy(img_path, os.path.join(val_img_dir, img))
    shutil.copy(label_path, os.path.join(val_label_dir, os.path.basename(label_path)))
