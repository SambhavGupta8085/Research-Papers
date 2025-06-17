import os
import shutil
import random

def split_dataset(base_dir, output_dir, split_ratio=0.8):
    classes = os.listdir(base_dir)

    for cls in classes:
        cls_path = os.path.join(base_dir, cls)
        if not os.path.isdir(cls_path):
            continue
        
        images = os.listdir(cls_path)
        random.shuffle(images)
        
        train_count = int(len(images) * split_ratio)

        train_dir = os.path.join(output_dir, 'train', cls)
        val_dir = os.path.join(output_dir, 'val', cls)
        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(val_dir, exist_ok=True)

        for i, img in enumerate(images):
            src_path = os.path.join(cls_path, img)
            if i < train_count:
                dst_path = os.path.join(train_dir, img)
            else:
                dst_path = os.path.join(val_dir, img)
            shutil.copy(src_path, dst_path)

    print("✅ Dataset split completed!")

# Usage
split_dataset(
    base_dir="C:/Users/asus/Desktop/ResearchPaper for USA/final_dataset",
    output_dir="C:/Users/asus/Desktop/ResearchPaper for USA/final_dataset_split",
    split_ratio=0.8
)
