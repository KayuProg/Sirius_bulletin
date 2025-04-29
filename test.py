import subprocess
import re

two_step_authentication = ['oathtool', '--totp', '--base32', 'HHDMVM54HSTMAJQB']
SecondLoginPass = re.findall(r'\d+', subprocess.check_output(two_step_authentication).decode('utf-8'))
print(SecondLoginPass[0])