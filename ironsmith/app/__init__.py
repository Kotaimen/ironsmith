# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '9/17/15'

from flask import Flask

import ironsmith

app = Flask(__name__)


class Application(Flask):
    def __init__(self):
        Flask.__init__(self, __name__)

        self.add_url_rule(
            rule='/',
            view_func=self.hello_world,
            methods=['GET']
        )

        self.add_url_rule(
            rule='/health_check',
            view_func=self.health_check,
            methods=['GET']
        )


    def hello_world(self):
        return 'Hello, world'

    def health_check(self):
        return '',200



