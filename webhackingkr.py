import base64

val_id = "admin".encode()
val_pw = "nimda".encode()

for i in range(20):
    val_id = base64.b64encode(val_id)
    val_pw = base64.b64encode(val_pw)

val_id = val_id.decode()
val_pw = val_pw.decode()

val_id = val_id.replace("1", "!")
val_id = val_id.replace("2", "@")
val_id = val_id.replace("3", "$")
val_id = val_id.replace("4", "^")
val_id = val_id.replace("5", "&")
val_id = val_id.replace("6", "*")
val_id = val_id.replace("7", "(")
val_id = val_id.replace("8", ")")

val_pw = val_pw.replace("1", "!")
val_pw = val_pw.replace("2", "@")
val_pw = val_pw.replace("3", "$")
val_pw = val_pw.replace("4", "^")
val_pw = val_pw.replace("5", "&")
val_pw = val_pw.replace("6", "*")
val_pw = val_pw.replace("7", "(")
val_pw = val_pw.replace("8", ")")

print("id : {}".format(val_id))
print("pw : {}".format(val_pw))
