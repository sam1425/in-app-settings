	so this is a reminder how to embed files
images just save the images in the enbeded folder(by default is  \vault\)if you copy and paste it it'll be automatically assigned 

![[../Enbeded/Pasted image 20240508203407.png]]
if you wanna use something more like a post you can just copy the embeded html made by almost all apps
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">thank you for 100 followers! <a href="https://t.co/iCij3uJWYO">pic.twitter.com/iCij3uJWYO</a></p>&mdash; Tofu (@TofuPixel) <a href="https://twitter.com/TofuPixel/status/1787843426764853444?ref_src=twsrc%5Etfw">May 7, 2024</a></blockquote>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/ehTIhQpj9ys?si=ZCAwhEXZf10cij2x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
[2:20](https://www.youtube.com/embed/ehTIhQpj9ys?si=ZCAwhEXZf10cij2x)
![[../Enbeded/Pasted image 20240508205513.png]]
you can also enbed twiters 
<iframe border=0 frameborder=0 height=250 width=550  
 src="https://twitter.com/year_progress/status/1788235913434140716"></iframe>

```html
$(document).ready(function() {
    /* find all iframes with ids starting with "tweet_" */
    $("iframe[id^='tweet_']").load(function() {
        this.contentWindow.postMessage({ element: this.id, query: "height" },
            "https://twitframe.com");
    });
});

/* listen for the return message once the tweet has been loaded */
$(window).bind("message", function(e) {
    var oe = e.originalEvent;
    if (oe.origin != "https://twitframe.com")
        return;
	
    if (oe.data.height && oe.data.element.match(/^tweet_/))
        $("#" + oe.data.element).css("height", parseInt(oe.data.height) + "px");
});
```

https://twitframe.com
