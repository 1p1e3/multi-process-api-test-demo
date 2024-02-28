from typing import Any
import yaml


# 读取 yaml 文件中的数据
def read_yaml(file_path: str) -> Any:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, yaml.FullLoader)
    return data


# 将数据写入 yaml 文件
def write_yaml(file_path: str, data: dict):
    with open(file_path, 'a') as f:
        yaml.dump(data, f)
