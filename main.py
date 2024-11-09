import json
import os
import shutil
def convertJsonToYoloFormat(json_file, json_dir, img_dir, output_label_dir, output_image_dir):
    json_path = os.path.join(json_dir, json_file)
    print(f"Loading JSON: {json_path}")
    with open(json_path) as f:
        data = json.load(f)

    img_width = data['size']['width']
    img_height = data['size']['height']

    yolo_data = []

    for obj in data['objects']:

        class_title = obj['classTitle']
        class_id = class_title_to_id.get(class_title)
        if class_id is None:
            print(f"Unknown class: {class_title}")
            continue

        x_min, y_min = obj['points']['exterior'][0]
        x_max, y_max = obj['points']['exterior'][1]

        x_center = ((x_min + x_max) / 2) / img_width
        y_center = ((y_min + y_max) / 2) / img_height
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        yolo_data.append(f"{class_id} {x_center} {y_center} {width} {height}")

    label_output_file = os.path.join(output_label_dir, os.path.splitext(json_file)[0] + ".txt").replace('.png', '')
    with open(label_output_file, 'w') as out_f:
        out_f.write("\n".join(yolo_data))

    image_file_base = os.path.splitext(json_file)[0]
    image_file = image_file_base

    src_image_path = os.path.join(img_dir, image_file)
    print(f"Checking path: {src_image_path}")  # Debugging case
    if os.path.exists(src_image_path):
        print(f"Image founded: {src_image_path}")
        dst_image_path = os.path.join(output_image_dir, image_file)
        shutil.copyfile(src_image_path, dst_image_path)
    else:
        print(f"No image for JSON file: {json_file}")

class_title_to_id = {
    'orange_cone': 0,
    'large_orange_cone': 1,
    'blue_cone': 2,
    'yellow_cone': 3
}
def processAllJsons(json_dir, img_dir, output_label_dir, output_image_dir):
    os.makedirs(output_label_dir, exist_ok=True)
    os.makedirs(output_image_dir, exist_ok=True)

    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            convertJsonToYoloFormat(json_file, json_dir, img_dir, output_label_dir, output_image_dir)


# PATHS
json_dir = r'/home/szewczyk/Desktop/dataset/ann'  # JSON files dir
img_dir = r'/home/szewczyk/Desktop/dataset/img'  # Image files dir
output_label_dir = r'/home/szewczyk/Desktop/Yolo/labels'  # Target dir for YOLO labels
output_image_dir = r'/home/szewczyk/Desktop/Yolo/out_img'  # Target dir for image labels

processAllJsons(json_dir, img_dir, output_label_dir, output_image_dir)
