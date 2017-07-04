# Power monitoring for the BVN office

First test case for this, potentially productise later

Desk pods/benches will be in 2-8 but probably 6 person groups. Better to make unit deal in modules of 4 plugs.

Can the module run with a pi zero w? What would it need to do? ML would probably need to run locally, is that feasible on a zero? YES?! [Check this out](https://blogs.microsoft.com/next/2017/06/29/ais-big-leap-tiny-devices-opens-world-possibilities/)

One input cable would be split, then internally have 4 tracks. Each track is monitored switched.

### Questions

*   If given a pi zero w, would it be crazy to have each plug individually monitored? Would that produce too much wifi chatter?
*   How would this be integrated into the desk? Under mount? Umbilical mount? Under is more commercialisable.

### Considerations

*   The plugs should be (colour?) coded so that there isn't _bench bleed_ (where someone plugs their things into their neighbour's sockets).
*   People will need to be educated about why they need to only plug into their own desk's power.

## Precedents

[synthetic-sensors](http://www.figlab.com/#/synthetic-sensors-2017/) (CMU) Really nice ML+sensor method of identifying what's going on in a room. _Seems_ to be mostly acoustic with a bit of infrared vision.

# Lighting unit

White LED lights, with RGB tone shifters

This turns out the be pretty much [what lifx do](https://www.marcoklobas.net/lifx-smart-bulb-disassembling/), so that's reassuring. They actually use separate R, G ad B LEDs, but I think that .\*s will be just fine. Using white .\*s is probably overkill, and we can get more power for the same money with powerful [cree](https://littlebirdelectronics.com.au/products/cree-xlamp-high-power-led-with-aluminum-chassis-3w-white) type lamps probably.

Aluminum PCBs: [seeed make them](http://support.seeedstudio.com/knowledgebase/articles/1086097-the-material-for-pcb-aluminum-board-fpc), might distribute heat better in final version. If there are 20 of these arms, and each one has 3m of light, then making custom PCBs might make sense. We can then tune the mix of Cree powerful whites, .\* RGBs to tune the colour.

The lighting unit would also have sensors in it, potentially taking on the sensicorn role. It could have a grid eye sensor to work out which chairs are occupied. The combination of "someone is exactly here" and "a specific person is in this area" might be really valuable. (Aiden Ray: the grid eye is a pretty nice addition. and really helps in the indoor positioning front.)

*   [Grid-EYE-breakout - PureEngineering](http://www.pureengineering.com/projects/grid-eye-breakout) not made any more?
*   [eewiki breakout](https://eewiki.net/display/projects/Panasonic+GridEYE+Breakout+Board+and+GUI) $50 us, cheapest
*   [click breakout](https://shop.mikroe.com/click/sensors/grid-eye)
*   [little bird, bt breakout, AMG8832 Infrared Array Sensor](https://littlebirdelectronics.com.au/products/amg8832-infrared-array-sensor) expensive, overkill? Product Overview The GridEYE Sensor boards combines the versatility of the MEMs based sensor with Bluetooth enabled connectivity and the option of mounting the

Grid eye sensor is ~$20US a pop, has a 60° FOV. Will need to check what it could see from the room.


### Questions
*   Can we get enough light intensity?
*   Can we tune the colour temperature?
*   Can we shed heat and not burn out the LEDs
*   Can we power it all without needing a crazy PSU?
*   What scale should we be thinking at? Single desk, pods of n?

# Combined control unit

These elements can each mqtt (or something) to a server, which can then connect to the app that will be running on a kiosked tablet. (Maybe with physical switches added, in the spirit of the Green switch)

They'd probably be a [fire 7 or 8](https://www.amazon.com/dp/B01GEW27DA/ref=fs_ods_tab_an) which are $50US a piece so they'd be almost disposable!

# Scenarios

*   Tuning light to look at sample boards
*   Setting light level and temperature for mood/productivity
*   Communicating lollies or other things like that
*   Tuning lighting to the task
*   Mad disco party


# System topology

![](/assets/system_sketch1.jpg)

I did a sketch, it might help explain some things. Explaining the parts:

### control
The control would be a fixed way of interacting with the system. It'd be input and output. It would be able to turn the lights on and off, and control them etc. It would also give output, so things like the values from the sensors, history etc. It would probably be an Amazon fire tablet because they are cheap, have screens, and can connect to a network.

It might, or not, have some physical buttons on it? A big off switch for the pod, or manual lighting controls?

### desk
I've only showed these as a surface, they might be hight adjustable, they might be rectangles or they might be blobby stars. I'm failry sure they'll be horizontal, but we can't be sure!

### thing
This is a _something_ that connects the desks to the ceiling, it holds the power and data. It might also be useful to hold up the _control_

### power and data
Each desk will be supplied with power and data. Where this comes from is uncertain, but it's definitely going to _end up_ at the desk. We need to make sure that each desk has its own power and that we don't get cross plugging.

### power monitoring
This will either be at the _thing_ where all the power comes together, or it'll be at each desk. It'll measure and control (interrupt) the power supply.

### light and sense
This will contain the lighting and more of the sensing. This will have tunable coloured light. Currently looking at dotstar LEDs to give lots of control, but we might need to add more power from some cree type things.

### S³
This will be the next version, of the S³ (Sensicorn stampede stick). There will be a lot of these hopefully!

### computer
This powers the S³ and does all the heavy lifting of the data transfer.

## How these parts are joined up
