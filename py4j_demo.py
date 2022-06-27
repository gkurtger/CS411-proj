from py4j.java_gateway import JavaGateway
import subprocess
from time import sleep

p = subprocess.Popen(["java", "-cp", "./py4j.jar", "backend_JVM.java"])


#subprocess.run(["java", "-cp", "./py4j.jar", "AdditionApplication.java"])

gateway = JavaGateway()
backend = gateway.entry_point
print(backend.test(1, 2))



p.terminate()
p.kill()