#include <stdio.h>
#include <string.h>
#if defined WIN
  #include <lusb0_usb.h>    // this is libusb, see http://libusb.sourceforge.net/
#else
  #include <usb.h>        // this is libusb, see http://libusb.sourceforge.net/
#endif

int main (int argc, char **argv)
{

//	cout << "in MAIN!!!!!!!!!!!!!";


  bool debug = false;
  bool readToNewline = false;
  int arg_pointer = 1;
  int charsToRead = 0;
  char thechar = ' ';

  while (arg_pointer < argc) {

    if (strcmp(argv[arg_pointer], "--help") == 0) {
      printf("DigiUSB Receive - Usage:\nreceive [--help] [--chars n] [--read-to-newline] [--debug]\n\
        Note: Unless chars or read-to-newline is set, it will read until nothing is left.");
      return 0;
    }
    else if(strcmp(argv[arg_pointer], "--debug") == 0) {
      debug = true;
    }
    else if(strcmp(argv[arg_pointer], "--read-to-newline") == 0) {
      readToNewline = true;
    }
    else if(strcmp(argv[arg_pointer], "--chars") == 0) {
      arg_pointer++;
      charsToRead = atoi(argv[arg_pointer]);

    }
    arg_pointer++;

  }
 



  struct usb_bus *bus = NULL;
  struct usb_device *digiSpark = NULL;
  struct usb_device *device = NULL;

  if(debug) printf("Detecting USB devices...\n");

  // Initialize the USB library
  usb_init();

  // Enumerate the USB device tree
  usb_find_busses();
  usb_find_devices();

  // Iterate through attached busses and devices
  bus = usb_get_busses();
  while(bus != NULL)
  {
     device = bus->devices;
     while(device != NULL)
     {
        // Check to see if each USB device matches the DigiSpark Vendor and Product IDs
        if((device->descriptor.idVendor == 0x16c0) && (device->descriptor.idProduct == 0x05df))
        {
           if(debug) printf("Detected DigiSpark... \n");
           digiSpark = device;
        }

        device = device->next;
     }

     bus = bus->next;
  }

  // If a digiSpark was found
  if(digiSpark != NULL)
  {
     int result = 0;
     int i = 0;
     int numInterfaces = 0;
     struct usb_dev_handle *devHandle = NULL;
     struct usb_interface_descriptor *interface = NULL;
    
        
    devHandle = usb_open(digiSpark);
         
    if(devHandle != NULL)         {
        /*result = usb_set_configuration(devHandle, digiSpark->config->bConfigurationValue);
        if(result < 0) {if(debug) printf("Error %i setting configuration to %i\n", result, digiSpark->config->bConfigurationValue); return 1;}*/
		

        numInterfaces = digiSpark->config->bNumInterfaces;
        interface = &(digiSpark->config->interface[0].altsetting[0]);
        if(debug) printf("Found %i interfaces, using interface %i\n", numInterfaces, interface->bInterfaceNumber);
   
        /*result = usb_claim_interface(devHandle, interface->bInterfaceNumber);
        if(result < 0) {if(debug) printf("Error %i claiming Interface %i\n", result, interface->bInterfaceNumber); return 1;}*/
  
        // Try to read from the digispark
		if(debug) printf("Read from Digispark: ", thechar);
		while(thechar != 4)		  {

			
			thechar = 4;
			result = usb_control_msg(devHandle, (0x01 << 5) | 0x80, 0x01, 0, 0, &thechar, 1, 1000);
			if(result < 0)
			{
				if(debug) printf("Error %i reading from USB device\n", result);
				break;
			} 
			else
			{
				if(readToNewline){
				if(thechar == '\n')
					break;
				}
				if(thechar != 4)
				printf("%c", thechar);

				i++;
				if(i>=charsToRead && charsToRead>0)
				break;
			}
		}
			if(debug) printf("\n", thechar);

			result = usb_release_interface(devHandle, interface->bInterfaceNumber);
			if(result < 0) {if(debug) printf("Error %i releasing Interface 0\n", result); return 1;}

			usb_close(devHandle);
    }
     
  }
  else{
    printf("No Digispark Found");
    return 1;
  }     
        
  return 0;
}
