# Hermes
Generate dummy data, or mask sensitive data with dummy.

# Usage

## Install

Clone and install with pip.

```bash
$ git clone https://github.com/ohbarye/Hermes
$ cd Hermes
$ pip install -r packages_requirements.txt
```

## Mask data

To mask data, prepare 2 files.

1. **in.csv**

    CSV data to mask. Any name is OK, but don't forget arrange `env.py`'s `in_file`.

    ```csv
    id,name,age,hire_date,phone_number,address,e-mail
    1,Tormas,25,1977/9/21,09-0000-0002,Ireland,tormas@te.te
    2,Yonaus,3,1990/2/26,039-0000-0002,神奈川県,yonaus@te.te
    3,Hermes,44,1982/5/21,092-0000-0002,東京,hermes@te.te
    ```

1. **rules.json**

    The rules how to mask data. It's written in JSON.

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

The above sample generate the following result: `out.csv`.

```csv
id,name,age,hire_date,phone_number,address,e-mail
1,渡辺 明美,19,1985-11-08,070-5797-2830,53 西之園 Street 21741 香織 Ville,animix@example.org
2,中島 裕樹,2,2015-04-09,090-3448-3624,07 山田 Street 73882 裕美子 Ville,ea.@example.net
3,石田 充,92,1995-01-15,090-5354-4606,78 大垣 Street 85516 さゆり Ville,rerum.@example.org

```

## Extend

If you want to mask data by other location style.Arrange `env.py`'s `lacation` property.

# License

MIT


## TODO

* format address
* generate frees style dummy data
