# Power monitoring for the BVN office

First test case for this, potentially productise later

Desk pods/benches will be in 2-8 but probably 6 person groups. Better to make unit deal in modules of 4 plugs.

Can the module run with a pi zero w? What would it need to do? ML would probably need to run locally, is that feasible on a zero?

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

# Combined control unit

These elements can each mqtt (or something) to a server, which can then connect to the app that will be running on a kiosked tablet. (Maybe with physical switches added, in the spirit of the Green switch)

They'd probably be a [fire 7 or 8](https://www.amazon.com/dp/B01GEW27DA/ref=fs_ods_tab_an) which are $50US a piece so they'd be almost disposable!

# Scenarios

*   Tuning light to look at sample boards
*   Setting light level and temperature for mood/productivity
*   Communicating lollies or other things like that
*   Tuning lighting to the task
*   Mad disco party
