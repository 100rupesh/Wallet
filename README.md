
# Wallet Application

Django based app to show the the expenses and income of a user based on the amount that he credits/debit.


## Acknowledgements

 - [Bootstrap Navbar Template](https://getbootstrap.com/docs/5.1/components/navs-tabs/)
 - [DRF ModelSerilizer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
 - [Django Message Framework](https://docs.djangoproject.com/en/4.0/ref/contrib/messages/)


## Setup
### 1. Clone the Project from Git
```git clone https://github.com/100rupesh/Wallet.git```

```cd Wallet```

### 2. Install the dependencies
```pip install -r requirements.txt```

### 3. Run the Project
```python manage.py runserver```

```python3 manage.py runserver``` (if ubuntu linux)
## Walkthrough
##### Before you interact with the application, you to need to first signup/register and then login to your account.At first your account will be disbaled,admin can enable your account through API or admin pannel.Once your wallet is enabled you can either credit the amount or debit it.You will be able to see the transaction report on the right side of your page.
## API Reference
##### There are three api which are : 
###### 1. To get balance of user wallet
###### 2. To activate/enable user wallet
###### 3. To update balance of user wallet

#### Get Balance of User

```http
  GET /get-user-balance/<int:id>/
```



Takes id of the user and returns the balance.

#### Enable User Wallet

```http
  POST /activate-user-wallet/
  request ={
"id":11,
"is_activate":true
}
```

#### Update User Wallet

```http
  POST /update-user-balance/
  request ={
"user":11,
"expense_type":"income",
"amount":111
}

or 

  request ={
"user":11,
"expense_type":"expense",
"amount":111
}
```

