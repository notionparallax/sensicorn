/*  checkthis.c  */
#include <stdio.h>
#include <string.h>
#if defined WIN
#include <lusb0_usb.h>    // this is libusb, see http://libusb.sourceforge.net/
#else
#include <usb.h>        // this is libusb, see http://libusb.sourceforge.net/
#endif
#include <curses.h>
#include <stdlib.h>


int main(int argc, char **argv)
{


	bool sendLine = true;
	int arg_pointer = 1;


	while (arg_pointer < argc) {

		if (strcmp(argv[arg_pointer], "--no-new-line") == 0) {
			sendLine = false;
		}

		arg_pointer++;
	}



	struct usb_bus *bus = NULL;
	struct usb_device *digiSpark = NULL;
	struct usb_device *device = NULL;

	// Initialize the USB library
	usb_init();

	// Enumerate the USB device tree
	usb_find_busses();
	usb_find_devices();

	// Iterate through attached busses and devices
	bus = usb_get_busses();
	while (bus != NULL)
	{
		device = bus->devices;
		while (device != NULL)
		{
			// Check to see if each USB device matches the DigiSpark Vendor and Product IDs
			if ((device->descriptor.idVendor == 0x16c0) && (device->descriptor.idProduct == 0x05df))
			{
				digiSpark = device;
			}

			device = device->next;
		}

		bus = bus->next;
	}
	if (digiSpark == NULL)
	{
		printf("No Digispark Found");
		return 1;
	}

	int result = 0;

	int numInterfaces = 0;
	struct usb_dev_handle *devHandle = NULL;
	struct usb_interface_descriptor *interface = NULL;


	devHandle = usb_open(digiSpark);

	if (devHandle != NULL)
	{
		/*result = usb_set_configuration(devHandle, digiSpark->config->bConfigurationValue);
		if(result < 0) {printf("Error %i setting configuration to %i\n", result, digiSpark->config->bConfigurationValue); return 1;}*/

		numInterfaces = digiSpark->config->bNumInterfaces;
		interface = &(digiSpark->config->interface[0].altsetting[0]);
		//if(debug) printf("Found %i interfaces, using interface %i\n", numInterfaces, interface->bInterfaceNumber);

		/*result = usb_claim_interface(devHandle, interface->bInterfaceNumber);
		if(result < 0) { printf("Error %i claiming Interface %i\n", result, interface->bInterfaceNumber); return 1;}*/


	}