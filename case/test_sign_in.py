import os
import sys
import time
from pathlib import Path

import pytest
import requests

from middleware.yml import read_yaml

current_file = Path(__file__).resolve().parent
project_dir = os.path.dirname(current_file)

user_db = dict(read_yaml(project_dir + '/api/sign_in.yaml'))
user_list = [tuple(i) for i in user_db['data']]


@pytest.mark.parametrize('users', user_list)
def test_sign_in(users):
    time.sleep(1)  # 为了直观的看到多进程执行用例的效果，因此让每条用例执行前都等待 1 s
    if users[0] == {}:
        r = requests.post(user_db.get('url'), json=users[0])
        assert r.json()['code'] == users[1]
        assert r.json()['msg'] == users[2]
    else:
        r = requests.post(user_db.get('url'), json=users[0])
        assert r.json()['code'] == users[1]
        assert r.json()['msg'] == users[2]
        if r.json()['code'] == 20000:
            print('got token: ', r.json()['data']['token'])
