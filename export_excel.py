#!/usr/bin/env python3

import os
import pandas as pd


def dict_to_excel(dict_data, excel_path):
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dict_data.items()]))
    df.to_excel(excel_path, index=False)


def find_python_java_files(directory):
    files_dict = {"python": [], "java": []}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                files_dict["python"].append(os.path.join(root, file))
            elif file.endswith(".java"):
                files_dict["java"].append(os.path.join(root, file))

    return files_dict


def read_folders_in_leetcode():
    leetcode_path = "LeetCode"
    dict = {"Title": [], "file_path": []}

    if not os.path.exists(leetcode_path):
        print("LeetCode directory does not exist.")
        return

    # 遍历LeetCode目录
    for item in os.listdir(leetcode_path):
        item_path = os.path.join(leetcode_path, item)
        # 如果是目录，并且名称以数字开头，则打印
        if os.path.isdir(item_path) and item[0].isdigit():
            dict["Title"].append(item)
            dict["file_path"].append(find_python_java_files(item_path))

    return dict


def dict_to_markdown_link(files_dict):
    markdown_links = ""
    for key, values in files_dict.items():
        if values:  # Check if the list under the key is not empty
            # Create a Markdown link using the first file path
            link = f"[{key.capitalize()}]({values[0]})"
            if len(markdown_links) > 0:
                markdown_links += (" " + link)
            else:
                markdown_links += link

    return markdown_links


def tweak_dict_fit_markdown_format(dict):
    # for example:
    # [Python](LeetCode/167.Two_Sum_II_-_Input_Array_Is_Sorted/Mario/167.Two_Sum_II_-_Input_Array_Is_Sorted.py)
    dict["Solution"] = []
    for item in dict["file_path"]:
        dict["Solution"].append(dict_to_markdown_link(item))
    return dict


files_dict = read_folders_in_leetcode()
md_dict = tweak_dict_fit_markdown_format(files_dict)
excel_path = "LeetCodeFiles.xlsx"
dict_to_excel(md_dict, excel_path)
print(f"Excel file created at {excel_path}")
