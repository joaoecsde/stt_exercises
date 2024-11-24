# ist193587

## Vulnerabilty

Cross-site scripting.

## Where

On the search bar of the user.

## Impact

Allows the user to execute script commands on his browser in this case to get the cookies.

## Steps to Reproduce

1. First I discovered where it could be executed, since what it's being searched reflects on the browser I believed that here is where the vulnerability exists. So to test it first i did a simple `<script>alert(1)</script>` and after confirming my belief i used this payload to get the cookies `<script>alert(document.cookie)</script>` .