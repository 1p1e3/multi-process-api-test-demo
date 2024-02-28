from typing import Any
from flask import jsonify, Response


# 响应 json 模板
def res_data(code: int, msg: str, data: Any) -> Response:
    return jsonify(
        {
            'code': code,
            'msg': msg,
            'data': data
        }
    )