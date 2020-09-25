from src.app import app
import src.controllers.studentcontrollers
import src.controllers.labcontrollers
from src.config import PORT



app.run("0.0.0.0", PORT, debug=True)