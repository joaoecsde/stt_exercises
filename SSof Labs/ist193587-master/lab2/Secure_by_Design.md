# ist193587

## Vulnerabilty

Unauthorized Access

## Where

Situated at http://mustard.stt.rnl.tecnico.ulisboa.pt:22056/

## Impact

Allows to access a page that only the admins should be able to

## Steps to Reproduce

1. After looking at the website and and doing some testing we can see that the cookies that exist are placed after the Nickname text box is filled in and the Go! button is clicked. The cookie that appears has the name user and has a value that seemed kinda like Base64, after copying it to cyberchef we are able to see that it is in fact Base64 and that it represents the Nickname we have inserted.
2. Run the file 'Secure_by_Design.py'.
3. This file allows to insert a random user in the text box and afterwards change the cookie that represents the username of the user to YWRtaW4= (that is admin in Base64) allowing us to get access to the admin page.