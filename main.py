import atexit
import logging
import requests


class Init:
    @staticmethod
    def __logging() -> None:
        logging.basicConfig(
            format='[%(asctime)s] [%(levelname)-8s] %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __greet() -> None:
        logging.info('hi')

    @staticmethod
    def __exit() -> None:
        atexit.register(lambda: logging.info('hi'))

    @staticmethod
    def exec() -> None:
        Init.__logging()
        Init.__greet()
        Init.__exit()


def main() -> None:
    Init.exec()


if __name__ == '__main__':
    main()
