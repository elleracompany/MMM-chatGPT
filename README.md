# MMM-chatGPT

This is a work in progress, it is going to start a voice recording and ask chatGPT a question. 
Later it is going to use a screen reader and read the answer back to you.

## Working

To do: create a function that listens to a trigger word, and activates a recorder. 

### how to create Module files

All modules are loaded in the modules folder. The default modules are grouped together in the modules/default folder. Your module should be placed in a subfolder of modules. Note that any file or folder your create in the modules folder will be ignored by git, allowing you to upgrade the MagicMirror² without the loss of your files.

A module can be placed in one single folder. Or multiple modules can be grouped in a subfolder. Note that name of the module must be unique. Even when a module with a similar name is placed in a different folder, they can't be loaded at the same time.


- modulename/modulename.js - This is your core module script.
- modulename/node_helper.js - This is an optional helper that will be loaded by the node script. The node helper and module script can communicate with each other using an integrated socket system.
- modulename/public - Any files in this folder can be accessed via the browser on /modulename/filename.ext.
- modulename/anyfileorfolder Any other file or folder in the module folder can be used by the core module script. For example: modulename/css/modulename.css would be a good path for your additional module styles.
