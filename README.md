# This is a cryptographically secure random password generator. 

## Use case:
- API Keys
- access tokens
- session token
- password


## Features: 
- Uses python's 'secrets' module instead of the 'random' module. The secrets module is purpose-built for secure, unpredictable random values.

## Length choice:
Choose the length based on your entropy requirements:
- 20+ characters for API keys, admins, crypto keys
- 16 characters for corporate/finance accounts
- 12 characters for personal accounts

## Storage Security:
A secret password or key is only as good as its storage mechanism. So store securely.
- For user password, use a reputed password manager with no history of leaks to store the password securely
- For keys, use a KMS for storage
- For access tokens, use an encrpyted database or encrypted storage solution like s3 buckets. 
