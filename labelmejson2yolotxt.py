import os
import sys
import argparse
import json


def json2txt(workingdirectory, class_list):
    json_files = [pos_json for pos_json in os.listdir(workingdirectory) if pos_json.endswith('.json')]
    for i in range (len(json_files)):

        with open(os.path.join(workingdirectory, json_files[i])) as f:
            data = json.load(f)
        width = data["imageWidth"]
        height = data["imageHeight"]
        shapes = data["shapes"]
        text_file_name = workingdirectory+"/"+json_files[i]
        text_file_name = text_file_name.replace("json","txt")
        text_file = open(text_file_name, 'w')
        for i in range (len(shapes)):
            class_name = shapes[i]["label"]
            class_id = class_list.index(str(class_name))
            points = data["shapes"][i]["points"]
            normalize_point_list = []
            normalize_point_list.append(class_id)
            for i in range (len(points)):
                normalize_x = points[i][0]/width
                normalize_y = points[i][1]/height
                normalize_point_list.append(normalize_x)
                normalize_point_list.append(normalize_y)
            for i in range (len(normalize_point_list)):
                text_file.write(str(normalize_point_list[i])+" ")
            text_file.write("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "json to yolo")
    parser.add_argument("-W", "--workingdir", metavar="directory", required=True, type=str, default=None, help="Please provide the file path to work on.")
    parser.add_argument("-C", "--classes", metavar="A,B,C...", required=True, type=lambda x:x.split(","), default=None, help="The classes of the created files are needed.")
    args = parser.parse_args(sys.argv[1:])
    json2txt(args.workingdir, args.classes)
    

