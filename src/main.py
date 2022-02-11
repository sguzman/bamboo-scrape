import libs
import libs.init
import libs.init.init

import libs.form

import libs.payload
import libs.payload.init


data = libs.init.init.exec()
out = libs.payload.init.exec(data)


def main() -> None:
    print(out)


if __name__ == '__main__':
    main()
