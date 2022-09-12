from enum import auto
import imp
from flask import Blueprint #import Blueprint class

#create a Blueprint object called auth and pass it the name of the Blueprint, the name of the module, 
#and the url_prefix to be used for all the routes defined in the Blueprint object (auth) 

auth = Blueprint('auth', __name__, url_prefix='/auth') 

from . import views #import views module from the auth package (app\auth\) 