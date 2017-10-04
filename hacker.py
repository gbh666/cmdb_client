#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/10/2

import requests

response = requests.get('http://127.0.0.1:8000/api/test.html',
                        headers={'auth-api': "b61ce38c864e94cb24f9952e61726f03|1506925641.902956"})
print(response.text)
