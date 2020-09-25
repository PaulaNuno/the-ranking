from src.app import app
import controllers.student_controllers
import controllers.lab_controllers
from config import PORT


PORT=3000
app.run("0.0.0.0", PORT, debug=True)