# Site Views
Count and display your site's views with this super lightweight minimal view recorder.

### Summary
**Site Views** is a javascript library to display and count your site's views without any chunky servers or expensive services. In just one HTML line, you can setup your counter. With customizable styles, **you** choose how you want to output content.

### Usage in HTML
##### Add text
Simply insert the following into your document:

    This site has <script src="https://site-views.herokuapp.com/js/text/{site-name}"></script> views.

The above will return the amount of views your site has gotten. Everytime a request is made to your page, the number will go up one.

![](media/plain-text.gif)

To style the text returned by the last code block, you can add the url paramter `tag`. For example...

    This site has <script src="https://site-views.herokuapp.com/js/text/{site-name}?tag=strong"></script> views.

This will make a `<strong>` tag, with it's contents being the views. 

![](tag.gif)

You can use css to style these too!

    <style>
        strong { color: red; }
    </style>
    This site has <script src="https://site-views.herokuapp.com/js/text/{site-name}?tag=strong"></script> views.

![](media/tag.gif)

##### Add badge
To add a badge to your document, add the following to the document:

    <h2>My Cool Site</h2>
    <script src="https://site-views.herokuapp.com/js/badge/{site-name}"></script>

![](media/plain-badge.gif)

You can change the color of the badge by adding the URL argument `color`. The supported colors are aqua, black, blue, brighred, brightyellow, fuchsia, gray, green, lightgrey, lime, maroon, navy, olive, orange, purple, red, silver, teal, white, yellow, yellowgreen.

    <h2>My Cool Site</h2>
    <script src="https://site-views.herokuapp.com/js/badge/{site-name}?color=blue"></script>

![](media/color.png)

You can center setting the URL argument `center` to `True`.

    <center>
        <h2>My Cool Site</h2>
    <center>
    <script src="https://site-views.herokuapp.com/js/badge/{site-name}?color=blue&center=True"></script>

![](media/center.gif)