from datetime import datetime, timezone
import time

maintenant = datetime.now(timezone.utc)
actuel = maintenant.timestamp()

test = time.time()
print(test)
print(f"Seconds since January 1, 1970: {round(test, 4)} or {actuel:.2e} in scientific notation")

x = datetime.today()
date_fait = x.strftime("%b %d %Y")

print(date_fait)