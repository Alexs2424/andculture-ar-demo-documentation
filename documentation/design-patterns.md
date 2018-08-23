# Design Patterns
>Unity doesn't allow you to create custom components in code. You have to create them in the UI, and then customize/initalize those objects from code. Those customizeable objects are called prefabs. There is a certain process when a target is found, how it creates the UI and what the User Interface should look like. 

# Platform/App Design
>This is the overall design of how the app works, and interacts with Vuforia to create the UI. 
The AR Reader App is designed so that when it detects an Image Target (Image for the phone to detect) it displays a User Interface that the user can interact with. Since we're using Unity it's not as easy as it sounds. 

#### Platform Workings Overview
1. **Vuforia is initalized (on default when app starts)**
2. **App is looking for Image Targets in database** 
3. **Image Target is detected** 
    - When the Image Target is detected in Unity, a couple pieces of information are automatically transferred from Vuforia's database. You get the rating of how good of an Image Target is able to be detected, the image target name, if the target is active, date modified, and most importantly metadata.
4. **Parses metadata from Image Target** 
    - (usually in JSON form, doesn't *have* to be) to understand what object should be created, where it should be postiioned, how interactable it is, and how many image targets you would like.
5. **Instantiates the specified objects with their prefabs**

## Prefabs
You must use them extensively throughout the entire process and these are how you get to several objects the user can choose to put overlay their user content.

The list object is an example of a prefab. A prefab is a prefabricated object created in the UI, that you can reference in code. The prefab in this case is the UI, with a preset view with various list elements. You can set the text, colors, font, once you instantiate it into the view. Here's an example: *be sure to have the prefab in the resources folder* 
`GameObject object = (GameObject)Instantiate(Resources.Load("List"));`
^ The above code would create a new GameObject with the List prefab. 
![List Prefab Example](images/prefab.png)

## Image Target UI Creation
This is the process of what happens when the app finds an Image in its database. The design flow is specific to how this works 
