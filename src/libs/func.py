import libs
import libs.init
import libs.init.init

import libs.form

import libs.payload
import libs.payload.init


data = libs.init.init.exec()


def exec() -> str:
    return libs.payload.init.exec(data)
