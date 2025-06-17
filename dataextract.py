import os
import shutil

# ✅ Use raw strings or forward slashes
source_dirs = [
    r'brain stroke/dataset/Dataset_MRI_Folder',
    r'brain stroke/dataset/Stroke_classification_dataset',
    r'brain stroke/dataset/Normal _ Stroke Patient Details'
]

# Target base directory
target_base = 'final_dataset/'
os.makedirs(target_base, exist_ok=True)

# Classes to extract
classes = ['Normal', 'Ischemic', 'Haemorrhagic']

# File counter
counter = 0

for src_dir in source_dirs:
    for class_name in classes:
        for root, dirs, files in os.walk(os.path.join(src_dir)):
            if class_name.lower() in root.lower():
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        src_path = os.path.join(root, file)
                        dst_dir = os.path.join(target_base, class_name)
                        os.makedirs(dst_dir, exist_ok=True)
                        dst_path = os.path.join(dst_dir, f"{class_name}_{counter}.png")
                        shutil.copyfile(src_path, dst_path)
                        counter += 1

print(f"✅ Done! {counter} images copied to 'final_dataset/' folder.")
