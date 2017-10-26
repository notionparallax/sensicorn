# What do we want to sense and why?

## Introduction

So far, the sensicorn project has measured only one thing, the bluetooth signal strength of the badges that we all wore[1. if you started since the experiment finished...]. Since then we've been working on what else we might be able to tell from sensing other things.

As a precursor it's important to remember that we almost never care about what we're sensing directly. Only what we can infer about something else by looking at the sensor data. An example might be heart rate. If it jumps from 60 beats per minute to 180 bpm (acording to a heart rate monitor) then all the sensor has told us is that your pulse has spiked[1. actually it's actually only told us about electrical activity in your chest.], we're left to speculate about why. Did a tigerstart chasing you? Did you meet the love of your life? The heart rate data alone can't tell us. We need a context, and more data sets/sources gives us more context.

The main motivation for sensing is to understand the world better. In our case to understand our tiny corner of the world i.e. the Sydney studio[1. Understanding the Sydney studio is actally a prototype for understanding more of the world]. There are two main goals. One is to understand how workplaces work, the other is specifically focused on how _we_ work.

The broad goal helps us design better workplaces for others. We realise that we (BVN) are different to a lot of our clients, so anything we learn isn't _completely_ transferrable. My assumption is---and I need to test this---that we're more similar than we imagine[1. A bit liek our similarity to chimps...]. That similarity makes what we learn transferrable. In the short term, instrumenting our workplace alows us to prototype the method of instrumenting other workplaces, which will give us an answer to the <q>how different</q> question.

Part two, understanding how _we_ work gives us the insights that katerine has talked so pasionately about. We'll be able to understad what it is that we do well, and position ourselves to make the most of these skills and attributes. This is really important in the comming onslaught of automation [1. link to mongol post]. There are two possible responses to it and understanding what it is that we do that is a genuine value add, rather than a supporting character, positions us well to survive the transition to a thriving position in the new economy.


## After that introduction, what do we actually want to sense?

We're looking at three main packages, stick based, desk based and sky based. Or, if you like cool names:

1. the Sensicorn Stampede Stick (or S³)---stick based
2. the Phreak Guardian---desk based
3. The Big Boo---sky based

These are all working titles, so if you've got a better one, then sound off in the comments.

# S³

The S³ is a small and cheap environmental sensor. It has a temperature, sound and light sensor. It also has a very nice colour changing LED that can be driven by the user's computer. The important thing about it being cheap is that it's possible to get incredible densities of them. That gives really good spatial resolution to the environmental data. They are about 1/10th [fix frac] of the price of comparible sensors currently available, and also have a way of giving the user feedback about their word through the LEDs. That could be about the bhysical environment, or it could notify about anything that can be connected to IFTTT[1. explain it]. This is part of my ethical position on not taking without giving back; it's only a small gesture, but I'd love to be able to pop up a red light to tell people that I'm in focus mode.

The way we're going to get the cost down is through manufacturing volume. 10 of them will cost [X] each to make, but 1000 will cost [Y] each to make. We're going to derisk that through kickstarter.

# Phreak Guardian

This package does two things. One is to give individuals control and visibility of their electricity usage. Two is to give us a better idea of occupant behaviour. Both of these ideas go back as far as about 2011 and the "Green Switch"[1. The Green switch....]. This does all of that, and a bit more. (_and_ for much less money!)

_What does it sense?_ It has an electrcal power sensor and a desk vibration sensor. It also controls a switch that can turn off the power to that desk. The electricty sensing can tell how much current is being pulled by that desk i.e. what the power bill will be. It can also "hear" the sound of things plugged into the desk. Each device adds a signal to the power signature, like different instuments combine to make music. This sensor will be able to separate those sounds and tell if a monitor and a phone charger are plugged in to the desk. That's important for future designs as it tells us what people really do and how they modify their envornment to make it suit their needs.

<figure>
![](http://tropos.bvn.com.au/wp-content/uploads/2017/07/WaveAdditionhappy.png)
<figcaption>
**A** is the signal as we read it. If we remove the 'pure' AC signal (**C**) we're left with **B** which by using some clever (magic) that I don't really understand (can't make AI with out Aiden) we can work out what the instruments that make up the sound.
</figcaption>
</figure>

The desk vibration sensor is also "listening": if you put your ear to the desk and then draw or type or sleep, the you'll be able to hear it. You won't be able to hear _what_ anyone is saying on the phone, but you might be aqble to tell _that_ they are talking. This is a really elegant solution to the a problem that we discovered at the same time as we were developing the green switch. [Greentrac](https://www.eventzero.com/Greentrac/) inferred our power usage from our computer usage, it also told us about desk ocupancy rates. This was really interesting because it told us that people used their computers 40-60% of the time. It's risky to infer that because only 60% of the computers are being used[1. mice moving, screens on, etc.] that only 60%of the desks are occupied. A quick walk around the officeshows people sketching, reading paper documents, having impromptue desk meetings, using iPads, all _kinds_ of things. By using a desk vibration sensor we'll be able to get a more accurate read on desk occupancy. It'll also give us an aidea about the proportions of each day that we do each _type_ of thing. Knowing that activity breakdown also lets us knwo our risk of automation [see the post about mongols!]. So in summary, the Phreak Guardian tells us about desk ocupancy behaviour and gives people control and visibility of their electricity consumption.

## The Big Boo

![The Big Boo comes after Mario](http://tropos.bvn.com.au/wp-content/uploads/2017/07/fc6dc29b17632b63b2fe8995403355dd.gif)

This is actually a bucket for all the rest of the sensing work. We'd like to have some kind of way of high quality air composition sensing. Cheap CO<sub>2</sub> sensors are like [mining canaries](https://media.giphy.com/media/xT5LMJGCAlmI3iPQ8o/giphy.gif), they'll warn you about lethal levels, but can't give you subtle distincions in gas mixes. Do you feel sleepy mid afternoon because of high CO<sub>2</sub> levels or because you are full of Jimmy's recipe? With a sensible sensing budget we could only justify one set of gas sensors, so it would be silly to leave them in one place. We could get a student to push a crash cart around, but it's 2017[1. You're welcome Max Goodbury], let's get an autonomous robot to do it. Navigating around on the ground is hard, a drone would be easier, but 'copter-drones are noisy. Hence a blimp drone: The Big Boo!

<figure>
![](http://tropos.bvn.com.au/wp-content/uploads/2017/07/big_boo.png)
<figcaption>
Just an idea: Here we've got a drone, but the helium baloon [O](https://www.google.com.au/search?q=foil+balloon+o&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiPgN-3-ajVAhXBTrwKHS8hAK8Q_AUICigB&biw=1220&bih=930)s
</figcaption>
</figure>

This would be a platform for expensive, mobile sensing that used Simultanious Localisation And Mapping (SLAM[1. Who would have thought I'd get to write about SLAM twice in one week!]) to measure things all over the studio to understand even more things.

![](http://tropos.bvn.com.au/wp-content/uploads/2017/07/gif-demo-grid-eye-400.gif)
![](http://tropos.bvn.com.au/wp-content/uploads/2017/07/513629d2777cf_OBoyle_EA0213_PANASONIC_Fig-2.jpg)

We're also looking into what we can do wih a low resolution (8×8 ![](https://image.freepik.com/free-icon/chess-board_318-119542.jpg)) thermal camera. As each component gets cheaper and better as [the peace dividend of the smartphone wars](http://foreignpolicy.com/2013/04/29/epiphanies-from-chris-anderson/)[1. "It’s hard to argue that we’re not in an exponential period of technological innovation. The personal drone is basically the peace dividend of the smartphone wars, which is to say that the components in a smartphone — the sensors, the GPS, the camera, the ARM core processors, the wireless, the memory, the battery — all that stuff, which is being driven by the incredible economies of scale and innovation machines at Apple, Google, and others, is available for a few dollars. They were essentially “unobtainium” 10 years ago. This is stuff that used to be military industrial technology; you can buy it at RadioShack now. I’ve never seen technology move faster than it’s moving right now, and that’s because of the supercomputer in your pocket." Epiphanies from Chris Anderson - http://foreignpolicy.com/2013/04/29/epiphanies-from-chris-anderson/] I see it as an oportunity to use more, rather than save money. With more, more is possible. That sounds lieka  truism, but with 1 camera you get a picture, with many you can have a 3d scene thanks to photogrametry. So one 8×8 view ins









[‘Smarkant’: IKEA Bekant Adjustable Sit/Stand Table Controller Reverse-Engineered, Controlled with Alexa](https://blog.adafruit.com/2017/03/27/smarkant-ikea-bekant-adjustable-sitstand-table-controller-reverse-engineered-controlled-with-alexa/)

[IKEA Bekant Desk, motorised hack?](https://www.eevblog.com/forum/beginners/ikea-bekant-desk-motorised-hack/)

https://github.com/vojto/Bekant

https://github.com/robin7331/IKEA-Hackant

https://robertaramar.wordpress.com/2017/03/09/hacking-an-office-desk/
