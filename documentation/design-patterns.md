# Design Patterns
>Unity doesn't allow you to create custom components in code. You have to create them in the UI, and then customize/initalize those objects from code. Those customizeable objects are called prefabs. There is a certain process when a target is found, how it creates the UI and what the User Interface should look like. 


## Prefabs
You must use them extensively throughout the entire process and these are how you get to several objects the user can choose to put overlay their user content.

The list object is an example of a prefab. A prefab is a prefabricated object created in the UI, that you can reference in code. The prefab in this case is the UI, with a preset view with various list elements. You can set the text, colors, font, once you instantiate it into the view. Here's an example: *be sure to have the prefab in the resources folder* 
`GameObject object = (GameObject)Instantiate(Resources.Load("List"));`
^ The above code would create a new GameObject with the List prefab. 
![List Prefab Example](images/prefab.png)

## Image Target UI Creation
This is the process of what happens when the app finds an Image in its database. The design flow is specific to how this works 

Go into more detail about the overall design of the platform and how it works.

Image Target is found. --> Metadata for Target is passed. --> Uses URL in Metadata to get JSON Object Response. --> Instantiates the specified prefab and object in the JSON.
