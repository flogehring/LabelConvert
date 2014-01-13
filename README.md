LabelConvert
============

Converts Xcode localized string files to XML files for Android projects.  
It scans the *.lproj subfolders for the `localizable.strings` files.  
Right now it only works for Android-style keys.  

##Usage

- Copy `labelConvert.py` into your Xcode project.
- Add your languages to it: `langs = ['de', 'en']`
- Call `python labelConvert.py` from the command line.


##Example

	"SEARCH_FIELD_PLACEHOLDER" = "Search";
	"BUTTON_SEARCH" = "Search";
	"BUTTON_CONTINUE" = "Continue";
	"BUTTON_SUBMIT" = "Submit";
	"BUTTON_SELECT_ALL" = "Select all";
	"BUTTON_SELECT_NONE" = "Select none";
	"BUTTON_OK" = "OK";
	"BUTTON_CANCEL" = "Cancel";
	"BUTTON_CLOSE" = "Close";

… will turn into … 

	<resources>
		<string name="SEARCH_FIELD_PLACEHOLDER">Search</string>
		<string name="BUTTON_SEARCH">Search</string>
		<string name="BUTTON_CONTINUE">Continue</string>
		<string name="BUTTON_SUBMIT">Submit</string>
		<string name="BUTTON_SELECT_ALL">Select all</string>
		<string name="BUTTON_SELECT_NONE">Select none</string>
		<string name="BUTTON_OK">OK</string>
		<string name="BUTTON_CANCEL">Cancel</string>
		<string name="BUTTON_CLOSE">Close";</string>
	</resources>