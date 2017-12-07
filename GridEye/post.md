We're at it again, sticking sensors up in your grill...<!--more-->

In the world of walking-path mapping, there's always been a tension between dropping a lot of ca$h on a thermal camera and trying to figure out some sort of way to infer it for a bit less money. There's a new sensor from Panasonic that seems to do that. It's an 8×8 thermal camera. Just to make that clear, that's 64 pixels, not <em>mega</em>pixels! That means that we can stick them in sensitive locations without any fear of catching anything to worry about. This is perfect for places like schools, or changing rooms... or toilets.

There's a pretty well established set of rules about where men stand at urinals. You can <a href="http://www.urinalman.com/">take a test</a> to see how well you conform to the reported norms, or you can read about what others have <a href="http://guestblog.scientopia.org/2012/03/20/the-art-of-selecting-a-urinal/">written</a> <a href="https://goodmenproject.com/good-feed-blog/7-rules-of-mens-bathroom-etiquette/">about</a> this <a href="http://www.telegraph.co.uk/men/thinking-man/10402308/Urinal-etiquette-the-10-commandments.html">complex</a> and <a href="https://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/">deep topic</a>. The problem with all this analysis is that it's reported, it's what people <em>say</em> they do. If you've been following the thread of <a href="http://tropos.bvn.com.au/author/bdoherty/">my posts</a> over the years, you'll know that I'm never satisfied with that!

So, we've got two problems here:
<ul>
	<li>We've got a new bit of hardware that we want to understand</li>
	<li>There's a bit of human behaviour that's not been experimentally tested nearly enough.</li>
</ul>
So the obvious solution to these problems is that we make a little experiment to test the theory and to test the hardware.

<img src="http://tropos.bvn.com.au/wp-content/uploads/2017/11/themal.jpg" alt="themal" />

The sandwich is a Panasonic Grideye sensor, on its development board on the left, then a big chunk of foam because why not, and then a Raspberry Pi, then another bit of foam to point it in the right direction. The Grideye is measuring the temperature of a grid of 64 points, and the Pi is writing the temperatures to a spreadsheet. That's it!

It's a really fast test, then we can do some really basic analysis and see if people really do behave according to the rules. E.g. "if some heat turns up in section A and stays there for more than 5 seconds then that's probably a hit" but we'll know better once we've looked at the results.

<img class="alignnone size-full wp-image-37436" src="http://tropos.bvn.com.au/wp-content/uploads/2017/11/demo-grid-eye-segmented.gif" alt="demo-grid-eye-segmented" width="500" height="504" />

There was a paper at Acadia about using this exact technique to do people tracking: <a href="http://tropos.bvn.com.au/wp-content/uploads/2017/11/acadia17_138.pdf">A Passive System for Quantifying Indoor Space Utilization</a>. It's got some limitations, but if you don't care who's who, and you've got high ceilings, it's great! We did something really similar, at Smart geometry in Copenhagen, back when I still had a hairstyle! This new hardware makes it <em>way</em> easier and cheaper!
<h1>Important points:</h1>
<ul>
	<li>This thing is mainly looking for the backs of heads.</li>
	<li>This is a hardware test and a fun experiment</li>
	<li>We're not tracking who's at the urinals at any given time, so if you really want a thermal picture of you then take a careful note of the time and we can sort you out.</li>
	<li>Expect to see results early next week</li>
	<li>We're still working on the Sensicorn data, and we'll have that to you as soon as we figure it out.</li>
</ul>
Come and see me if you want me to run you through how it works or if you have any other questions.
