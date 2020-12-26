
'''
curl -X POST -d "username=cfe&password=learncode" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw
" http://127.0.0.1:8000/api/comments/


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY2MTc4fQ._i5wEqJ_OO8wNiVVNAWNPGjGaO7OzChY0UzONgw06D0" -H "Content-Type: application/json" -d '{"content":"some reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'



curl http://127.0.0.1:8000/api/comments/



curl -X POST -d "username=anotheruser123&password=anotheruser123" http://127.0.0.1:8000/api/auth/token/


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyMTIzIiwidXNlcl9pZCI6NywiZW1haWwiOiJhbm90aGVydXNlcjEyM0BnbWFpbC5jb20iLCJleHAiOjE0NjE5NjY0ODF9.KZ991-PGIm63BKikMbDSdFStStJ6uu6WtsraAmbo7BQ

curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyMTIzIiwidXNlcl9pZCI6NywiZW1haWwiOiJhbm90aGVydXNlcjEyM0BnbWFpbC5jb20iLCJleHAiOjE0NjE5NjY0ODF9.KZ991-PGIm63BKikMbDSdFStStJ6uu6WtsraAmbo7BQ" -H "Content-Type: application/json" -d '{"content":"my new reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'



'''



"""

curl -X POST -d "username=CurlUser&password=q1q3q5q7" http://127.0.0.1:8000/api/auth/token/
curl -X POST -d "username=CurlUser&password=q1q3q5q7" http://dyclin99.pythonanywhere.com/api/auth/token/

{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6I
mNmZTEyMyIsImV4cCI6MTYwODk4ODU4OSwiZW1haWwiOiJjZmUxMjNAZ21haWwuY29tIn0.SBp-RDu_2
Ps_SqjCJ3SHejhfBLXmzEdr419SNZ-B6WE"}


curl -X POST -d "username=CurlUser&password=q1q3q5q7&email=curl@example.com&email2=curl@example.com" http://127.0.0.1:8000/api/users/register/

{"username":"CurlUser","email":"curl@example.com","email2":"curl@example.com"}


curl -X POST -d "username=CurlUser&password=q1q3q5q7&email=curl@example.com" http://127.0.0.1:8000/api/users/login/



curl http://127.0.0.1:8000/api/posts/

curl -X DELETE -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjA4OTkwNDQ4LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIn0.gXgQx4LPhH-79Mi_wiZKPppb-ZaPHdiSudcr2NEGcgs" http://127.0.0.1:8000/api/posts/python-and-physics/delete/


eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMSwidXNlcm5hbWUiO
iJDdXJsVXNlciIsImV4cCI6MTYwODk5MDMzOSwiZW1haWwiOiJjdXJsQGV4YW1wbGUuY29tIn0.IObEx
z1_t6H31yVadKrBAHIDnGh18dpef5B6YGlwR6A


"""