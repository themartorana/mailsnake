MailSnake
=========

`MailSnake` is a Python wrapper for MailChimp APIs.

Installation
------------
    pip install mailsnake

Usage
-----

```python
from mailsnake import MailSnake
from mailsnake.exceptions import *

ms = MailSnake('YOUR MAILCHIMP API KEY')
try:
    ms.ping() # returns "Everything's Chimpy!"
except MailSnakeException:
    print 'An error occurred. :('
```

You can also catch specific errors:

```python
ms = MailSnake('my_wrong_mailchimp_api_key_that_does_not_exist')
try:
    ms.ping() # returns "Everything's Chimpy!"
except InvalidApiKeyException:
    print 'You have a bad API key, sorry.'
```

The default API is MCAPI, but STS or Export can be used by supplying an api argument set to 'sts' or 'export' respectively. Here's an example:

```python
mcsts = MailSnake('YOUR MAILCHIMP API KEY', api='sts')
mcsts.GetSendQuota() # returns something like {'Max24HourSend': '10000.0', 'SentLast24Hours': '0.0', 'MaxSendRate': '5.0'}
```

Note
----

API parameters must be passed by name. For example:

```python
mcapi.listMemberInfo(id='YOUR LIST ID', email_address='name@example.com')
```

API Documentation
-----------------

Note that in order to use the STS API you first need to enable the Amazon Simple Email Service [integration](https://us4.admin.mailchimp.com/account/integrations/ "MailChimp Integrations") in MailChimp.

[MailChimp API v1.3 documentation](http://apidocs.mailchimp.com/api/1.3/ "MCAPI v1.3")

[MailChimp STS API v1.3 documentation](http://apidocs.mailchimp.com/sts/1.0/ "STS API v1.0")

[MailChimp Export API v1.0 documentation](http://apidocs.mailchimp.com/export/1.0/ "Export API v1.0")
