URL_USERS = {
    "rule": "/users",
    "methods": ["POST"]
}

URL_LOGIN = {
    "rule": "/login",
    "methods": ["POST"]
}

URL_PROCESSES = {
    "rule": "/processes",
    "methods": ["POST", "GET"]
}

URL_PROCESS_UPDATE = {
    "rule": "/processes/<int:process_id>",
    "methods": ["PUT"]
}