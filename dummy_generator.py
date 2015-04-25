import csv
import json
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

    def mask(self,target_to_mask):

        with open(target_to_mask,'rb') as f:
            in_data  = csv.reader(f)
            return [self.mask_row(row) for row in in_data]

    def write_csv(self,file_name,data):

        with open(file_name, 'w') as f:
            csv.writer(f).writerows(data)

    def __init__(self,rules=""):

        self.fake = Factory.create('ja_JP')

        if rules != "":
            self.set_rules(rules)
