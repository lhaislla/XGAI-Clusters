from Models import DefaultConfig


if __name__ == "__main__":
    config = DefaultConfig()
    print(config.result_dataframe.head())
