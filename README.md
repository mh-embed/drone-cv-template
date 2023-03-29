# MHackers Embedded Drone CV Module Template

## Make your own module
1. Fork this repo, give it a name based on the UID we provide you with. 
  - You can get the UID by contacting a MHackers Embedded group member, DM us in Slack/Discord, or email houhd@umich.edu
2. Change Your Package Name in these files: 
  - <workspace>/src/mhcv_template/ --> <workspace>/src/<your_package_name>/
  - <workspace>/src/<your_package_name>/scripts/cv.py: NODE_CV_UID="mhcv_template" --> NODE_CV_UID=<your_package_name>
  - <workspace>/src/<your_package_name>/package.xml: <name>mhcv_template</name> --> <name> <your_package_name> </name>
  - <workspace>/src/<your_package_name>/package.xml: <name>mhcv_template</name> --> <name> <your_package_name> </name>
  - <workspace>/src/<your_package_name>/CMakeLists.txt: project(mhcv_template)--> project(<your_package_name>)
  - <workspace>/src/<your_package_name>/launch/cv.launch: <node ...> to your package name. 
3. Change Additional Information in <workspace>/src/<your_package_name>/package.xml
