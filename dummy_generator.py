import env
import csv
import json
import random
from faker import Factory

class DummyGenerator(object):

    def set_rules(self,rules):

        with open(rules,'rb') as f:
            jsondata = f.read()
            self.rules = json.loads(jsondata)

    def mask_row(self,row):

        for key,value in self.rules.iteritems():
            fakedata = self.create_fakedata(value)
            row[int(key)] = fakedata

        return row

    def create_fakedata(self,data_type):

        if data_type == "name":
            return self.fake.name().encode('utf-8')
        elif data_type == "date":
            return self.fake.date()
        elif data_type == "age":
            return self.fake.random_number(random.choice([1,2,2,2,2,2,2]))
        elif data_type == "phone_number":
            return self.fake.phone_number()
        elif data_type == "address":
            return self.fake.address().encode('utf-8')
        elif data_type == "email":
            return self.fake.word() + self.fake.safe_email()

    def mask(self,target_to_mask):

        with open(target_to_mask,'rb') as f:
            in_data  = csv.reader(f)

            out_data = []

            if env.skip_header:
                out_data.append(in_data.next())

            out_data.extend([self.mask_row(row) for row in in_data])

            return out_data

    def write_csv(self,file_name,data):

        with open(file_name, 'w') as f:
            csv.writer(f).writerows(data)

    def __init__(self,rules=""):

        self.fake = Factory.create(env.location)

        if rules != "":
            self.set_rules(rules)
