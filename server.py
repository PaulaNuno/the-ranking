from src.app import app
import controllers.studentcontrollers
import controllers.labcontrollers
from config import PORT


PORT=3000
app.run("0.0.0.0", PORT, debug=True)