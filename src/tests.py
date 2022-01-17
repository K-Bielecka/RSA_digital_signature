import rsa_signature

message = "dscvdfbvgbngnytujkuyj"
keys =  (rsa_signature.generate_keys())
public_key = keys[0]
private_key = keys[1] 
print(keys)

signature = rsa_signature.generate_signature(message,public_key[0], public_key[1], private_key)
is_valid = rsa_signature.verify(message,public_key[0], public_key[1],signature)

print(is_valid)




