from flask import Flask;
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.salad_spree
import codeitsuisse.routes.secrete_message
import codeitsuisse.routes.contract
import codeitsuisse.routes.inventory
import codeitsuisse.routes.clean
import codeitsuisse.routes.geometry