# Authentication

    User
        Register
        Login
        Profile

# Finance management

    User
        income add
        expense add
        transaction view
        transaction delete

 Authentication endpoint

    POST /auth/register
    POST /auth/login
    GET /auth/me

Transaction endpoint

    POST /transactions
    GET  /transactions
    DELETE / transactions/{transaction_id}

    GET /transactions/analytics/monthly
    GET /transactions/analytics/categories
    GET /transactions/analytics/top-category


    ## Installation
    pip install fastapi, uvicorn
    pip install sqlalchemy
    pip install passlib[bcrypt] bcrypt==3.2.0
    pip install python-jose