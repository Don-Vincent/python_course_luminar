# Given Input: user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"} — 
# extract only ["id", "username", "email"]

# Expected Output: {'id': 42, 'username': 'jdoe', 'email': 'jdoe@example.com'}
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
need = ["id", "username", "email"]

extracted = {}
for i in need:
    if i in user:
        extracted[i] = user[i]
print(extracted)

# or

print({i:user[i] for i in need if i in user})
