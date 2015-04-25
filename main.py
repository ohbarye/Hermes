from dummy_generator import DummyGenerator

def main():

    rules    = "test_data/rules.json"
    in_file  = "test_data/in.csv"
    out_file = "test_data/out.csv"

    dummy = DummyGenerator(rules)

    replaced_data = dummy.mask(in_file)

    dummy.write_csv(out_file,replaced_data)

if __name__ == "__main__":
    main()
