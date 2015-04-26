from dummy_generator import DummyGenerator
import env

def main():

    dg = DummyGenerator(env.rules)

    masked_data = dg.mask(env.in_file)

    dg.write_csv(env.out_file,masked_data)

if __name__ == "__main__":
    main()
