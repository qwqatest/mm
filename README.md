• Adding adb to the Mac PATH. Run in terminal:
  "echo 'export PATH=$PATH:~/Library/Android/sdk/platform-tools/' >> ~/.bash_profile

  source ~/.bash_profile"
  Than: "adb"and than "adb devices" with connected device
• Install Node.js and npm. Running: "brew install node"
• To verify that all of Appium's dependencies are met you can use appium-doctor. Install it with npm install -g appium-doctor, then run the appium-doctor command, supplying the --ios or --android flags to verify that all of the dependencies are set up correctly.
• Download and install JDK
• Adding JAVA_HOME and ANDROID_HOME to .bash_profile file:
   - Open the TextEdit app
   - Navigate to File → Open
   -  in center drop down, be sure to select Home
   - Then, use COMMAND+SHIFT+. to show hidden files
  export PATH=$PATH:/usr/local/bin
  export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
  launchctl setenv STUDIO_JDK /library/Java/JavaVirtualMachines/jdk1.8.0_25.jdk
  export ANDROID_HOME="/Users/sergey/Library/Android/sdk"
  export ANDROID_TOOLS="/Users/sergey/Library/Android/sdk/tools"
  export ANDROID_PLATFORM_TOOLS="/Users/sergey/Library/Android/sdk/platform-tools"
  PATH=$PATH:$ANDROID_HOME:$ANDROID_TOOLS:$ANDROID_PLATFORM_TOOLS
  export PATH=$JAVA_HOME/bin:$PATH
• Install Appium Python client: "pip install Appium-Python-Client"
• Install Appium UiAutomator2 Driver: "npm install appium-uiautomator2-driver"
• Install carthage: "brew install carthage"
• PyCharm > Preferences > Project Interpreter > Add "Appium-Python-Client"