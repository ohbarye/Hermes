# Hermes
Mask sensitive data with dummy.

# Usage

## Install

First, `git clone` and `pip install`.

```bash
$ git clone https://github.com/ohbarye/Hermes
$ cd Hermes
$ pip install git+https://github.com/joke2k/faker.git # The latest faker is not released PyPI
```

## Mask data

To mask data, prepare 2 files.

1. **in.csv**

    It's CSV data to mask. Any name is OK, but don't forget edit `env.py`'s `in_file`.

    ```csv
    id,name,age,hire_date,phone_number,address,e-mail
    1,Tormas,25,1977/9/21,09-0000-0002,Ireland,tormas@te.te
    2,Yonaus,3,1990/2/26,039-0000-0002,神奈川県,yonaus@te.te
    3,Hermes,44,1982/5/21,092-0000-0002,東京,hermes@te.te
    ```

1. **rules.json**

    The rules how to mask data. It's written in JSON. The `Key` means *column number* (it starts from 0), and the `value` does *data type*.

    ```json
    {
        "1": "name",
        "2": "age",
        "3": "date",
        "4": "phone_number",
        "5": "address",
        "6": "email"
    }
    ```

The above sample generates the following result: `out.csv`.

```csv
id,name,age,hire_date,phone_number,address,e-mail
1,杉山 和也,99,2004-10-04,73-7004-3804,青森県日野市独鈷沢15丁目2番6号 パーク九段南823,sequiy@example.org
2,山田 裕美子,54,1988-12-08,48-8365-9175,長崎県西多摩郡檜原村細竹15丁目25番16号 ハイツ日光446,qui84@example.com
3,宇野 香織,22,1973-03-09,30-8595-4194,愛知県北区三ノ輪22丁目6番15号 前弥六パーク361,veroy@example.net

```

## Extend

* If you want to mask data by other location style.Edit `env.py`'s `location`. e.g. `en_US`: English(United States), `it_IT`: Italian, and so on.

* If there is no header row in `in.csv`, then edit `env.py`'s `skip_header` to `False`.

* This tool depends heavily on **faker** for data generation. For more information, refer to https://github.com/joke2k/faker.

# License

MIT


## TODO

* generate frees style dummy data
* skip any row
