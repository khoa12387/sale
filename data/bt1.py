import json


def read_data():
    with open("data/products.json", "r", encoding="utf-8") as f:
        return json.loads(f)


def output(data):
    for x in data:
        for k, v in x.items():
            if k == 'ma_nv':
                print(f"Ma nhan vien: {v}")
            if k == 'ten_nv':
                print(f"Ten nhan vien: {v}")


def add(id, name):
    data = read_data()
    nv = {
        "ma_nv": id,
        "ten_nv": name
    }
    data.append(nv)
    with open("data/products.json","w") as f:
        json.dump(data,f)


if __name__ == '__main__':
    data = read_data()
    output(data)