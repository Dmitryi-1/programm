import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename='stderr.txt',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
