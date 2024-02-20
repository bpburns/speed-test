import json

json_sample = '''
{
    "type": "result",
    "timestamp": "2024-02-19T18:30:25Z",
    "ping": {
        "jitter": 1.685,
        "latency": 27.4,
        "low": 26.173,
        "high": 28.584
    },
    "download": {
        "bandwidth": 36571648,
        "bytes": 307512108,
        "elapsed": 8501,
        "latency": {
            "iqm": 57.446,
            "low": 26.25,
            "high": 353.744,
            "jitter": 15.17
        }
    },
    "upload": {
        "bandwidth": 36961218,
        "bytes": 336123482,
        "elapsed": 9208,
        "latency": {
            "iqm": 35.49,
            "low": 25.942,
            "high": 55.847,
            "jitter": 1.809
        }
    },
    "packetLoss": 1.7647058823529411,
    "isp": "Hyper Fusion",
    "interface": {
        "internalIp": "redacted",
        "name": "eno1",
        "macAddr": "redacted",
        "isVpn": false,
        "externalIp": "redacted"
    },
    "server": {
        "id": 58493,
        "host": "redacted",
        "port": 8080,
        "name": "redacted",
        "location": "redacted",
        "country": "redacted",
        "ip": "redacted"
    },
    "result": {
        "id": "redacted",
        "url": "https://www.speedtest.net/result/c/redacted",
        "persisted": true
    }
}
'''

parsed_json = json.loads(json_sample)

def unnest_dict(prefix, dictionary):
    results = {}
    if prefix is None:
        prefix = '$'
    for k, v in dictionary.items():
        if isinstance(v, dict):
            results.update(unnest_dict(prefix + '.' + k, v))
        else:
            results[prefix + '.' + k] = v
    return results

result_set = unnest_dict(None, parsed_json)

for k in sorted(result_set.keys()):
    v = result_set[k]
    v_type = type(v)
    TEMPLATE = f'''JSON_EXTRACT(result_json, '{k}')'''
    if v_type == str:
        TEMPLATE = f'''JSON_UNQUOTE({TEMPLATE})'''
    TEMPLATE = f"{TEMPLATE} AS '{k[2:]}',"
    print(TEMPLATE)

#for k, v in parsed_json.items():
#    if isinstance(v, dict):
#        for k2, v2 in v.items():
#            print(k + '.' + k2 + ':', v2)
#    else:
#        print(k + ':', v)
